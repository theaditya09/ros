#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
import random

def push():
    pub = rospy.Publisher("getData", Float32, queue_size=10)
    rospy.init_node("sensor", anonymous=True)

    rate = rospy.Rate(0.33)
    while not rospy.is_shutdown():
        num = random.uniform(5.00, 50.00)
        rospy.loginfo(f"Distance : {num} cm")
        pub.publish(num)
        rate.sleep()


if __name__ == "__main__":
    push()