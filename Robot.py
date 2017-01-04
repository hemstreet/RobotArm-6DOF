from lib.Hand import Hand
from lib.Servo import Servo
from lib.Report import Report


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

