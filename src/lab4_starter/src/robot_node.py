#!/usr/bin/env python

import rospy 
import sys 
import matplotlib.pyplot as plt
from lab4_starter.msg import msg_type_trajectory 
from lab4_starter.msg import msg_type_position
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import atan2
import numpy as np 
from tf.transformations import euler_from_quaternion

from robot import robot

#robot_num = rospy.get_param("robot_number")  
#This is how you get number of robots from any file, 
#if you hard coded number of robots change the variable using this line(line16) of code

if __name__ == '__main__':
	robot_num = int(sys.argv[1])
	mode = int(sys.argv[2])
	print(mode)
	#print(robot_num)

	robots = []      #list of class 'robot'
	for i in range(robot_num):
		temp = 'robot%d' % (i)
		robots.append(robot(temp,mode))    #robot.name defined as robot(i)

	#for robot in robots:
		#rospy.init_node(robot.name, anonymous=True)
	rospy.init_node('robot_node', anonymous = True)

	for robot in robots: 
		robot.past_time = rospy.Time.now()
		robot.current_time = rospy.Time.now()
		robot.start_time = rospy.Time.now()

	while not rospy.is_shutdown():
		for robot in robots:
			robot.send_robot_status()
			robot.send_robot_position()
			robot.send_robot_penstatus()
			robot.get_robot_trajectory()
			robot.get_robot_odom()
			robot.move_to_point()

		r = rospy.Rate(10)
		r.sleep()