"""Monitor customisable temperature and humidity ranges, with an optional alarm."""
from adafruit_clue import clue

# Set desired temperature range in degrees Celsius.
min_temp = 24
max_temp = 30

# Set desired humidity range in percent.
min_humidity = 20
max_humidity = 65

# Set to true to enable alarm warning.
alarm = False

data = clue.simple_text_display(text_scale=3, colors=((255, 255, 255),))

data[0].text = "Temperature &"
data[1].text = "Humidity"
while True:
    alarm = False
    temperature = clue.temperature
    humidity = clue.humidity
    data[3].text = "Temp: {:.1f} C".format(temperature)
    data[5].text = "Humi: {:.1f} %".format(humidity)
    if temperature < min_temp:
        data[3].color = (0, 0, 255)
        alarm = True
    elif temperature > max_temp:
        data[3].color = (255, 0, 0)
        alarm = True
    else:
        data[3].color = (255, 255, 255)

    if humidity < min_humidity:
        data[5].color = (0, 0, 255)
        alarm = True
    elif humidity > max_humidity:
        data[5].color = (255, 0, 0)
        alarm = True
    else:
        data[5].color = (255, 255, 255)
    data.show()

    if alarm:
        clue.start_tone(2000)
    else:
        clue.stop_tone()
