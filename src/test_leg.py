
from __future__ import annotations
from gpiozero import Servo
from time import sleep

hip_pin = 17
knee_pin = 27
foot_pin = 22

class Joint(object):
    @property
    def angle(self):
        pass

    @angle.setter
    def angle(self, angle: float):
        pass

class LegBuilder(object):
    def hip(self, hip: Joint) -> LegBuilder:
        self.hip = hip
        return self

    def knee(self, knee: Joint) -> LegBuilder:
        self.knee = knee
        return self

    def foot(self, foot: Joint) -> LegBuilder:
        self.foot = foot
        return self

    def build(self) -> Leg:
        return Leg(self.hip, self.knee, self.foot)

class Leg(object):
    def __init__(self, hip: Joint, knee: Joint, foot: Joint) -> Leg:
        self.hip = hip
        self.knee = knee
        self.foot = foot

    def set_hip_angle(self, angle: float) -> Leg:
        self.hip.angle = angle
        return self

    def set_knee_angle(self, angle: float) -> Leg:
        self.knee.angle = angle
        return self

    def set_foot_angle(self, angle: float) -> Leg:
        self.foot.angle = angle
        return self

    def set_angles(self, hip_angle: float, knee_angle: float, foot_angle: float) -> Leg:
        return self.set_hip_angle(hip_angle) \
            .set_knee_angle(knee_angle) \
            .set_foot_angle(foot_angle)

    def get_angles(self):
        return (self.hip.angle, self.knee.angle, self.foot.angle)

class ServoJoint(Joint):
    def __init__(self, servo: Servo):
        self.servo = servo

    @property
    def angle(self):
        return self.servo.value

    @angle.setter
    def angle(self, angle: float):
        self.servo.value = angle

class Knee(ServoJoint):
    pass

class Foot(ServoJoint):
    pass

class Hip(ServoJoint):
    pass

hip = Hip(Servo(hip_pin))
knee = Knee(Servo(knee_pin))
foot = Foot(Servo(foot_pin))

leg = LegBuilder() \
    .hip(hip) \
    .knee(knee) \
    .foot(foot) \
    .build()

while(True):
    pos = input("Next configuration: ")

    vals = list(map(lambda x: float(x), pos.split(" ")))

    leg.set_angles(vals[0], vals[1], vals[2])
    
    print(leg.get_angles())

    sleep(0.5)

