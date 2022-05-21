cmake_minimum_required(VERSION 3.0.0)
project(democoolprop VERSION 0.1.0)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "../bin")

set(CMAKE_CXX_FLAGS "-DCOOLPROP_LIB")

include_directories(include) 
link_directories(bin)
add_executable(demo demo.cpp)
target_link_libraries(demo CoolProp)
