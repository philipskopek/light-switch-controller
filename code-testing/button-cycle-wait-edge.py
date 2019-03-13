

#Philip Skopek Light_Strp_Controller
#This script utilizes a push button to cycle trhough different animations
#on the WS2182B LED Strip with a potentiometer for brightness control

#Code is applicable for a raspberry pi.

#Initial Pin assignments are GPIO2 for Button, GPIO18 for DataIn, and
#SPI pins (GPIO8-11) for potentiometer inputs

from rpi_ws281x import *
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) #Set pin numbercd .. configuration to BCM numbering


# LED strip configuration
LED_COUNT = 9      #number of LED pixels
LED_PIN = 18        #GPIO pin connected to the pixels (must support PWM!)
LED_FREQ_HZ = 800000 #LED signal frequency in hertz (usually 800khz)
LED_DMA = 5         #DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 90 #Set to 0 for darkest and 255 for brightest
LED_CHANNEL = 0     # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_INVERT = False #set True to invert the signal (when using NPN transistor level shift)


button = 2 #button set to GPIO2
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#animation running control variable

# Define functions which animate LEDs in various ways.

# Cycles through LED to create rainbow animation.
def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

button_cycle = 0


def animation():
    global button_cycle
    button_cycle=button_cycle+1





#Main program logic follows

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

while True:
    channel = GPIO.wait_for_edge(button, GPIO.FALLING)
    if button_cycle%2 == 0:
        while channel is 0:
            print ("Button Was Pressed 0")
            print ('Color wipe animations.')
            time.sleep(.3)

    elif button_cycle%2 == 1:
        while channel is 0:
            print ("Button Was Pressed 1")
            print ('Theater chase animations.')
    button_cycle = button_cycle + 1
