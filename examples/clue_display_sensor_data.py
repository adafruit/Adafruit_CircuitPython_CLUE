# SPDX-FileCopyrightText: 2019 Kattni Rembor, written for Adafruit Industries
#
# SPDX-License-Identifier: MIT
from adafruit_clue import clue

clue.sea_level_pressure = 1020

clue_data = clue.simple_text_display(title="CLUE Sensor Data!", title_scale=2)

while True:
    clue_data[0].text = "Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(*clue.acceleration)
    clue_data[1].text = "Gyro: {:.2f} {:.2f} {:.2f} dps".format(*clue.gyro)
    clue_data[2].text = "Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*clue.magnetic)
    clue_data[3].text = f"Pressure: {clue.pressure:.3f} hPa"
    clue_data[4].text = f"Altitude: {clue.altitude:.1f} m"
    clue_data[5].text = f"Temperature: {clue.temperature:.1f} C"
    clue_data[6].text = f"Humidity: {clue.humidity:.1f} %"
    clue_data[7].text = f"Proximity: {clue.proximity}"
    clue_data[8].text = f"Gesture: {clue.gesture}"
    clue_data[9].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
    clue_data[10].text = f"Button A: {clue.button_a}"
    clue_data[11].text = f"Button B: {clue.button_b}"
    clue_data[12].text = f"Touch 0: {clue.touch_0}"
    clue_data[13].text = f"Touch 1: {clue.touch_1}"
    clue_data[14].text = f"Touch 2: {clue.touch_2}"
    clue_data.show()
