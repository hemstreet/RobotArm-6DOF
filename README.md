Robot Arm Controls with Python
==============================

For terminal control
```
$ python 
>>> Import Robot
>>> from Robot import Robot
```

Now in that same python repl we can now access the robot and call module's
methods to control such as:
```
>>> robot.hand.open()
>>> robot.hand.close()
>>> robot.servo.move_servo_to_percent(0,0)
>>> robot.servo.move_servo_to_percent(0,100)
>>> robot.servo.move_servo_to_percent(4, 0)
>>> robot.servo.move_servo_to_percent(4, 100)

```

Snipped from the example.py code in the root package
```
from Robot import Robot
from time import sleep

# invoke a new robot
robot = Robot()

# open the hand
robot.hand.open()

sleep(1)

# close the hand
robot.hand.close()
```