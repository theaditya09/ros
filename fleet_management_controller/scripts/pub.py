#!/usr/bin/env python3
import rospy
from fleet_management_controller.msg import DroneTelemetry
from geometry_msgs.msg import Point
import random

if __name__ == '__main__':
    rospy.init_node('telemetry_publisher', anonymous=True)
    pub = rospy.Publisher('telemetry', DroneTelemetry, queue_size=10)
    rate = rospy.Rate(0.5)

    while not rospy.is_shutdown():
        drone = DroneTelemetry()
        namespace = rospy.get_namespace().strip('/') or "root"
        drone.drone_id = f"{namespace}/drone"
        position = Point(random.randint(0,10), random.randint(0,10), random.randint(0,10))
        drone.position = position
        drone.battery_level = random.random()*100
        drone.is_emergency = True if random.random() <= 0.3 else False
        rospy.loginfo(f"[{rospy.get_name()}] Sent: {drone}")
        pub.publish(drone)

        rate.sleep()


