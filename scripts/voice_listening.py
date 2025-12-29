#!/usr/bin/env python

import rospy
import speech_recognition as sr
from std_msgs.msg import String

def main():
    rospy.init_node("voice_listener")
    rospy.loginfo("the node has started")

    recognizer = sr.Recognizer()

    voice_listener_pub = rospy.Publisher('motion_command', String, queue_size=10)

    with sr.Microphone() as source:
        while not rospy.is_shutdown():
            print("Say something!")
            audio = recognizer.listen(source)

            try:
                recognized_text = recognizer.recognize_google(audio)
                rospy.loginfo("You said: %s", recognized_text)
                #command_verifier(recognized_text)
                #pub.publish(recognized_text)
                print(recognized_text)
                #command_verifier(recognized_text)
            except sr.UnknownValueError:
                rospy.loginfo("Could not understand the audio")
            except sr.RequestError as e:
                rospy.loginfo("Could not request results; {0}".format(e))


if __name__ == "__main__":
    main()
