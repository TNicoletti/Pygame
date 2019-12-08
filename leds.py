import RPi.GPIO as GPIO
import time

class Leds(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.pins = [ 17, 18, 27 ]
	
        
    def turnOnOffPin(self, pin, on):
        GPIO.setup(pin, GPIO.OUT)
        if on:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

    def simulateClick(self, pin):
        self.turnOnOffPin(pin, False)
        time.sleep(0.01)
        self.turnOnOffPin(pin, True)

    def piscarLeds(self):
        self.simulateClick(self.pins[2])

    def ligarTodos(self):
        for pin in self.pins:
            self.turnOnOffPin(pin, True)

    def desligarTodos(self):
        for pin in self.pins:
            self.turnOnOffPin(pin, False)

