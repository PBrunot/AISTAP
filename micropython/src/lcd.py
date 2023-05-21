from machine import Pin, I2C, RTC
import ssd1306
import framebuf
import time
WIDTH = 128
HEIGHT = 32
rtc=RTC()
oled_reset = Pin(18, Pin.OUT, value=1)
i2c=I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)
print(i2c.scan())
# should return 49 (0x31 - I2C buttons) and 60 (0x3c - display)
display = ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
display.poweroff()
display.poweron()
while True:
    display.fill(0)
    display.fill_rect(0, 0, 32, 32, 1)
    display.fill_rect(2, 2, 28, 28, 0)
    display.vline(9, 8, 22, 1)
    display.vline(16, 2, 22, 1)
    display.vline(23, 8, 22, 1)
    display.fill_rect(26, 24, 2, 4, 1)
    display.text('AISTAP', 40, 12, 1)
    display.show()
    time.sleep_ms(200)