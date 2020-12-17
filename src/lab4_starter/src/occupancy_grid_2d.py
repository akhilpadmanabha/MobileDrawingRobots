################################################################################
#
# OccupancyGrid2d class listens for LaserScans and builds an occupancy grid.
#
################################################################################

import rospy
import tf2_ros
import tf

from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA
from std_msgs.msg import String
from lab4_starter.msg import msg_type_trajectory 
from lab4_starter.msg import msg_type_position
from nav_msgs.msg import Odometry

import numpy as np

class OccupancyGrid2d(object):
    def __init__(self, robotNum, mode):
        self.robot_num = robotNum
        self._intialized = False
        self.r_position = []
        self.r_status = []
        self.n = 0
        self.mode = mode
        self.index = robotNum*5
        self.start_time = rospy.get_rostime()

        # Set up tf buffer and listener.
        #self._tf_buffer = tf2_ros.Buffer()
        #self._tf_listener = tf2_ros.TransformListener(self._tf_buffer)

    # Initialization and loading parameters.
    def Initialize(self):
        #self.robot_num = robot_num
        self._name = rospy.get_name() + "/grid_map_2d"

        # Load parameters.
        if not self.LoadParameters():
            rospy.logerr("%s: Error loading parameters.", self._name)
            return False

        # Register callbacks.
        if not self.RegisterCallbacks():
            rospy.logerr("%s: Error registering callbacks.", self._name)
            return False

        # Set up the map.
        self._map = np.zeros((self._x_num, self._y_num))
        self.colors = np.zeros((self._x_num, self._y_num))
        
        self.sensor_x = 0
        self.sensor_y = 0
    

        self._initialized = True
        return True
        

        

    def LoadParameters(self):
        # Random downsampling fraction, i.e. only keep this fraction of rays.
        # if not rospy.has_param("~random_downsample"):
        #     return False
        self._random_downsample = 0.1#rospy.get_param("~random_downsample")

        # Dimensions and bounds.
        # TODO! You'll need to set values for class variables called:
        # -- self._x_num
        # if not rospy.has_param("~x/num"):
        #     return False
        self._x_num = 100#rospy.get_param("~x/num")

        # -- self._x_min
        # if not rospy.has_param("~x/min"):
        #     return False
        self._x_min = 0.0#rospy.get_param("~x/min")

        # -- self._x_max
        # if not rospy.has_param("~x/max"):
        #     return False
        self._x_max = 10.0#rospy.get_param("~x/max")

        # -- self._x_res # The resolution in x. Note: This isn't a ROS parameter. What will you do instead?
        self._x_res = 0.25#(self._x_max - self._x_min)/self._x_num

        # -- self._y_num
        # if not rospy.has_param("~y/num"):
        #     return False
        self._y_num = 100#rospy.get_param("~x/num")

        # -- self._y_min
        # if not rospy.has_param("~y/min"):
        #     return False
        self._y_min = 0.0#rospy.get_param("~y/min")

        # -- self._y_max
        # if not rospy.has_param("~y/max"):
        #     return False
        self._y_max = 10#rospy.get_param("~y/max")

        # -- self._y_res # The resolution in y. Note: This isn't a ROS parameter. What will you do instead?
        self._y_res = 0.25#(self._y_max - self._y_min)/self._y_num

        # Update parameters.
        # if not rospy.has_param("~update/occupied"):
        #     return False
        ################self._occupied_update = self.ProbabilityToLogOdds(0.7)

        # if not rospy.has_param("~update/occupied_threshold"):
        #     return False
        self._occupied_threshold = self.ProbabilityToLogOdds(0.97)

        # if not rospy.has_param("~update/free"):
        #     return False
        ################self._free_update = self.ProbabilityToLogOdds(0.3)

        # if not rospy.has_param("~update/free_threshold"):
        #     return False
        #self._free_threshold = self.ProbabilityToLogOdds(0.03)

        # Topics.
        # TODO! You'll need to set values for class variables called:
        # -- self._sensor_topic
        # if not rospy.has_param("~topics/sensor"):
        #     return False
        self._sensor_topic = "/robot0/laser_0"#rospy.get_param("~topics/sensor")

        # -- self._vis_topic
        # if not rospy.has_param("~topics/vis"):
        #     return False
        self._vis_topic = "/vis/map"#rospy.get_param("~topics/vis")

        # Frames.
        # TODO! You'll need to set values for class variables called:
        # -- self._sensor_frame
        # if not rospy.has_param("~frames/sensor"):
        #     return False
        #self._sensor_frame = "robot0_laser_0"#rospy.get_param("~frames/sensor")

        # -- self._fixed_frame
        # if not rospy.has_param("~frames/fixed"):
        #     return False
        self._fixed_frame = "world"#rospy.get_param("~frames/fixed")

        return True

    def RegisterCallbacks(self):
        # Subscriber.
        self._sensor_sub = rospy.Subscriber(self._sensor_topic,
                                            LaserScan,
                                            self.SensorCallback,
                                            queue_size=1)

        # Publisher.
        self._vis_pub = rospy.Publisher(self._vis_topic,
                                        Marker,
                                        queue_size=1)

        return True

    # Callback to process sensor measurements.
    def callback_robot_position(self,message, n):
        r0x = message.position[0]
        r0y = message.position[1]
        self.r_position[n] = ([r0x, r0y])
   

    def get_robot_position(self, name, n):
        rospy.Subscriber("/%s/position" % (name), msg_type_position, self.callback_robot_position, n, queue_size = 1) 

    def callback_robot_odom(self, message, n):
        r0x = message.pose.pose.position.x
        r0y = message.pose.pose.position.y
        rot = message.pose.pose.orientation 
        self.r_position[n] = ([r0x, r0y])

    def get_robot_odom(self, name, n):   
        rospy.Subscriber("/%s/odom" % (name), Odometry, self.callback_robot_odom, n, queue_size = 1)

    def callback_penstatus(self,message, n):
        self.r_status[n] = message.data

    def get_robot_penstatus(self, name, n):
        rospy.Subscriber("/%s/penstatus" % (name), String, self.callback_penstatus, n, queue_size =1)
    
    def SensorCallback(self, msg):
        robots = []
        
    
        for x in range(self.robot_num):
            self.r_position.append([0,0])

        for x in range(self.robot_num):
            self.r_status.append('no')

        
        for i in range(self.robot_num):
            robots.append('robot%d' % (i))
        while not rospy.is_shutdown():
            self.n = 0
            for robot in robots:
                self.get_robot_odom(robot, self.n) #this listens for robot current positiion
                valz = self.PointToVoxel(self.r_position[self.n][0], self.r_position[self.n][1])
                self.get_robot_penstatus(robot, self.n)
                if(self.r_status[self.n] == 'yes'):
                    self._map[valz] = self._occupied_threshold
                    self.colors[valz] = self.n        
                    #self.flag[valz[0]][valz[1]] = -1
                self.n += 1
            self.Visualize()
                
                
            r = rospy.Rate(10)
            r.sleep()


    # Convert (x, y) coordinates in fixed frame to grid coordinates.
    def PointToVoxel(self, x, y):
        grid_x = int((x - self._x_min) / self._x_res)
        grid_y = int((y - self._y_min) / self._y_res)

        return (grid_x, grid_y)

    # Get the center point (x, y) corresponding to the given voxel.
    def VoxelCenter(self, ii, jj):
        center_x = self._x_min + (0.5 + ii) * self._x_res
        center_y = self._y_min + (0.5 + jj) * self._y_res

        return (center_x, center_y)

    # Convert between probabity and log-odds.
    def ProbabilityToLogOdds(self, p):
         return np.log(p / (1.0 - p))

    # def LogOddsToProbability(self, l):
    #     return 1.0 / (1.0 + np.exp(-l))

    # Colormap to take log odds at a voxel to a RGBA color.
    def Colormap(self, ii, jj):

        #%p = self.LogOddsToProbability(self._map[ii, jj])
        p = 0.01
        val = self.PointToVoxel(self.r_position[self.n][0], self.r_position[self.n][1])
        c = ColorRGBA()
        c.r = p
        c.g = 0.1
        c.b = 1.0 - p
        c.a = 0.75
        if self.mode == 2:
            c.r = 0
            c.b = 0
            c.g = 0
        #if((val == (ii, jj)) and (self.flag[val] == -1)):
        if self._map[ii,jj] == self._occupied_threshold:
            if(self.mode == 2):
                if(self.colors[ii, jj] ==0):
                    c.r = 1
                    c.b = 0
                    c.g = 0
                if(self.colors[ii,jj] ==1):
                    c.r = 0
                    c.b = 1
                    c.g = 0
                if(self.colors[ii,jj] == 2):
                    c.r = 0
                    c.b = 0
                    c.g = 1
                if(self.colors[ii,jj] == 3):
                    c.r = 0
                    c.b = 0.5
                    c.g = 0.5    
            else:
                c.r = 1
                c.b = 0
                c.g = 0

        
        return c


    # Visualize the map as a collection of flat cubes instead of
    # as a built-in OccupancyGrid message, since that gives us more
    # flexibility for things like color maps and stuff.
    # See http://wiki.ros.org/rviz/DisplayTypes/Marker for a brief tutorial.
    def Visualize(self):
        current_time = rospy.get_rostime()
        dt = (current_time- self.start_time).to_sec()
        if dt > 1: 
            m = Marker()
            m.header.stamp = rospy.Time.now()
            m.header.frame_id = self._fixed_frame
            m.ns = "map"
            m.id = 0
            m.type = Marker.CUBE_LIST
            m.action = Marker.ADD
            m.scale.x = self._x_res
            m.scale.y = self._y_res
            m.scale.z = 0.01
            for ii in range(self._x_num):
                for jj in range(self._y_num):
                    p = Point(0.0, 0.0, 0.0)
                    (p.x, p.y) = self.VoxelCenter(ii, jj)
                    m.points.append(p)
                    m.colors.append(self.Colormap(ii, jj))
            self._vis_pub.publish(m)
            self.start_time = rospy.get_rostime()