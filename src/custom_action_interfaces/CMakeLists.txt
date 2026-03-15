cmake_minimum_required(VERSION 3.8)
project(custom_action_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)

# 1. Find the generator package
find_package(rosidl_default_generators REQUIRED)

# 2. Tell CMake to build your custom Action file
rosidl_generate_interfaces(${PROJECT_NAME}
  "action/Fibonacci.action"
)

ament_package()
