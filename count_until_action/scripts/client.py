#!/usr/bin/env python3
import rospy
import actionlib
from count_until_action.msg import CountUntilAction, CountUntilGoal

def action_feedback(feedback):
    rospy.loginfo(f"[FEEDBACK] Current : {feedback.current}")

if __name__ == '__main__':
    rospy.init_node('client')
    client = actionlib.SimpleActionClient('count_action_server', CountUntilAction)
    client.wait_for_server()

    goal = CountUntilGoal()
    goal.target = int(input("Enter a number to count"))

    client.send_goal(goal, feedback_cb=action_feedback)

    finished_before_timeout = client.wait_for_result(rospy.Duration(20.0))
    if not finished_before_timeout:
        rospy.logwarn("[CLIENT] Timeout reached — cancelling goal.")
        client.cancel_goal()
    else:
        res = client.get_result()
        rospy.loginfo(f"[CLIENT] Result: success={res.success}, message='{res.message}'")


