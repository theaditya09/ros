#!/usr/bin/env python3

import rospy
from speed_setter.srv import SetSpeed, SetSpeedResponse

def cb(req):
    return SetSpeedResponse(True, f"Linear speed set as : {req.linear}, Angular speed set as : {req.angular}")

if __name__=='__main__':
    rospy.init_node('set_speed_server')
    service = rospy.Service('set_speed', SetSpeed, cb)
    rospy.spin()


