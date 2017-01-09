from Robot import Robot
from time import sleep

# invoke a new robot
robot = Robot()

# open the hand
robot.hand.open()

sleep(1)

# close the hand
robot.hand.close()
