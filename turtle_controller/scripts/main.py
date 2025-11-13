#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def pose_callback(msg : Pose):
    cmd = Twist()

    if msg.x > 9.0 or msg.x < 2 or msg.y > 9.0 or msg.y < 2:
        cmd.linear.x = 1.0
        cmd.angular.z = 0.8
    else:
        cmd.linear.x = 24.0
    
    # if msg.y > 9.0 or msg.y < 2 :
    #     cmd.linear.y = 1.0
    #     cmd.angular.z = 1.72
    # else:
    #     cmd.linear.y = 3.0

    pub.publish(cmd)

    

if __name__=='__main__':
    rospy.init_node('turtle_controller')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.spin()