#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys


PI = 3.1415926535897
speed = 40                 # speed in degree per seconds
linear_velocity = 1.5      # linear velocity in unit/s


def pose_callback(pose):
    
        global rob_data
        rob_data = [pose.x,pose.y,pose.theta]


def turtle_revolve():   #lin_vel,ang_vel

    # initialise the node
    rospy.init_node('node_turtle_revolve.py',
                    anonymous =True)

    # Publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                         Twist,
                                         queue_size=10)

    # Subscriber
    rospy.Subscriber('/turtle1/pose',
                     Pose,
                     pose_callback)


    rate = rospy.Rate(10) #10 Ghz
    vel_msg = Twist()


    # Converting speed in degree/s to rad/s
    angular_speed = (speed*PI)/180

    #Establishing velocity components
    vel_msg.angular.z =angular_speed 
    


    rospy.loginfo('Moving your Robot ')

    radius = 1.0/angular_speed   
    vel_msg.linear.x= linear_velocity
    total_distance  = 2*PI*radius

    # Initial time
    t0 = rospy.Time.now().to_sec()

    rate = rospy.sleep(1)
    

    current_angle = 0
    current_distance = 0
    pass

    # The function will run until current disance reaches perimeter of circle
    while (current_distance<total_distance):  
        
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed*(t1-t0)
        current_distance = current_angle*radius
      
    rate = rospy.sleep(1) # just to make sure we are getting co-ordinate values after simulatin stops
    rospy.loginfo("\n\nGoal Reached")
    print "final angle" ,current_angle*(180/PI)

    rospy.loginfo( 'Covered %f metre in %f seconds',current_distance,(t1-t0))
    print "Initial position: X = 5.544445 : Y = 5.544445 : Z= 0.000000"
    print "Final Position:   X= ",rob_data[0],'Y= ',rob_data[1],'Z= ',rob_data[2]


if __name__ == '__main__':
	try:
	   # Running our function
	   turtle_revolve()
	except rospy.ROSInterruptException:
	   pass


#  roslaunch pkg_task0 task0.launch record:=true rec_name:=task0.bag
