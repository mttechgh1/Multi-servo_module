# install PCA9865 driver - sudo pip3 install adafruit-circuitpython-servokit
from adafruit_servokit import ServoKit
froom time import sleep
kit=ServoKit(channels=16)
servo=14 # toal channels used
#input command for angles
while true:
  a=input("enter - ")
  kit.servo[12].angle=int(a)
  
  
