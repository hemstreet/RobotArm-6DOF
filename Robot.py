from components.Hand import Hand
from components.Servo import Servo
from components.Report import Report


class Robot:
    def __init__(self):
        print("Initializing Robot")

        config = {
            'report': Report()
        }

        servo = Servo(config)
        hand = Hand(config)

        hand.close()
        hand.open()

        hand.position(12)

