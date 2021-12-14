
import board
from adafruit_mma8451 import MMA8451

bus_address = 0x1d

i2c = board.I2C()
sensor = MMA8451(i2c, address=0x1d)

x, y, z = sensor.acceleration
orientation = sensor.orientation

print(x, y, z)
print(orientation)

