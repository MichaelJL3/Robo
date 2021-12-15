
from __future__ import annotations
from adafruit_servokit import ServoKit
from time import sleep
from leg.arachne_leg_factory import ArachneLegFactory

kit = ServoKit(channels = 16)

factory = ArachneLegFactory(kit.servo)

nw_leg = factory.build(0, 1, 2, reverse_knee = True)
ne_leg = factory.build(3, 4, 5, reverse_knee = True)
sw_leg = factory.build(6, 7, 8, reverse_knee = True)
se_leg = factory.build(9, 10, 11, reverse_knee = True)

def loop():
    while(True):
        pos = input("Next configuration: ")

        vals = list(map(lambda x: float(x), pos.split(" ")))

        nw_leg.set_angles(vals[0], vals[1], vals[2])

        print(nw_leg.get_angles())

        sleep(0.5)

def init_pos():
    nw_leg.set_angles(0, 0, 0)

init_pos()
loop()
