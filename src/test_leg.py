
from __future__ import annotations
from adafruit_servokit import ServoKit
from time import sleep
from leg.servo_joint import ServoJoint
from leg.arachne_leg import ArachneLegBuilder

hip_pin = 0
knee_pin = 1
foot_pin = 2

kit = ServoKit(channels = 16)

leg = ArachneLegBuilder() \
    .hip(ServoJoint(kit.servo[hip_pin])) \
    .knee(ServoJoint(kit.servo[knee_pin])) \
    .foot(ServoJoint(kit.servo[foot_pin])) \
    .build()

def loop():
    while(True):
        pos = input("Next configuration: ")

        vals = list(map(lambda x: float(x), pos.split(" ")))

        leg.set_angles(vals[0], converter(vals[1]), vals[2])

        print(leg.get_angles())

        sleep(0.5)

def init_pos():
    leg.set_angles(0, 100, 20)

def converter(a):
    return 180 - a

loop()
