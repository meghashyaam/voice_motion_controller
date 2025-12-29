#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("message is: " + msg)

if __name__ == "__main__":
    rospy.init_node("test_subscriber")
    rospy.loginfo("This node has started")

    rospy.Subscriber("/motion_command", String, callback)

    rospy.spin()
