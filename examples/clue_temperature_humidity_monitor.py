"""Monitor customisable temperature and humidity ranges, with an optional alarm."""
from adafruit_clue import clue

# Set desired temperature range in degrees Celsius.
min_temp = 24
max_temp = 30

# Set desired humidity range in percent.
min_humidity = 20
max_humidity = 65

# Set to true to enable alarm warning.
alarm_enable = False

data = clue.simple_text_display(text_scale=3, colors=(clue.WHITE,))

data[0].text = "Temperature &"
data[1].text = "Humidity"
while True:
    alarm = False
    temperature = clue.temperature
    humidity = clue.humidity
    data[3].text = "Temp: {:.1f} C".format(temperature)
    data[5].text = "Humi: {:.1f} %".format(humidity)
    if temperature < min_temp:
        data[3].color = clue.BLUE
        alarm = True
    elif temperature > max_temp:
        data[3].color = clue.RED
        alarm = True
    else:
        data[3].color = clue.WHITE

    if humidity < min_humidity:
        data[5].color = clue.BLUE
        alarm = True
    elif humidity > max_humidity:
        data[5].color = clue.RED
        alarm = True
    else:
        data[5].color = clue.WHITE
    data.show()

    if alarm and alarm_enable:
        clue.start_tone(2000)
    else:
        clue.stop_tone()
