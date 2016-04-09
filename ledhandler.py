import RPi.GPIO as GPIO
import time
import sys

GREEN_LED = 18
RED_LED = 17
YELLOW_LED = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Led:
    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.pin = pin

    def on(self):
        GPIO.output(self.pin, True)

    def off(self):
        GPIO.output(self.pin, False)

class LedHandler:
    def __init__(self):
        self.green = Led(GREEN_LED);
        self.red = Led(RED_LED);
        self.yellow = Led(YELLOW_LED);

    def good(self):
        self.green.on()
        self.red.off()
        self.yellow.off()

    def noInternet(self):
        self.green.off()
        self.red.on()
        self.yellow.off()

    def noSoundCard(self):
        self.green.off()
        self.red.on()
        self.yellow.on()

    def noConnection(self):
        self.green.off()
        self.red.off()
        self.yellow.on()

    def onlySilence(self):
        self.green.on()
        self.red.off()
        self.yellow.on()
