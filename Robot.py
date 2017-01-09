from components import Report, Servo, Hand


class Robot:
    def __init__(self):
        report = Report()
        self.servo = Servo(report)

        config = {
            'report': report,
            'servo': self.servo,
        }

        self.hand = Hand(config)
