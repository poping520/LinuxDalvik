cmake_minimum_required(VERSION 3.10)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -m32")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m32")
set(CMAKE_ASM_FLAGS "${CMAKE_ASM_FLAGS} -m32")

project(LinuxDalvik)

set(INSTALL_DIR "/tmp/linux-dalvik")

message("INSTALL_DIR: " ${INSTALL_DIR})

set(CMAKE_CXX_STANDARD 11)

# Common include dirs
include_directories(
        compat/include
)

add_subdirectory(external/zlib)
add_subdirectory(external/libffi)
add_subdirectory(external/fdlibm)
add_subdirectory(compat)
add_subdirectory(libnativehelper)
add_subdirectory(dalvik)
add_subdirectory(libcore)
add_subdirectory(art/dalvikvm)


install(FILES framework-dex/core.jar
        DESTINATION "${INSTALL_DIR}/framework"
)

