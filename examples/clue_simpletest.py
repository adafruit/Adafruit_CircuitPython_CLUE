# SPDX-FileCopyrightText: 2019 Kattni Rembor, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT
from adafruit_clue import clue

clue.sea_level_pressure = 1020

while True:
    print("Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(*clue.acceleration))
    print("Gyro: {:.2f} {:.2f} {:.2f} dps".format(*clue.gyro))
    print("Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*clue.magnetic))
    print(f"Pressure: {clue.pressure:.3f} hPa")
    print(f"Altitude: {clue.altitude:.1f} m")
    print(f"Temperature: {clue.temperature:.1f} C")
    print(f"Humidity: {clue.humidity:.1f} %")
    print(f"Proximity: {clue.proximity}")
    print(f"Gesture: {clue.gesture}")
    print("Color: R: {} G: {} B: {} C: {}".format(*clue.color))
    print("--------------------------------")
