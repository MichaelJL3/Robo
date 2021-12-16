
from __future__ import annotations
from time import sleep

def set_all_hips(legs, angle: float, delay: float = .3):
    (nw, ne, sw, se) = legs

    nw.set_hip_angle(angle)
    ne.set_hip_angle(angle)
    sw.set_hip_angle(angle)
    se.set_hip_angle(angle)
    sleep(delay)

def set_all_knees(legs, angle: float, delay: float = .3):
    (nw, ne, sw, se) = legs

    nw.set_knee_angle(angle)
    ne.set_knee_angle(angle)
    sw.set_knee_angle(angle)
    se.set_knee_angle(angle)
    sleep(delay)

def set_all_feet(legs, angle: float, delay: float = .3):
    (nw, ne, sw, se) = legs

    nw.set_foot_angle(angle)
    ne.set_foot_angle(angle)
    sw.set_foot_angle(angle)
    se.set_foot_angle(angle)
    sleep(delay)

def awaken(legs):
    set_all_hips(legs, 45)
    set_all_feet(legs, 60)
    set_all_knees(legs, 50)

def sleep(legs):
    set_all_feet(legs, 180)
    set_all_knees(legs, 0)
    set_all_feet(legs, 0)
    set_all_hips(legs, 0)

def step(leg, foot_angle: float, hip_angle: float, delay: float = .3)
    leg.offset_foot_angle(foot_angle)
    leg.offset_hip_angle(hip_angle)
    leg.offest_foot_angle(-foot_angle)
    sleep(delay)

def step(legs):
    (nw, ne, sw, se) = legs

    step(nw, 5, 10)
    step(se, 5, -10)

    nw.offset_hip_angle(-10)
    se.offset_hip_angle(10)
    sleep(.2)

    step(ne, 5, 10)
    step(sw, 5, -10)

    ne.offset_hip_angle(-10)
    sw.offset_hip_angle(10)
    sleep(.2)
