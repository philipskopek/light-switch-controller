import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #Set pin number configuration to BCM numbering
 #button set to GPIO2
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False) # Ignore warning for now




GPIO.add_event_detect(2, GPIO.FALLING)
while True:
    if GPIO.event_detected(2):
        print('Button pressed')
