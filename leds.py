import RPi.GPIO as GPIO
import time

class Leds(Object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
	self.pins = [ 17, 18, 27 ]
	
        
    def turnOnOffPin(pin, on):
        GPIO.setup(pin, GPIO.OUT)
        if on:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)

    def simulateClick(pin)
        self.turnOnOffPin(pin, False)
        time.sleep(0.01)
        self.turnOnOffPin(pin, True)

    def piscarLeds():
        self.simulateClick(pins[2])

    def ligarTodos():
        for pin in self.pins:
            turnOnOffPin(pin, True)

    def desligarTodos():
        for pin in self.pins:
            turnOnOffPin(pin, False)

