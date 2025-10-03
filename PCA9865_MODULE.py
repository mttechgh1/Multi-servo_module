# install PCA9865 driver - sudo pip3 install adafruit-circuitpython-servokit
# refrences  -"techspassion", "FREEDOM TECH" - on Youtube
#In config, "I2C" needs to be set ON
from adafruit_servokit import ServoKit
from time import sleep
kit=ServoKit(channels=16)
servo=14 # toal channels used
# # new code
# import time
kit.servo[0].angle=180
kit.continuous_servo[1].throttle=1
time.sleep(1)
kit.continuous_servo[1].throttle=-1
time.sleep(1)
kit.servo[0].angle=0
kit.continuous_servo[1].throttle=0
  

  
