
from adafruit_servokit import ServoKit
from time import sleep

kit = ServoKit(channels=16)

kit.servo[0].angle = 180
kit.servo[1].angle = 180
kit.servo[2].angle = 180

sleep(0.5)

