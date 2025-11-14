#!/usr/bin/env python3
import rospy
import actionlib
from count_until_action.msg import CountUntilAction, CountUntilFeedback, CountUntilResult

class Count:
    def __init__(self):
        rospy.init_node('count_node')
        self._as = actionlib.SimpleActionServer('count_action_server', CountUntilAction, execute_cb=self.execute_cb, auto_start=False)
        self._as.start()
        rospy.loginfo("Action Server Started")

    def execute_cb(self, goal):
        result = CountUntilResult()
        feedback = CountUntilFeedback()
        rate = rospy.Rate(1)
        rospy.loginfo(f"Goal Received : {goal.target}")

        for i in range(goal.target + 1):
            if self._as.is_preempt_requested():
                result.success = False
                result.message = "Goal Preempted"
                self._as.set_preempted(result, "Goal is preempted")
                rospy.loginfo("Goal preempted")
                return
            
            feedback.current = i
            self._as.publish_feedback(feedback)
            rospy.loginfo(f"current i : {i}")
            rate.sleep()

        
        result.success = True
        result.message = "Goal Reached"
        self._as.set_succeeded(result)


if __name__=='__main__':
    Count()
    rospy.spin()