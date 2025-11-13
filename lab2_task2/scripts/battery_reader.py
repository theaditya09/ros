#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32

def read():
    pub = rospy.Publisher("battery_status", Int32, queue_size=10)
    rospy.init_node("battery_status_publisher", anonymous=True)

    rate = rospy.Rate(0.5)
    battery = 100
    while not rospy.is_shutdown():
        battery = battery - random.randint(1,5)
        rospy.loginfo(f"Current Battery : {battery}%")
        pub.publish(battery)
        rate.sleep()


if __name__ == "__main__":
    read()