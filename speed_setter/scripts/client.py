#!/usr/bin/env python3

import rospy
from speed_setter.srv import SetSpeed

if __name__ == '__main__':
    rospy.init_node('client')
    rospy.wait_for_service('set_speed')
    service = rospy.ServiceProxy('set_speed', SetSpeed)

    rate = rospy.Rate(0.33)

    while not rospy.is_shutdown():
        linear = float(input("Enter linear speed : "))
        angular = float(input("Enter angular speed : "))
        response = service(linear, angular)
        rospy.loginfo(f"[INFO] Response : {response}")
        rate.sleep
