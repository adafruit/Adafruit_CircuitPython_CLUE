import time
import array
import math
import board
import busio
import digitalio
import audiobusio  # possibly audiocore or whatever
import neopixel
import adafruit_bmp280
import adafruit_sht31d
import adafruit_apds9960.apds9960
import adafruit_lis3mdl
import adafruit_lsm6ds
import gamepad

class Clue:
    def __init__(self):
        # Define I2C:
        self._i2c = board.I2C()

        # Define buttons:
        self._a = digitalio.DigitalInOut(board.BUTTON_A)
        self._a.switch_to_input(pull=digitalio.Pull.DOWN)
        self._b = digitalio.DigitalInOut(board.BUTTON_B)
        self._b.switch_to_input(pull=digitalio.Pull.DOWN)

        # Define LEDs:
        self._white_leds = digitalio.DigitalInOut(board.WHITE_LEDS)
        self._white_leds.switch_to_output()
        self._pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
        self._red_led = digitalio.DigitalInOut(board.L)
        self._red_led.switch_to_output()

        # Define audio:
        self._mic = audiobusio.PDMIn(board.MICROPHONE_CLOCK, board.MICROPHONE_DATA,
                                     sample_rate=16000, bit_depth=16)
        self._speaker = digitalio.DigitalInOut(board.SPEAKER)
        self._speaker.switch_to_output()
        self._sample = None
        self._samples = None
        self._sine_wave = None
        self._sine_wave_sample = None

        # Define sensors:
        # Accelerometer/gyroscope:
        self._accelerometer = adafruit_lsm6ds.LSM6DS33(self._i2c)

        # Magnetometer:
        self._magnetometer = adafruit_lis3mdl.LIS3MDL(self._i2c)

        # DGesture/proximity/color/light sensor:
        self._sensor = adafruit_apds9960.apds9960.APDS9960(self._i2c)

        # Humidity sensor:
        self._humidity = adafruit_sht31d.SHT31D(self._i2c)

        # Barometric pressure sensor:
        self._pressure = adafruit_bmp280.Adafruit_BMP280_I2C(self._i2c)

    @property
    def button_a(self):
        """``True`` when Button A is pressed. ``False`` if not.

        To use with the CLUE:
        """
        return self._a.value

    @property
    def button_b(self):
        """``True`` when Button B is pressed. ``False`` if not.

        To use with the CLUE:
        """
        return self._b.value

    @property
    def were_pressed(self):
        """Returns a set of the buttons that have been pressed.

        .. image :: ../docs/_static/button_b.jpg
          :alt: Button B

        To use with the CLUE:

        .. code-block:: python

          import

          while True:
              print(.were_pressed)
        """
        ret = set()
        pressed = self.gamepad.get_pressed()
        for button, mask in (('A', 0x01), ('B', 0x02)):
            if mask & pressed:
                ret.add(button)
        return ret

    @property
    def acceleration(self):
        """Obtain acceleration data from the x, y and z axes.

        This example prints the values. Try moving the board to see how the printed values change.

        To use with the CLUE:


        """
        return self._accelerometer.acceleration

    @property
    def gyro(self):
        """Obtain x, y, z angular velocity values in degrees/second.

        This example prints the values. Try moving the board to see how the printed values change.

        To use with the CLUE:

        """
        return self._accelerometer.gyro

    @property
    def magnetic(self):
        """Obtain x, y, z magnetic values in microteslas.

        This example prints the values. Try moving the board to see how the printed values change.

        To use with the CLUE:

        """
        return self._magnetometer.magnetic

    @property
    def proximity(self):
        """A relative proximity to the sensor in values from 0 - 255.

        This example prints the value. Try moving your hand towards and away from the front of the
        board to see how the printed values change.

        To use with the CLUE:

        """
        self._sensor.enable_proximity = True
        return self._sensor.proximity()

    @property
    def color(self):
        """The red, green blue and clear light values. (r, g, b, c)"""
        self._sensor.enable_color = True
        return self._sensor.color_data

    @property
    def gesture(self):
        """gesture code if detected. =0 if no gesture detected
        =1 if an UP, =2 if a DOWN, =3 if an LEFT, =4 if a RIGHT"""
        self._sensor.enable_gesture = True
        return self._sensor.gesture()

    @property
    def humidity(self):
        """The measured relative humidity in percent."""
        return self._humidity.relative_humidity

    @property
    def pressure(self):
        """The barometric pressure in hectoPascals."""
        return self._pressure.pressure

    @property
    def temperature(self):
        """The temperature in degrees Celsius."""
        return self._pressure.temperature

    @property
    def altitude(self):
        """The altitude in meters based on the sea level pressure at your location. You must set
        ``sea_level_pressure`` to receive an accurate reading."""
        return self._pressure.altitude

    @property
    def sea_level_pressure(self):
        """Set to the pressure at sea level at your location, before reading altitude for
        the most accurate altitude measurement.
        """
        return self._pressure.sea_level_pressure

    @sea_level_pressure.setter
    def sea_level_pressure(self, value):
        self._pressure.sea_level_pressure = value

    @property
    def red_led(self):
        """The red led next to the USB plug labeled LED.
        """
        return self._red_led.value

    @red_led.setter
    def red_led(self, value):
        self._red_led.value = value

    @property
    def pixel(self):
        return self._pixel

    @staticmethod
    def _sine_sample(length):
        tone_volume = (2 ** 15) - 1
        shift = 2 ** 15
        for i in range(length):
            yield int(tone_volume * math.sin(2*math.pi*(i / length)) + shift)

    def _generate_sample(self, length=100):
        if self._sample is not None:
            return
        self._sine_wave = array.array("H", self._sine_sample(length))
        self._sample = self.audiopwmio.PWMAudioOut(board.SPEAKER)
        self._sine_wave_sample = audiocore.RawSample(self._sine_wave)

    def play_tone(self, frequency, duration):
        """ Produce a tone using the speaker. Try changing frequency to change
        the pitch of the tone.

        :param int frequency: The frequency of the tone in Hz
        :param float duration: The duration of the tone in seconds

        To use with the CLUE:

        .. code-block:: python

            import

            .play_tone(440, 1)
        """
        # Play a tone of the specified frequency (hz).
        self.start_tone(frequency)
        time.sleep(duration)
        self.stop_tone()

    def start_tone(self, frequency):
        """ Produce a tone using the speaker. Try changing frequency to change
        the pitch of the tone.

        :param int frequency: The frequency of the tone in Hz

        To use with the CLUE:

        .. code-block:: python

             import

             while True:
                 if .button_a:
                     .start_tone(262)
                 elif .button_b:
                     .start_tone(294)
                 else:
                     .stop_tone()
        """
        self._speaker_enable.value = True
        length = 100
        if length * frequency > 350000:
            length = 350000 // frequency
        self._generate_sample(length)
        # Start playing a tone of the specified frequency (hz).
        self._sine_wave_sample.sample_rate = int(len(self._sine_wave) * frequency)
        if not self._sample.playing:
            self._sample.play(self._sine_wave_sample, loop=True)

    def stop_tone(self):
        """ Use with start_tone to stop the tone produced.

        To use with the CLUE:

        .. code-block:: python

             import

             while True:
                 if .button_a:
                     .start_tone(262)
                 elif .button_b:
                     .start_tone(294)
                 else:
                     .stop_tone()
        """
        # Stop playing any tones.
        if self._sample is not None and self._sample.playing:
            self._sample.stop()
            self._sample.deinit()
            self._sample = None
        self._speaker_enable.value = False

    @staticmethod
    def _normalized_rms(values):
        mean_values = int(sum(values) / len(values))
        return math.sqrt(sum(float(sample - mean_values) * (sample - mean_values)
                             for sample in values) / len(values))

    @property
    def sound_level(self):
        """Obtain the sound level from the microphone (sound sensor).

        This example prints the sound levels. Try clapping or blowing on
        the microphone to see the levels change.

        .. code-block:: python

          import

          while True:
              print(.sound_level)
        """
        if self._sample is None:
            self._samples = array.array('H', [0] * 160)
        self._mic.record(self._samples, len(self._samples))
        return self._normalized_rms(self._samples)

    def loud_sound(self, sound_threshold=200):
        """Utilise a loud sound as an input.

        :param int sound_threshold: Threshold sound level must exceed to return true (Default: 200)

        .. image :: ../docs/_static/microphone.jpg
          :alt: Microphone (sound sensor)

        This example turns the NeoPixel LED blue each time you make a loud sound.
        Try clapping or blowing onto the microphone to trigger it.

        .. code-block:: python

          import

          while True:
              if .loud_sound():
                  .pixel.fill((0, 50, 0))
              else:
                  .pixel.fill(0)

        You may find that the code is not responding how you would like.
        If this is the case, you can change the loud sound threshold to
        make it more or less responsive. Setting it to a higher number
        means it will take a louder sound to trigger. Setting it to a
        lower number will take a quieter sound to trigger. The following
        example shows the threshold being set to a higher number than
        the default.

        .. code-block:: python

          import

          while True:
              if .loud_sound(sound_threshold=300):
                  .pixel.fill((0, 50, 0))
              else:
                  .pixel.fill(0)
        """

        return self.sound_level > sound_threshold

clue = Clue()
"""Object that is automatically created on import.

   To use, simply import it from the module:

   .. code-block:: python

     from adafruit_clue.Clue import clue
"""