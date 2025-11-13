cmake_minimum_required(VERSION 3.0.2)
project(action_pkg)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  actionlib_msgs
  geometry_msgs
  message_generation
)

################################################
## Declare ROS messages, services and actions ##
################################################

## Generate actions in the 'action' folder
add_action_files(
  DIRECTORY action
  FILES PickPlace.action
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
  geometry_msgs
)

###################################
## catkin specific configuration ##
###################################
catkin_package(
  CATKIN_DEPENDS
    rospy
    actionlib
    actionlib_msgs
    geometry_msgs
    message_runtime
)

###########
## Build ##
###########

include_directories(
  ${catkin_INCLUDE_DIRS}
)

#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
# catkin_install_python(PROGRAMS
#   scripts/action_server.py
#   scripts/action_client.py
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )
