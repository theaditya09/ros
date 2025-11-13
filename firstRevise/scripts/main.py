#!/usr/bin/env python3

import rospy

if __name__ == "__main__":
    rospy.init_node("MyNode")
    rospy.loginfo("The node has been started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello World!")
        rospy.sleep(0.1)