cmake_minimum_required(VERSION 3.0.2)
project(learn_action)

## Compile as C++11
add_compile_options(-std=c++11)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS
  actionlib
  actionlib_msgs
  geometry_msgs
  rospy
  roscpp
  actionPkg   # <-- your package that defines the .action file
)

catkin_package(
  CATKIN_DEPENDS actionlib actionlib_msgs geometry_msgs rospy roscpp actionPkg
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Example: Add an action server node
# add_executable(server_node src/server.cpp)
# target_link_libraries(server_node ${catkin_LIBRARIES})
# add_dependencies(server_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Example: Add an action client node
# add_executable(client_node src/client.cpp)
# target_link_libraries(client_node ${catkin_LIBRARIES})
# add_dependencies(client_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
