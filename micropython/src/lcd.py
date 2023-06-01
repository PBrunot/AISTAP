from machine import Pin, I2C, RTC
import ssd1306
import framebuf
import time
WIDTH = 128
HEIGHT = 32
rtc=RTC()

oled_reset = Pin(18, Pin.OUT)
oled_reset.off()
# ensure display reset is held high, otherwise nothing will work
oled_reset.on()

# ESP32 S2 only has one hardware I2C channel, #0 on pins 8 & 9
i2c = I2C(0, sda=Pin(8), scl=Pin(9))
# use default address 0x3C (60) for SSD1306
display = ssd1306.SSD1306_I2C(128, 32, i2c)

display.poweroff()
time.sleep(1)
display.poweron()
cpt = 0
while True:
    display.fill(0)
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.vline(9, 8, 22, 1)
    display.vline(16, 2, 22, 1)
    display.vline(23, 8, 22, 1)
    display.fill_rect(26, 24, 2, 4, 1)
    display.text('AISTAP', 40, 12, 1)
    display.text(str(cpt), 102, 24, 1)
    display.show()
    time.sleep_ms(1000)
    cpt += 1