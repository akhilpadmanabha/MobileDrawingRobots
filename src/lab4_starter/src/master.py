#!/usr/bin/env python

import rospy 
import roslaunch
import numpy as np 
import cv2 as cv 
from lab4_starter.msg import msg_type_trajectory 
from lab4_starter.msg import msg_type_position
from std_msgs.msg import String
from matplotlib import pyplot as plt
import time
import random 
import coloring

r_position = []
r_status = []
r_times = []

#Subscriber for robot status 
def callback_robot_status(message, n):
	r_status[n] = message.data

def get_robot_status(name, n):
	rospy.Subscriber("/%s/status" % (name), String, callback_robot_status, n, queue_size=1) 

#Subscriber for robot position
def callback_robot_position(message, n):
	r0x = message.position[0]
	r0y = message.position[1]
	r_position[n] = ([r0x, r0y])

def get_robot_position(name, n):
	rospy.Subscriber("/%s/position" % (name), msg_type_position, callback_robot_position, n) 

#optimization functions for choosing trajectories 
def distance(point1, point2):
	x1 = point1[0]
	y1 = point1[1]
	x2 = point2[0]
	y2 = point2[1]
	return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def optimization(robottrajectories, n): 
	#optimization using distance from current position
	mindist = 1000000
	minindex = 0
	startorend = 0 #0 for start, 1 for end 
	x = 0
	while x < len(robottrajectories):
		trajectory = robottrajectories[x]
		startpoint = trajectory[0]
		dist = distance(startpoint, r_position[n])
		if dist < mindist:
			mindist = dist
			startorend = 0
			minindex = x 
		if len(trajectory) > 1:
			endpoint = trajectory[len(trajectory)-1]
			dist = distance(endpoint, r_position[n])
			if dist < mindist:
				mindist = dist
				startorend = 1
				minindex = x
		x += 1
	next_trajectory = robottrajectories[minindex]
	if startorend == 1: #if the end element is closer than the start element
		next_trajectory.reverse()
	robottrajectories.pop(minindex)
	return next_trajectory

#send robot trajectory functions
def send_robot_trajectory(name,n): #for edges case 
	rtrajectory_publisher = rospy.Publisher('/%s/trajectory' % (name), msg_type_trajectory, queue_size=10)
	if robot_trajectories != [] and r_status[n] == 'yes' and (rospy.get_rostime() - r_times[n]).to_sec() > 3:
		rtrajectory = msg_type_trajectory()
		next_trajectory = optimization(robot_trajectories,n) #picks new trajectory based on optimization
		i = 0
		while i < len(next_trajectory):
			data = msg_type_position()
			data.position = next_trajectory[i]
			rtrajectory.trajectory.append(data)
			i+=1
		print('sent trajectory')
		r_times[n] = rospy.get_rostime()
		rtrajectory_publisher.publish(rtrajectory)

def send_robot_trajectory_logo(name,n): #for fill case 
	rtrajectory_publisher = rospy.Publisher('/%s/trajectory' % (name), msg_type_trajectory, queue_size=10)
	if robot_trajectories[n] != [] and r_status[n] == 'yes':
		rtrajectory = msg_type_trajectory()
		next_trajectory = optimization(robot_trajectories[n],n) #picks new trajectory based on optimization
		i = 0
		while i < len(next_trajectory):
			data = msg_type_position()
			data.position = next_trajectory[i]
			rtrajectory.trajectory.append(data)
			i+=1
		rtrajectory_publisher.publish(rtrajectory)
	else:
		print(str(name)+'done')




def launch_file(robot_num):
	uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
	roslaunch.configure_logging(uuid)
	#file = 'main' + str(robot_num) + '.launch'
	file = 'main.launch'
	#args = 'robot_num:= ' + str(robot_num)
	cli_args1 = ['lab4_starter', file]
	roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(cli_args1)
	roslaunch_args1 = cli_args1[2:]
	roslaunch_files = roslaunch_file1 
	roslaunch_args = [roslaunch_args1]
	parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_files, roslaunch_args)
	parent.start()

def rviz_launch_file():
	uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
	roslaunch.configure_logging(uuid)
	#file = 'main' + str(robot_num) + '.launch'
	file = 'rviz.launch'
	#args = 'robot_num:= ' + str(robot_num)
	cli_args1 = ['stdr_launchers', file]
	roslaunch_file1 = roslaunch.rlutil.resolve_launch_arguments(cli_args1)
	roslaunch_args1 = cli_args1[2:]
	roslaunch_files = roslaunch_file1 
	roslaunch_args = [roslaunch_args1]
	parent = roslaunch.parent.ROSLaunchParent(uuid, roslaunch_files, roslaunch_args)
	parent.start()

def rviz_node():
	package = 'rviz'
	executable = 'rviz'
	string = "-d $(find stdr_launchers)/rviz/config.rviz"
	node = roslaunch.core.Node(package, executable, args = string)

	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)
	print process.is_alive()
	time.sleep(1)


def spawn_robot(): 
	package = 'stdr_robot'
	executable = 'robot_handler'
	randomx = random.randrange(3, 22) #spawning x range 
	randomy = random.randrange(3, 22) #spawning y range
	
	string = 'add $(find lab4_starter)/robots/simple_robot.yaml ' + str(randomx) + ' ' + str(randomy) + ' 0'
	node = roslaunch.core.Node(package, executable, args = string)

	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)
	print process.is_alive()
	time.sleep(1)

