import math as mt
import time
import random
from machine import Pin, I2C, RTC, ADC
import ssd1306

window_size = 128,32

oled_reset = Pin(18, Pin.OUT)
oled_reset.off()
oled_reset.on()

analog_input = ADC(Pin(4))

i2c = I2C(0, sda=Pin(8), scl=Pin(9))
display = ssd1306.SSD1306_I2C(128, 32, i2c)


def set_px(position, color, scale):
    #window.set_at((round(position[0]),round(position[1])), color)
    display.pixel(position[0],position[1],int(random.randrange(0,256)<sum(color)/3))
def sin(x): return mt.sin(mt.radians(x))
def cos(x): return mt.cos(mt.radians(x))

def check_collisions(position, objects):
    collisions = []
    for object_ in objects:
        if object_.type == 'cube':
            if position.x > object_.position.x and position.x < object_.position.x + object_.size.x:
                if position.y > object_.position.y and position.y < object_.position.y + object_.size.y:
                    if position.z > object_.position.z and position.z < object_.position.z + object_.size.z:
                        collisions.append(object_)

        if object_.type == 'sphere':
            if mt.sqrt((position.x - object_.position.x)**2 + (position.y - object_.position.y)**2 + (position.z - object_.position.z)**2) <= object_.size:
                collisions.append(object_)
            
    return collisions

class point_3D:
    def __init__(self,coordinates):
        self.x, self.y, self.z = coordinates

    def toArray(self): return (self.x,self.y,self.z)

class color_RGB:
    def __init__(self, color):
        self.r, self.g, self.b = color

    def toArray(self): return (self.r, self.g, self.b)
        
class Camera:
    def __init__(self,position,rotation,FOV):
        self.position = position
        self.rotation = rotation
        self.FOV = FOV

    def cast_ray(self, angle, max_distance, objects, light_sources):
        ray = point_3D(self.position.toArray())
        sin_x_angle, sin_y_angle, cos_x_angle = sin(angle[0]), sin(angle[1]), cos(angle[0])
        continue_ray = True
        while continue_ray:
            collisions = check_collisions(ray, objects)
            if len(collisions) > 0: continue_ray = False
            
            ray.x += sin_x_angle
            ray.y += sin_y_angle
            ray.z += cos_x_angle
            if mt.sqrt(ray.x**2 + ray.y**2 + ray.z**2) >= max_distance: continue_ray = False

        if len(collisions) == 0: return color_RGB((0,0,0))
        collision = collisions[0]
        color = color_RGB(collision.color.toArray())
        #print(collision.color.r)
        color_filters = []
        for light_source in light_sources:
            x1, y1, z1 = ray.toArray()
            x2, y2, z2 = light_source.position.toArray()
            step = 1
            
            dist_to_light_source = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

            diff_x = x2 - x1
            diff_y = y2 - y1
            diff_z = z2 - z1
            hitting_angle = mt.degrees(mt.acos(diff_x / dist_to_light_source))


            
            step_x = diff_x / dist_to_light_source * step
            step_y = diff_y / dist_to_light_source * step
            step_z = diff_z / dist_to_light_source * step

            ray_interrupted = False

            cycles = 0
            while dist_to_light_source > step and not ray_interrupted:
                x1 += step_x
                y1 += step_y
                z1 += step_z
                
                if len(check_collisions(point_3D((x1, y1, z1)), objects)) > 0 and cycles > 2: ray_interrupted = True
                
                dist_to_light_source = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

                cycles += 1

            x1, y1, z1 = ray.toArray()
            dist_to_light_source = mt.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
            light_power = light_source.power/(dist_to_light_source + mt.sqrt((ray.x - self.position.x)**2 + (ray.y - self.position.y)**2 + (ray.z - self.position.z)**2))
            
            if light_power > 1: light_power = 1
            if ray_interrupted: light_power = 0

            raw_light_color = light_source.color.toArray()
            color_filters.append([raw_light_color[0]*light_power,
                                  raw_light_color[1]*light_power,
                                  raw_light_color[2]*light_power])

          
        color_filters_channels = [[color_filter[0] for color_filter in color_filters], [color_filter[1] for color_filter in color_filters], [color_filter[2] for color_filter in color_filters]]
        color_filter = [sum(color_filters_channels[0])/len(color_filters_channels[0])/255, sum(color_filters_channels[1])/len(color_filters_channels[1])/255, sum(color_filters_channels[2])/len(color_filters_channels[2])/255]

        color_filter[0] += 0.25
        color_filter[1] += 0.25
        color_filter[2] += 0.25
        
        if color_filter[0] > 1: color_filter[0] = 1
        if color_filter[1] > 1: color_filter[1] = 1
        if color_filter[2] > 1: color_filter[2] = 1
        
        color.r *= color_filter[0]
        color.g *= color_filter[1]
        color.b *= color_filter[2]
        
        return color
        

    def raycast(self, objects, light_sources, render_distance, quality):
        for angle_y_i in range(round(self.FOV[1]*quality)):
            angle_y = angle_y_i/quality - self.FOV[1]/2
            for angle_x_i in range(round(self.FOV[0]*quality)):
                angle_x = angle_x_i/quality - self.FOV[0]/2
                collision = self.cast_ray((angle_x+self.rotation[0],angle_y+self.rotation[1]), render_distance, objects, light_sources)

                #pp = (round(sin(angle_x)*self.FOV[0]), round(sin(angle_y_i)*self.FOV[1]))
                #print(pp)
                if collision != None:
                    col = collision.toArray()
                    set_px((angle_x_i,angle_y_i), col, (mt.ceil(window_size[0]/self.FOV[0]/quality),mt.ceil(window_size[1]/self.FOV[1]/quality)))
                    display.show()
            
class Light_source:
    def __init__(self,position,power,color):
        self.position = position
        self.power, self.color = power, color

        
class Cube:
    def __init__(self,position,size,color,ID):
        self.position = position
        self.size = size
        self.color = color
        self.type, self.ID = 'cube', ID
        
class Sphere:
    def __init__(self,position,size,color,ID):
        self.position = position
        self.size = size
        self.color = color
        self.type, self.ID = 'sphere', ID
        

Camera_ = Camera(point_3D((0,0,0)),(0,0),(64,32))

objects = [Cube(point_3D((-200,-60,0)),point_3D((400,10,900)), color_RGB((0,255,0)), '1'),
           Cube(point_3D((-40,-60,100)),point_3D((30,30,30)), color_RGB((255,0,0)), '2'),
           ]
#objects = [Cube(point_3D((random.randrange(-200,200),random.randrange(-100,200),random.randrange(0,random.randrange(0,300)))),point_3D((random.randrange(0,20),random.randrange(0,20),random.randrange(0,20))), color_RGB((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))), '1') for __ in range(100)]
lights = [Light_source(point_3D((-80,50,30)), 200, color_RGB((255,255,255)))]





display.fill(1)
Camera_.raycast(objects,lights,400,1)

raycast_loop_tr = threading.Thread(target=raycast_loop)
raycast_loop_tr.start()

        

