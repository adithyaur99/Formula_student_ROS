#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int8


#constants
topic1 = 'vigneshpurushothamsrinivas'
topic2 = 'kthfs/result'
rate = 20


def publisher(topic1, topic2, rate=20):
    pub1 = rospy.Publisher(topic1, Int8, queue_size=10)
    pub2 = rospy.Publisher(topic2, Int8, queue_size=10)
    rospy.init_node('Publisher', anonymous=True)
    rate = rospy.Rate(rate)     # hz

    n = 4
    while not rospy.is_shutdown():
        for k in range(1, 20, n):
            rospy.loginfo("publishing %s to topics [%s, %s]" % (k, topic1, topic2))
            pub1.publish(k)
            pub2.publish(k)
            rate.sleep()

def main():
    try:
        publisher(topic1=topic1, topic2=topic2, rate=rate)
    except rospy.ROSInterruptException:
        # print "Program Interrupted"
        pass


if _name== 'main_':
    main()