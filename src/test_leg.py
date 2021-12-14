
from __future__ import annotations
from time import sleep
from leg.servo_joint import ServoJoint
from leg.arachne_leg import ArachneLegBuilder

hip_pin = 17
knee_pin = 27
foot_pin = 22

leg = ArachneLegBuilder() \
    .hip(ServoJoint(hip_pin)) \
    .knee(ServoJoint(knee_pin)) \
    .foot(ServoJoint(foot_pin)) \
    .build()

while(True):
    pos = input("Next configuration: ")

    vals = list(map(lambda x: float(x), pos.split(" ")))

    leg.set_angles(vals[0], vals[1], vals[2])
    
    print(leg.get_angles())

    sleep(0.5)
