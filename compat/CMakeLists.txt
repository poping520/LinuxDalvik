cmake_minimum_required(VERSION 3.10)
project(compat CXX)

add_library(
        compat
        SHARED
        compat_log.cpp
)

target_include_directories(compat PRIVATE
        include
)

