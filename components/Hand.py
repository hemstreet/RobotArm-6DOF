class Hand:
    def __init__(self, options):

        self.report = options['report']
        self.servo = options['servo']

        self.channels = {
            'hand': 5,
            'wrist': {
                'rotate': 4,
                'flex': 3
            }
        }

    def open(self):
        """Open the end effectors"""
        self.report.log("HAND::Open")
        self.servo.move_servo_to_percent(self.channels['hand'], 60)

    def close(self):
        """Close the end effectors"""
        self.report.log("HAND::Close")
        self.servo.move_servo_to_percent(self.channels['hand'], 95)

    def grip(self, percent):
        """close the end effectors to a specific position to grip onto something"""
        int(((percent / 100.0) * (self.servo_max - self.servo_min)) + self.servo_min)
        self.report.log("HAND::Wrist_Rotate to {0} percent".format(percent))
        self.servo.move_servo_to_percent(self.channels['hand'], percent)

    def rotate(self, percent):
        """Pronation and Supination of the wrist"""
        self.report.log("HAND::Wrist_Rotate to {0} percent".format(percent))
        self.servo.move_servo_to_percent(self.channels['wrist']['rotate'], percent)

    def flex(self, percent):
        """Flexion and extension of the wrist"""
        self.report.log("HAND::Wrist_Flex to {0} percent".format(percent))
        self.servo.move_servo_to_percent(self.channels['wrist']['flex'], percent)
