import Adafruit_PCA9685


class Servo:
    def __init__(self, report):
        self.report = report
        self.pwm = Adafruit_PCA9685.PCA9685()

        self.servo_min = 150  # Min pulse length out of 4096
        self.servo_max = 600  # Max pulse length out of 4096

        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)

    def move_servo(self, channel, amount):
        if amount > self.servo_max or amount < self.servo_min:
            print('Out of servo range, \
                  try entering a number from {0} to {1}, you entered \
                  {2}'.format(self.servo_min, self.servo_max, amount))
            return

        self.pwm.set_pwm(channel, 0, amount)

    def move_servo_to_percent(self, channel, percent):

        value = int(((percent / 100.0) * (self.servo_max - self.servo_min)) + self.servo_min)

        self.report.log("SERVO::Move channel {0} to {1} percent. Value of {2}".format(channel, percent, value))

        self.move_servo(channel, value)

