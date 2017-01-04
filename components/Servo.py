import RPi.GPIO as GPIO


class Servo:
    def __init__(self, config):
        print("Initializing Servo")
        self.initialize_board()

        pins = [11, 12, 13, 15, 16, 18]
        self.initialize_pin_setup(pins)

    @staticmethod
    def initialize_board(self):
        GPIO.setmode(GPIO.BOARD)

    @staticmethod
    def initialize_pin_setup(self, pins):
        for pin in pins:
            GPIO.setup(pin, GPIO.OUT)
            p = GPIO.PWM(pin, 0.5)


        p.start(1)

    def to_position(self, servo, amount):
        pass
