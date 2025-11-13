#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("I heard %s", data.data)

def listener():
    rospy.init_node("sub_node", anonymous=True)
    rospy.Subscriber("topic_chat", String, callback)
    rospy.spin()

if __name__ == "__main__":
    listener()