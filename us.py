from machine import Pin
import utime

trigger = Pin(27, Pin.OUT)
echo = Pin(26, Pin.IN)
led=Pin(0,Pin.OUT)

def ultra():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    print("The distance from object is ", distance, "cm")
    return distance

while True:
    di=ultra()
    utime.sleep(1)
    if di<=10:
        led.on()
    else:
        led.off()
    
        