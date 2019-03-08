import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
sleepTime = .1

led = 25
button = 23


GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
BS=False


while True:
    if GPIO.input(button)== 0:
        print ("Button was pressed")
        if BS==False:
            GPIO.output(led, True)
            BS=True
            sleep(.3)
        else:
            GPIO.output(led,False)
            BS=False
            sleep(.3)
