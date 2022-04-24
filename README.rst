Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-clue/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/clue/en/latest/
    :alt: Documentation Status

.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_CLUE/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_CLUE/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

A high level library representing all the features of the Adafruit CLUE


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_
* `Adafruit LSM6DS <https://github.com/adafruit/Adafruit_CircuitPython_LSM6DS>`_
* `Adafruit LIS3MDL <https://github.com/adafruit/Adafruit_CircuitPython_LIS3MDL>`_
* `Adafruit APDS9960 <https://github.com/adafruit/Adafruit_CircuitPython_APDS9960>`_
* `Adafruit BMP280 <https://github.com/adafruit/Adafruit_CircuitPython_BMP280>`_
* `Adafruit SHT31D <https://github.com/adafruit/Adafruit_CircuitPython_SHT31D>`_
* `Adafruit NeoPixel <https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel>`_
* `Adafruit Display Text <https://github.com/adafruit/Adafruit_CircuitPython_Display_Text>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Demos may require libraries not listed here.

Usage Example
=============
This example displays sensor and input data on the CLUE display.

.. code-block:: python

    from adafruit_clue import clue

    clue.sea_level_pressure = 1020

    clue_data = clue.simple_text_display(title="CLUE Sensor Data!", title_scale=2, num_lines=15)

    while True:
        clue_data[0].text = "Acceleration: {:.2f} {:.2f} {:.2f}".format(*clue.acceleration)
        clue_data[1].text = "Gyro: {:.2f} {:.2f} {:.2f}".format(*clue.gyro)
        clue_data[2].text = "Magnetic: {:.3f} {:.3f} {:.3f}".format(*clue.magnetic)
        clue_data[3].text = "Pressure: {:.3f}hPa".format(clue.pressure)
        clue_data[4].text = "Altitude: {:.1f}m".format(clue.altitude)
        clue_data[5].text = "Temperature: {:.1f}C".format(clue.temperature)
        clue_data[6].text = "Humidity: {:.1f}%".format(clue.humidity)
        clue_data[7].text = "Proximity: {}".format(clue.proximity)
        clue_data[8].text = "Gesture: {}".format(clue.gesture)
        clue_data[9].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
        clue_data[10].text = "Button A: {}".format(clue.button_a)
        clue_data[11].text = "Button B: {}".format(clue.button_b)
        clue_data[12].text = "Touch 0: {}".format(clue.touch_0)
        clue_data[13].text = "Touch 1: {}".format(clue.touch_1)
        clue_data[14].text = "Touch 2: {}".format(clue.touch_2)
        clue_data.show()


Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/clue/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_CLUE/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
