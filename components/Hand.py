class Hand:
    def __init__(self, options):
        self.report = options['report']
        self.servo = options['servo']

        self.channels = {
            'claw': 5,
            'wrist': 4
        }

    def open(self):
        self.report.log("HAND::Open")
        self.servo.move_servo_to_percent(self.channels['claw'], 60)

    def close(self):
        self.report.log("HAND::Close")
        self.servo.move_servo_to_percent(self.channels['claw'], 95)

    def rotate(self, percent):
        self.report.log("HAND::Rotate to {0} percent".format(percent))
        self.servo.move_servo_to_percent(self.channels['wrist'], percent)

    def position(self, value):
        self.report.log("HAND::Position")

