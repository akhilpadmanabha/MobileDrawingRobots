#!/usr/bin/env python

import rospy 
import matplotlib.pyplot as plt
from lab4_starter.msg import msg_type_trajectory 
from lab4_starter.msg import msg_type_position
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from math import atan2
import numpy as np 
from tf.transformations import euler_from_quaternion


class robot:
	def __init__(self, name, mode, trajectory = [], status = 'no', position = [0,0], penstatus = 'no', e_past = 0, e_curr = 0, theta = 0):
		self.name = name
		self.mode = mode
		self.trajectory = trajectory
		self.status = status
		self.position = position
		self.penstatus = penstatus
		self.e_past = e_past
		self.e_curr = e_curr
		self.e_sum = 0 
		self.theta = theta
		self.current_time = 0
		self.past_time = 0
		self.start_time = 0
		self.robotstate = 'notspin'


	def namecheck(self):
		print("This is " + self.name)

	def callback_robot_trajectory(self, message):
		if self.status == 'yes':
			traject_message = message.trajectory
			self.trajectory = []
			i = 0
			while i < len(traject_message):
				l = traject_message[i].position
				self.trajectory.append(list(l))
				i+=1

	def get_robot_trajectory(self):
		rospy.Subscriber("/%s/trajectory" % (self.name), msg_type_trajectory, self.callback_robot_trajectory) 


	def callback_robot_odom(self, message):
		r0x = message.pose.pose.position.x
		r0y = message.pose.pose.position.y
		rot = message.pose.pose.orientation 
		(roll,pitch, theta) = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])
		if theta < 0:
			theta = 2 * np.pi + theta
		self.theta = theta 
		self.position = [r0x, r0y]

	def get_robot_odom(self):	
		rospy.Subscriber("/%s/odom" % (self.name), Odometry, self.callback_robot_odom, queue_size = 1)

	def send_robot_status(self):
		r0status_publisher = rospy.Publisher('/%s/status' % (self.name), String, queue_size=1)	
		#print(self.status, self.position, self.trajectory, self.penstatus)
		if self.trajectory == []: 
			self.status = 'yes'
			self.penstatus = 'no'
		else:
			x_des = self.trajectory[0][0]
			y_des = self.trajectory[0][1]
			x_curr = self.position[0]
			y_curr = self.position[1]
			#print(' ')
			#print('Desired: ' + str(self.trajectory[0][0]) + ' , ' + str(self.trajectory[0][1]))
			#print('current:' + str(self.position))
			dist = np.sqrt((x_curr-x_des)**2 + (y_curr-y_des)**2)
			if dist < 0.4:
				past_x = self.trajectory[0][0]
				self.trajectory = self.trajectory[1:]
				self.e_curr = 0 
				self.e_sum = 0 
				self.penstatus = 'yes'
				if abs(self.trajectory[0][0] - past_x) > 1 and self.mode == 2: #For multi coloring
					self.penstatus = 'no'						
				self.start_time = rospy.get_rostime()
			self.status = 'no'
		r0status_publisher.publish(self.status)
		

	def send_robot_position(self): 
		rposition_publisher = rospy.Publisher('/%s/position' % (self.name), msg_type_position, queue_size=1)
		message = msg_type_position()
		message.position = self.position
		rposition_publisher.publish(message)



	def move_to_point(self):
		move_publisher = rospy.Publisher('/%s/cmd_vel' % (self.name), Twist, queue_size = 0)
		speed = Twist()
		if self.status == 'yes':
			speed.linear.x = 0.0
			speed.angular.z = 0.0
		elif self.trajectory != []:
			Kp = 0.7
			Kd = 0.001
			Ki = 0
			self.past_time = self.current_time
			self.current_time = rospy.get_rostime()
			dt = (self.current_time- self.past_time).to_sec()

			goal = self.trajectory[0]
			goal_x = goal[0]
			goal_y = goal[1]
			inc_x = goal_x - self.position[0]
			inc_y = goal_y - self.position[1]
			des_angle = atan2(inc_y, inc_x)
			if des_angle < 0:
				des_angle = 2 * np.pi + des_angle
			self.e_past = self.e_curr
			self.e_curr = des_angle - self.theta
			d_error = self.e_curr-self.e_past 

			if self.e_curr > 3.14:
				self.e_curr = self.e_curr - (2 * 3.14)
			elif self.e_curr < -3.14:
				self.e_curr = self.e_curr + (2 * 3.14)

			e_dot = (self.e_curr - self.e_past)/dt
			self.e_sum = self.e_sum + self.e_curr*dt
			thetadot = Kp*self.e_curr + Kd*e_dot + Ki*self.e_sum
			
			#saturation if/then statements (max = 5)
			if thetadot > 0:
				if thetadot > 0.75: 
					thetadot = 0.75
			else:
				if thetadot < -0.75: 
					thetadot = -0.75
			if abs(self.e_curr) < 0.09:
				thetadot = 0
				linear_vel = 0.3
			else: 
				linear_vel = 0
			elapsed_time = (self.current_time - self.start_time).to_sec()
			'''
			if self.penstatus == 'yes' and elapsed_time > 20:
				if self.robotstate == 'spin':
					linear_vel = 0
					thetadot = 0
					if elapsed_time > 25:
						self.start_time = rospy.get_rostime()
						self.robotstate = 'notspin'
				else:
					linear_vel = 0
					thetadot = 0
					self.e_curr = 0 
					self.robotstate = 'spin'
					#self.trajectory = self.trajectory[1:]
			'''
		
			speed.linear.x = linear_vel
			speed.angular.z = thetadot

			#print('Desired: ' + str(des_angle) + ' | Current: ' + str(self.theta) + ' | Error: ' + str(self.e_curr) + ' | thetadot: ' + str(thetadot) + ' | linear_vel: ' + str(linear_vel)+ ' | time: ' + str(elapsed_time))

		speed.linear.y = 0
		speed.linear.z = 0
		speed.angular.x = 0
		speed.angular.y = 0
		move_publisher.publish(speed)

	def send_robot_penstatus(self): 
		penpublisher = rospy.Publisher('/%s/penstatus' % (self.name), String, queue_size = 1)
		penpublisher.publish(self.penstatus)
