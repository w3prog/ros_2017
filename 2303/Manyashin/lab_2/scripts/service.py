from .Car import Car
import rospy
from .msg import Signal 
from .repair import Repair

def repair_command(data):
    try:
        repair_service = rospy.ServiceProxy('repair_service', Repair)
        result = repair_service(data.part)
        if (result.result == "Wrong"):
            rospy.loginfo("Service can't fix this")
        else:
            rospy.loginfo("Car is fixed " + result.result)
    except rospy.ServiceException, e:
        rospy.logerr("Service call failed: %s" % e)


def wait_for_command():
    rospy.wait_for_service('repair_service')
    serv = rospy.Subscriber('dispatcher_dying_patient', Signal, repair_command)

    rospy.init_node('repair__service', anonymous=True)
    rospy.spin()

if __name__ == '__main__':
    try:
        wait_for_command()
    except rospy.ROSInterruptException:
        pass