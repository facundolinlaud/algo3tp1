cmake_minimum_required(VERSION 3.7)
project(impl)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES src/main.cpp src/dynamic_programming.cpp src/dynamic_programming.h)
add_executable(impl ${SOURCE_FILES})