import rospy
from std_msgs.msg import String, Int8

topic = 'AdithyaUR'


def callback(data):
    q = 0.15
    rospy.loginfo("%s: got message- %s" % (rospy.get_caller_id(), float(data.data)/q))


def subscriber(topic):
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(topic, Int8, callback)
    rospy.spin()


def main():
    subscriber(topic=topic)


if _name== 'main_':
    main()