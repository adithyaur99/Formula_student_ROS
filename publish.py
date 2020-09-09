import rospy
from std_msgs.msg import String, Int8

message1 = 'AdithyaUR'
message2= 'kthfs/result'
rate = 20


def publisher(topic1, topic2, rate=20):
    pub1 = rospy.Publisher(topic1, Int8, queue_size=10)
    rospy.init_node('Publisher', anonymous=True)
    rate = rospy.Rate(rate)     # hz

    n = 4
    k=1
    while not rospy.is_shutdown():
        while(k<20):
            k=k+4
            rospy.loginfo("publishing %s to topics [%s, %s]" % (k, topic1, topic2))
            pub1.publish(k)

            subscriber(topic=topic)

            pub1.publish(k)
            rate.sleep()



def callback(data):
    rospy.loginfo("%s: got message- %s" % (rospy.get_caller_id(), float(data.data)))


def subscriber(topic):
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(topic, Int8, callback)
    rospy.spin()


def main():
    publisher(topic1=message1, topic2=message2, rate=rate)
   


if _name== 'main_':
    main()