def spawn_robot_logo(i): 
	package = 'stdr_robot'
	executable = 'robot_handler'
	#x = list()
	#a.append()
	randomx = random.randrange(3, 22) #spawning x range 
	randomy = random.randrange(3, 22) #spawning y range
	
	string = 'add $(find lab4_starter)/robots/simple_robot.yaml ' + str(randomx) + ' ' + str(randomy) + ' 0'
	node = roslaunch.core.Node(package, executable, args = string)

	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)
	print process.is_alive()
	time.sleep(1)

def start_robot_node(robot_num , mode):
	package = 'lab4_starter'
	executable = 'robot_node.py'

	string = str(robot_num) + ' ' + str(mode)
	node = roslaunch.core.Node(package, executable, args = string)
	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)
	print process.is_alive()
	time.sleep(2)

def start_drawing_node(robot_num, mode):
	package = 'lab4_starter'
	executable = 'mapping_node.py'

	string = str(robot_num) + ' ' + str(mode)
	node = roslaunch.core.Node(package, executable, args = string)
	launch = roslaunch.scriptapi.ROSLaunch()
	launch.start()

	process = launch.launch(node)
	print process.is_alive()
	time.sleep(2)

def scale_trajectories(trajectories):
	new_trajectories = []
	for trajectory in trajectories: 
		new_trajectory = []
		for point in trajectory: 
			new_point = []
			for i in point: 
				new_i = float(i)/8
				new_point.append(new_i)
			new_trajectory.append(new_point)
		new_trajectories.append(new_trajectory)
	return new_trajectories 

#CV functions
def generate_bounds(blurred, sigma):
	#adapted from https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
	med = np.median(blurred)
	lower = int(max(0, (1.0 - sigma) * med))
	upper = int(min(255, (1.0 + sigma) * med))
	return [lower, upper]


def comp_vision(imagepath): #CV for edges case
	img_path = imagepath
	color_img = cv.imread(img_path)
	img = cv.imread(img_path, 0) #will only work if you are in the directory where it is located
	#cv.imshow('Original Image', color_img)
	img = cv.resize(img, (200, 200))
	blurred = cv.GaussianBlur(img, (3,3), 0)
	sigma = 0.33
	user_input = 0
	while(user_input != 'start'):
		[lower, upper] = generate_bounds(blurred, sigma)
		edges = cv.Canny(blurred, lower, upper)
		cv.imshow('Edges', edges)
		cv.waitKey(250)
		user_input = raw_input('Enter start to begin, 0 to decrease edges, 1 to increase edges, or c to quit: ')
		if user_input == '0':
			sigma = sigma  - 0.05
		elif user_input == '1':
			sigma = sigma + 0.05
		elif user_input == 'c':
			exit()
		cv.destroyAllWindows()

	_, contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

	trajectories = []
	for i in range(0,len(contours)):
		add = []
		for l in contours[i]: 
			new = l[0].tolist()
			add.append(new)
		trajectories.append(add)
	print(trajectories)
	return trajectories 

def comp_vision_logo(robot_num, imagepath): #CV for fill case 
	IMG_DIR = coloring.IMG_DIR
	test_img_color = coloring.read_image(IMG_DIR + '/%s' % (imagepath))
	test_img_color = cv.resize(test_img_color, (200, 200))
	coloring.test_cluster(test_img_color,6,robot_num)    # 6-2 = 4 different clusters will be given
	color_traj = coloring.c_trajectories
	color_traj = scale_trajectories(color_traj)
	return color_traj 

if __name__ == '__main__':
	#user input 
	imagepath = raw_input('Enter image path: ')
	robot_num = int(raw_input('Enter the number of robots: '))
	mode = int(raw_input('Enter mode (1 for edges, 2 for logo with fill): '))

	#imagepath = '/chrome.jpg'
	#mode = 2

	#generating trajectories based on the mode selected 
	if mode == 1: 
		robot_trajectories = scale_trajectories(comp_vision(imagepath))
		print('Number of Trajectories: ' +  str(len(robot_trajectories)))
	elif mode == 2: 
		robot_trajectories = comp_vision_logo(robot_num, imagepath)
		print(len(robot_trajectories))

	#launches launch file and nodes 
	launch_file(robot_num) #if this is bugging out and saying roscore is running already use command "killall -9 rosmaster" in terminal
	start_drawing_node(robot_num, mode)
	start_robot_node(robot_num, mode)

	for x in range(robot_num): #spawns robots based on the number of robots inputted by user 
		spawn_robot()
		
	rviz_node() #starts rviz 

	rospy.init_node('master', anonymous=True)

	for x in range(robot_num):
		r_status.append('no')
		r_position.append([0,0])
		r_times.append(rospy.get_rostime())

	robots = []
	
	for i in range(robot_num):
		robots.append('robot%d' % (i))

	while not rospy.is_shutdown():
		n = 0
		for robot in robots:
			get_robot_status(robot, n)
			get_robot_position(robot, n) #this listens for robot current positiion
			if mode == 1: 
				send_robot_trajectory(robot,n) #this publishes a trajectory for robot
			elif mode == 2:
				send_robot_trajectory(robot,n)
			n += 1
		r = rospy.Rate(10)
		r.sleep()
	
	