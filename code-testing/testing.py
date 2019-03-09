import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Set pin number configuration to BCM numbering
button = 2 #button set to GPIO2
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False) # Ignore warning for now

def button_callback(channel):
    print("Button was pushed!")

GPIO.add_event_detect(4, GPIO.RISING, callback=button_callback, bouncetime=300)

while True:
        time.sleep(20) #you can put every value of sleep you want here..
