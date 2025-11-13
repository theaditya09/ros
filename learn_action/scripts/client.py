#!/usr/bin/env python3
import rospy
import actionlib
from action_pkg.msg import PickPlaceAction, PickPlaceGoal
from geometry_msgs.msg import Pose

def feedback_cb(feedback):
    rospy.loginfo(f"Feedback: {feedback.current_phase}")

if __name__ == "__main__":
    rospy.init_node("pick_place_client")
    client = actionlib.SimpleActionClient("pick_place", PickPlaceAction)

    rospy.loginfo("Waiting for action server...")
    client.wait_for_server()

    # Define goal
    goal = PickPlaceGoal()
    goal.object_name = "cube"
    goal.target_pose = Pose()  # Fill in pose if needed

    client.send_goal(goal, feedback_cb=feedback_cb)

    # Example: Cancel goal after 5 seconds
    rospy.sleep(5)
    client.cancel_goal()
    rospy.logwarn("Sent cancel request!")

    client.wait_for_result()
    rospy.loginfo(f"Final Result: {client.get_result().result_message}")
