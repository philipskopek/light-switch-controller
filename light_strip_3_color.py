#Philip Skopek Light_Strp_Controller
#This script utilizes a push button to cycle trhough different animations
#on the WS2182B LED Strip with a potentiometer for brightness control

#Code is applicable for a raspberry pi.

#Initial Pin assignments are GPIO2 for Button, GPIO18 for DataIn, and
#SPI pins (GPIO8-11) for potentiometer inputs

from rpi_ws281x import *
from time import sleep
from gpiozero import Button, MCP3008
import RPi.GPIO as GPIO
import neopixel
import board

GPIO.setmode(GPIO.BCM) #Set pin number configuration to BCM numbering
pixels = neopixel.NeoPixel(board.D18, 18) #LEDS on GPIO 18, LED count

# LED strip configuration
LED_COUNT = 20 #number of LED pixels
LED_PIN = 18 #GPIO pin connected to the pixels (must support PWM!)
LED_FREQ_HZ = 800000 #LED signal frequency in hertz (usually 800khz)
LED_DMA = 5 #DMA channel to use for generating signal (try 5)
LED_INVERT = False #set True to invert the signal

#create pot objects to refer to MCP3008 channel 0 and 1
pot_brightness = MCP3008(0)
pot_speed = MCP3008(1)

#connect pushbutton to GPIO pin 2, pull-up
button = 2 #button set to GPIO2
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#animation running control variable
button_cycle = 0

while True:
    if GPIO.input(button)== 0:
        print ("Button Was Pressed")
        if button_cycle==0:
            pixels.fill((255, 0, 0))
            button_cycle=1
            sleep(.3)
        elif button_cycle==1:
            pixels.fill((0, 255, 0))
            button_cycle=2
            sleep(.3)
        elif button_cycle==2:
            pixels.fill((210, 0, 210))
            button_cycle=0
            sleep(.3)
