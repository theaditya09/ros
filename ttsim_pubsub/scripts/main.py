#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen

def ser_pen_service(r, g, b, width, off):
    try:
        set_pen = rospy.ServiceProxy("/turtle1/set_pen", SetPen)
        set_pen(r, g, b, width, off)
    except rospy.ServiceException as e:
        rospy.logwarn(e)

def controller_callback(coords : Pose):
    msg = Twist()
    if(coords.x > 9.0 or coords.x < 2 or coords.y > 9.0 or coords.y < 2.0):
        msg.linear.x = 1.0
        msg.angular.z = 1.0
    else:
        msg.linear.x = 5.0
        msg.angular.z = 0.0
    
    pub.publish(msg)

    if(coords.x >= 5.5):
        ser_pen_service(255, 0, 0, 3, 0)
    else:
        ser_pen_service(0, 255, 0, 3, 0)


if __name__ == "__main__":
    rospy.init_node("turtle_controller")
    rospy.wait_for_service("/turtle1/set_pen")
    pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    sub = rospy.Subscriber("/turtle1/pose", Pose, callback=controller_callback)
    rospy.spin()