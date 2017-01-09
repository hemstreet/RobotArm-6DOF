Robot Arm Controls with Python
==============================
Raspberry Pi host using (PCA9685)[https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf] as an I2C 16 bit PWM driver to control the robot arm's (Tower MG996R)[http://www.electronicoscaldas.com/datasheet/MG996R_Tower-Pro.pdf] Servos
In order to get this working, you may need to customize the limits / bounds for each servo so it will be tuned to your application

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