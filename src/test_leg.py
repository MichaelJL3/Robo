
from __future__ import annotations
from adafruit_servokit import ServoKit
from time import sleep
from leg.arachne_leg_factory import ArachneLegFactory

import brain.moves

kit = ServoKit(channels = 16)

factory = ArachneLegFactory(kit.servo)

nw_leg = factory.build(0,  1,  2,  reverse_foot = True)
ne_leg = factory.build(4,  5,  6,  reverse_knee = True, reverse_hip = True)
sw_leg = factory.build(8,  9,  10, reverse_knee = True, reverse_hip = True)
se_leg = factory.build(12, 13, 14, reverse_foot = True)

legs = [nw_leg, ne_leg, sw_leg, se_leg]

def loop():
    while(True):
        pos = input("Next configuration: ")

        vals = list(map(lambda x: float(x), pos.split(" ")))

        for leg in legs:
            leg.set_hip_angle(vals[0])
            sleep(0.3)

        for leg in legs:
            leg.set_knee_angle(vals[1])
            sleep(0.3)

        for leg in legs:
            leg.set_foot_angle(vals[2])
            sleep(0.3)
            print(leg.get_angles())

def init_pos(leg):
    leg.set_angles(0, 0, 0)

def test_small_move_big_delay():
    for x in range(0, 175, 5):
        for leg in legs:
            leg.offset_hip_angle(5)
            leg.offset_knee_angle(5)
            leg.offset_foot_angle(5)
            sleep(.5)

def reset_legs_slow():
    for leg in legs:
        leg.set_knee_angle(0)
        sleep(1)
        leg.set_foot_angle(0)
        sleep(1)

def sit():
    legs[0].set_knee_angle(60)
    legs[1].set_knee_angle(30)
    legs[2].set_knee_angle(60)
    legs[3].set_knee_angle(30)
    sleep(.5)

    legs[0].set_foot_angle(180)
    legs[2].set_foot_angle(180)

def stand():
    sleep(1)

    for leg in legs:
        leg.set_hip_angle(45)
        sleep(.3)
    
    for leg in legs:
        leg.set_foot_angle(180)
        sleep(.3)

    legs[0].set_knee_angle(90)
    legs[1].set_knee_angle(70)
    legs[2].set_knee_angle(90)
    legs[3].set_knee_angle(70)

    sleep(.3)

def extend_leg():
    legs[1].set_hip_angle(25)
    legs[1].offset_foot_angle(-40)
    sleep(.3)
    legs[1].offset_knee_angle(30)

#test_small_move_big_delay()
#reset_legs_slow()

#init_pos()
#loop()

#stand()
#sleep(1)
#extend_leg()
#sleep(1)
sit()

#brain.moves.awaken(legs)
#sleep(2)
#brain.moves.disable(legs)
