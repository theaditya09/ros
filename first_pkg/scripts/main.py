#!/usr/bin/env python3
import rospy

if __name__=='__main__':
    rospy.init_node('myFirstNode')
    rospy.loginfo("[INFO] this is an info")
    rospy.logwarn("[WARNING] this is a warning")
    rospy.logerr("[ERROR] this is an error")
        