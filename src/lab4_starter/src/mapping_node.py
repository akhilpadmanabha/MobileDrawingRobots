#!/usr/bin/python
#adapted from occupancy grid code provided by EECS 106A course staff 

from occupancy_grid_2d import OccupancyGrid2d

import rospy
import sys

if __name__ == "__main__":
    rospy.init_node("mapping_node")
    robot_num = int(sys.argv[1])
    mode = int(sys.argv[2])
    og = OccupancyGrid2d(robot_num, mode)
    if not og.Initialize():
        rospy.logerr("Failed to initialize the mapping node.")
        sys.exit(1)

    rospy.spin()
