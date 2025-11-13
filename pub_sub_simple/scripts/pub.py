#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

if __name__=='__main__':
    rospy.init_node('pub_node')
    pub = rospy.Publisher('/data', Int32, queue_size=10)
    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        battery = random.randint(0,100)
        rospy.loginfo("Publishing battery level: %d" % battery)
        pub.publish(battery)
        rate.sleep()
        