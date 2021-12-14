
import smbus
import time
import math

bus = smbus.SMBus(1)

bus_addr = 0x1D

bus.write_byte_data(bus_addr, 0x2A, 0x00)
bus.write_byte_data(bus_addr, 0x2A, 0x01)
bus.write_byte_data(bus_addr, 0x0E, 0x00)

time.sleep(0.5)

def convert(block_a, block_b):
    delta = (block_a * 256 + block_b) / 16 
    return delta if delta <= 2047 else delta - 4096

def dist(a, b):
    return math.sqrt((a*a) + (b*b))

def rotation(x, y, z):
    radians_x = math.atan2(x, dist(y, z))
    radians_y = math.atan2(y, dist(x, z))
    degrees_x = math.degrees(radians_x)
    degrees_y = math.degrees(radians_y)

    return (-degrees_x, degrees_y)

while True:
    data = bus.read_i2c_block_data(bus_addr, 0x00, 7)

    xAccl = convert(data[1], data[2])
    yAccl = convert(data[3], data[4])
    zAccl = convert(data[5], data[6])

    rotations = rotation(xAccl, yAccl, zAccl)

    print(data)
    print(xAccl, yAccl, zAccl)
    print(rotations)

    time.sleep(0.5)

