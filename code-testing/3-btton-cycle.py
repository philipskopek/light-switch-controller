import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Set pin number configuration to BCM numbering
 #button set to GPIO2
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False) # Ignore warning for now
button_cycle = 0

def button_callback(channel):
    global button_cycle
    if (button_cycle%3 == 0):
        while True:
            print('button cycle 0')

    elif (button_cycle%3 == 1):
        while True:
            print('button cycle 1')

    elif (button_cycle%3 == 2):
        while True:
            print('button cycle 2')
    button_cycle = button_cycle + 1



GPIO.add_event_detect(2, GPIO.FALLING, callback=button_callback, bouncetime=630)

try:
    while True:
        time.sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()
