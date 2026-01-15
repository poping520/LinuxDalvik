cmake_minimum_required(VERSION 3.10)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -m32")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32")
set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -m32")

project(LinuxDalvik)

set(CMAKE_CXX_STANDARD 11)

include_directories(
        compat/include
)

add_subdirectory(compat)
add_subdirectory(dalvik)
add_subdirectory(external/zlib)
add_subdirectory(external/libffi)
add_subdirectory(libnativehelper)

add_executable(LinuxDalvik main.cpp)

target_link_libraries(
        LinuxDalvik PRIVATE
        nativehelper
)
