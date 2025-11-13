#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher("topic_chat", String, queue_size=10)
    rospy.init_node("pub_node", anonymous=True)

    rate = rospy.Rate(0.5)
    while not rospy.is_shutdown():
        msg = "Hello, time : %s " % rospy.get_time()
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep



if __name__ == "__main__":
    talker()