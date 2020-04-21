#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import String
def buttons(data):
    info = "( "
    if (data.buttons[0]):
        info += "segitiga "
    if (data.buttons[1]):
        info += "bulat "
    if (data.buttons[2]):
        info += "silang "
    if (data.buttons[3]):
        info += "kotak "
    info += ")"
    return info;

def callback(data):
    rospy.loginfo("The total is :  %s", int(data.buttons[0]*3 + data.buttons[1]*4 + data.buttons[2]*1 + data.buttons[3]*2))
    rospy.loginfo(buttons(data))    
def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("joy", Joy, callback)
    
    rospy.spin()

if __name__ == '__main__':
    listener()