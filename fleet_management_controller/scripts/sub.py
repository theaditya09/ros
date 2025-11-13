#!/usr/bin/env python3
import rospy
from fleet_management_controller.msg import DroneTelemetry

def callback(msg):
    drone = msg
    rospy.loginfo(f"[INFO] RECEIVED DATA : \n drone_id : {drone.drone_id} \n position : {drone.position} \n battery_level : {drone.battery_level} \n is_emergency : {drone.is_emergency}")

    if(drone.battery_level <= 20 or drone.is_emergency==True):
        rospy.logwarn("[WARNING] CRITICAL CONDITION")
    else:
        rospy.loginfo("[INFO] CONDITION OK")

if __name__=='__main__':
    rospy.init_node('sub_node')
    rospy.Subscriber('/telemetry', DroneTelemetry, callback=callback)
    rospy.spin()