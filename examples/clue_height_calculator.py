"""Calculate the height of an object. Press button A to reset initial height and then lift the
CLUE to find the height."""
from adafruit_clue import clue

# Set to the sea level pressure in hPa at your location for the most accurate altitude measurement.
clue.sea_level_pressure = 1015

clue_data = clue.simple_text_display(text_scale=2, colors=((0, 255, 255), 0, (255, 0, 0),
                                                           (255, 0, 0), 0, (255, 255, 0), 0,
                                                           (0, 255, 0)))

initial_height = clue.altitude

clue_data[0].text = "Calculate height!"
clue_data[2].text = "Press A to reset"
clue_data[3].text = "initial height!"
while True:
    if clue.button_a:
        initial_height = clue.altitude
        clue.pixel.fill((255, 0, 0))
    else:
        clue.pixel.fill(0)
    clue_data[5].text = "Altitude: {:.1f} m".format(clue.altitude)
    clue_data[7].text = "Height: {:.1f} m".format(clue.altitude - initial_height)
    clue_data.show()
