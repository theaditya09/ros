#!/usr/bin/env python3
import rospy
import random 
from std_msgs.msg import Float32

def callback(distance):
    if distance.data <= 25.00:
        rospy.logwarn(f"[WARNING] Distance is really close : {distance.data} cm")
    else:
        rospy.loginfo(f"OK: Distance is {distance.data} cm")

def screen():
    rospy.init_node("mobile")
    rospy.Subscriber("getData", Float32, callback)
    rospy.spin()

if __name__ == "__main__":
    screen()