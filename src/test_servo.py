
from gpiozero import Servo
from time import sleep

aPin = 18
bPin = 27
cPin = 22

servoA = Servo(aPin)
servoB = Servo(bPin)
servoC = Servo(cPin)

servoA.value = 1
servoB.value = 1
servoC.value = 1
sleep(.5)

