cmake_minimum_required(VERSION 3.7)
project(impl)

set(CMAKE_CXX_STANDARD 11)

set(CMAKE_VERBOSE_MAKEFILE ON)

set(SOURCE_FILES
        src/main.cpp
        src/dynamic_programming.cpp
        src/dynamic_programming.h
        src/brute_force.cpp
        src/brute_force.h
        src/back_tracking.cpp
        src/back_tracking.h
        src/utils.h
        )
add_executable(impl ${SOURCE_FILES})