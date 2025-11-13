#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def cb(msg):
    if(msg.data <= 30):
        rospy.logwarn('[WARNING] BATTERY LEVEL LOW')
    else:
        rospy.loginfo('[INFO] BATTER OK')

if __name__=='__main__':
    rospy.init_node('sub_node')
    rospy.Subscriber('/data', Int32, cb)
    rospy.spin()
