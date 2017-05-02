# noinspection PyInterpreter
from Side import Side
from time import sleep
from  Motor import Motor
import RPi.GPIO as GPIO
import threading

class RubiksCubeMotor:
    motors = {}
    threads = [None] * 4

    def SetupTurn(self):
        self.threads[0] = threading.Thread(target=self.motors[Side.Left].Rotate, args=(1,))
        self.threads[1] = threading.Thread(target=self.motors[Side.Right].Rotate)
        self.threads[2] = threading.Thread(target=self.motors[Side.Left].Rotate)
        self.threads[3] = threading.Thread(target=self.motors[Side.Right].Rotate, args=(1,))

    def Turn(self, inverse = 0):
        if(inverse == 0):
            self.threads[0].start()
            self.threads[1].start()
        else:
            self.threads[2].start()
            self.threads[3].start()
        self.WaitForActiveThreads()

    def WaitForActiveThreads(self):
        prevCalc = self.ActiveThreads()
        if (prevCalc != 0):
            print('Waiting for threads: %s' % prevCalc)
            calc = -1
            while (calc != 0):
                sleep(0.1)
                calc = self.ActiveThreads()
                if (calc != prevCalc):
                    print('Threads remaining: %s' % str(calc))
                    prevCalc = calc

    # Checking if a thread is still active
    def ActiveThreads(self):
        x = 0
        for t in self.threads:
            if t.isAlive():
                x = x + 1
        return x

    def SetupMotor(self, side, stepperPort, directionPort):
        motor = Motor(str(side), stepperPort, directionPort)
        self.motors[side] = motor

    def R(self, inverse = 0, rotations = 1):
        self.motors[Side.Right].Rotate(inverse, rotations)
        if (rotations % 2 == 1):
            #todo move out Side.LeftRight
            self.motors[Side.Right].Rotate()
            #todo move in Side.LeftRight

    def L(self, inverse = 0, rotations = 1):
        self.motors[Side.Left].Rotate(inverse, rotations)
        if (rotations % 2 == 1):
            #todo move out Side.LeftRight
            self.motors[Side.Left].Rotate()
            #todo move in Side.LeftRight

    def F(self, inverse = 0, rotations = 1):
        self.motors[Side.Front].Rotate(inverse, rotations)
        if (rotations % 2 == 1):
            #todo move out Side.FrontBack
            self.motors[Side.Front].Rotate()
            #todo move in Side.FrontBack

    def B(self, inverse = 0, rotations = 1):
        self.motors[Side.Back].Rotate(inverse, rotations)
        if (rotations % 2 == 1):
            #todo move out Side.FrontBack
            self.motors[Side.Back].Rotate()
            #todo move in Side.FrontBack

    def U(self, inverse = 0, rotations = 1):
        # todo move out Side.FrontBack
        Turn()
        # todo move out Side.FrontBack
        self.motors[Side.Front].Rotate(inverse, rotations)
        # todo move out Side.FrontBack
        Turn(1)
        # todo move out Side.FrontBack

    def D(this, inverse = 0, rotations = 1):
        # todo move out Side.FrontBack
        this.Turn(1)
        # todo move out Side.FrontBack
        this.motors[Side.Front].Rotate(inverse, rotations)
        # todo move out Side.FrontBack
        this.Turn()
        # todo move out Side.FrontBack