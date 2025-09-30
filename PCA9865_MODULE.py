# install PCA9865 driver - sudo pip3 install adafruit-circuitpython-servokit
# refrences  -"techspassion", "FREEDOM TECH" - on Youtube
#In config, "I2C" needs to be set ON
from adafruit_servokit import ServoKit
from time import sleep
kit=ServoKit(channels=16)
servo=14 # toal channels used
#input command for angles
while true:
  a=input("enter - ")
  kit.servo[12].angle=int(a)
  
  
