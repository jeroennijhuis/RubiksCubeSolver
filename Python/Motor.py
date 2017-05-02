# noinspection PyInterpreter
import RPi.GPIO as GPIO
from time import sleep        

class Motor:

    def __init__(self, side, stepperPort, directionPort):
        self.Side = side
        self.StepperPort = stepperPort
        GPIO.setup(stepperPort, GPIO.OUT)  # set stepper pin as an output
        self.DirectionPort = directionPort
        GPIO.setup(directionPort, GPIO.OUT)  # set direction pin as an output

    def Rotate(self, inverse = 0, count = 1):
        GPIO.output(self.DirectionPort, inverse)
        print (self.Side + ' is rotating '+ str(90*count - 180*inverse*count) + ' degrees.')
        for x in range(0, 50 * count):
            GPIO.output(self.StepperPort, 0)
            GPIO.output(self.StepperPort, 1)
            sleep(0.02)