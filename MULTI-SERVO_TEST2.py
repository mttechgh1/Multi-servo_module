# install PCA9865 driver - sudo pip3 install adafruit-circuitpython-servokit
# refrences  -"techspassion", "FREEDOM TECH" - on Youtube
#In config, "I2C" needs to be set ON
from adafruit_servokit import ServoKit
from time import sleep
kit=ServoKit(channels=16) #toal channels used
#input command for angles
kit.servo[0].angle=0
print("SERVO 0 = 0")
sleep(2)
kit.servo[0].angle=180
print("SERVO 0 = 180")
kit.continuous_servo[1].throttle=0
print("SERVO 1 = 0")
sleep(2)
kit.continuous_servo[1].throttle=1
print("servo 1 = +1")
sleep(2)
kit.continuous_servo[1].throttle=-1
print("SERVO 1 = -1")
sleep(2)
print("DONE")
