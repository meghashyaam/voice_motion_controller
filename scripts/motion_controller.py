#!/sys/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
motion_pub = None
msg_command = "stop"


def motion_callback_function(msg):
    global msg_command
    rospy.loginfo(msg)
    msg_command = msg.data

def publish_motion(event):
    #global motion_pub 
    #pub = rospy.Publisher("/cmd_vel", S)
    motion_pub_msg = Twist()
    
    rospy.loginfo("msg_command is:" + msg_command + ".")
    rospy.loginfo(type(msg_command) == type("move forward"))
    rospy.loginfo(msg_command == "move forward")
    #rospy.loginfo(msg_command)
    #if msg.data == "wave":
        #motion_pub_msg = wave()
    if msg_command == "turn left":
        rospy.loginfo("branch1")
        motion_pub_msg.angular.z = 0.5
        motion_pub_msg.linear.x = 0.0
    elif msg_command == "turn right":
        rospy.loginfo("branch2")
        motion_pub_msg.angular.z = -0.5
        motion_pub_msg.linear.x = 0.0
    elif msg_command == "move forward":
        rospy.loginfo("branch3")
        motion_pub_msg.angular.z = 0.0
        motion_pub_msg.linear.x = 0.2
    elif msg_command == "move backward":
        rospy.loginfo("branch4")
        motion_pub_msg.angular.z = 0.0
        motion_pub_msg.linear.x = -0.2
    elif msg_command == "stop":
        rospy.loginfo("branch5")
        motion_pub_msg.angular.z = 0.0
        motion_pub_msg.linear.x = 0.0
    else:
        pass

    motion_pub.publish(motion_pub_msg)


def main():
    
    rospy.init_node("Subscriber_node")
    rospy.loginfo("The node has started")
    global motion_pub
    motion_pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
    rospy.sleep(0.5)
    subs = rospy.Subscriber("/motion_command", String, motion_callback_function)
    rospy.Timer(rospy.Duration(0.1), publish_motion)
    rospy.spin()

if __name__ == "__main__":
    #rospy.init_node("Subscriber_node")
    #rospy.loginfo("The node has started")
    main()

