#!/usr/bin/env python3
import rospy
import actionlib
from action_pkg.msg import PickPlaceAction, PickPlaceFeedback, PickPlaceResult

class PickPlaceServer:
    def __init__(self):
        self.server = actionlib.SimpleActionServer("pick_place",
                                                   PickPlaceAction,
                                                   self.execute_cb,
                                                   auto_start=False)
        self.server.start()
        rospy.loginfo("PickPlace Action Server started")

    def execute_cb(self, goal):
        feedback = PickPlaceFeedback()
        result = PickPlaceResult()

        phases = ["Approaching object", "Grasping object", "Moving to destination", "Releasing object"]

        for phase in phases:
            # Check for cancel request
            if self.server.is_preempt_requested():
                rospy.logwarn("Goal cancelled!")
                result.result_message = "Action cancelled"
                self.server.set_preempted(result)
                return

            feedback.current_phase = phase
            self.server.publish_feedback(feedback)
            rospy.loginfo(f"Feedback: {phase}")
            rospy.sleep(2)  # simulate delay for each phase

        result.result_message = f"Successfully placed {goal.object_name} at target location"
        self.server.set_succeeded(result)

if __name__ == "__main__":
    rospy.init_node("pick_place_server")
    server = PickPlaceServer()
    rospy.spin()
