import RPi.GPIO as GPIO
from time import sleep
from Side import Side
from  RubiksCubeMotor import RubiksCubeMotor

#Setup
GPIO.setmode(GPIO.BCM) # choose BCM or BOARD
GPIO.setwarnings(False) # disable warning messages
GPIO.setup(16, GPIO.IN) #button

#Configure Motor pins ( side, stepper, direction )
rubiksCubeMotor = RubiksCubeMotor()
rubiksCubeMotor.SetupMotor(Side.Left, 14, 15)
rubiksCubeMotor.SetupMotor(Side.Right, 23, 24)
rubiksCubeMotor.SetupMotor(Side.Front, 19, 26)
rubiksCubeMotor.SetupMotor(Side.Back, 5, 6)
rubiksCubeMotor.SetupMotor(Side.LeftRight, 17, 27)
rubiksCubeMotor.SetupMotor(Side.FrontBack, 20, 21)
rubiksCubeMotor.SetupTurn()

print('waiting for start signal..')
while True:
	if (GPIO.input(16) == True):
		break
	sleep(0.05)

print('-------- MOVE ---------')
rubiksCubeMotor.D()

sleep(0.1)
print('exit')