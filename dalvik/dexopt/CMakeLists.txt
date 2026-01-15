cmake_minimum_required(VERSION 3.10)
project(dexopt CXX)

set(DEXOPT_SRC_FILES
        OptMain.cpp
)

set(DEXOPT_INCLUDE_DIRS
        ${CMAKE_CURRENT_SOURCE_DIR}/..              # dalvik
        ${CMAKE_CURRENT_SOURCE_DIR}/../libdex       # dalvik/libdex
        ${CMAKE_CURRENT_SOURCE_DIR}/../vm           # dalvik/vm
        ${CMAKE_CURRENT_SOURCE_DIR}/../../system/core/include   # system/core/include
        # ${CMAKE_CURRENT_SOURCE_DIR}/../../external/stlport/stlport  # external/stlport/stlport
        # ${CMAKE_CURRENT_SOURCE_DIR}/../../bionic                   # bionic/
        # ${CMAKE_CURRENT_SOURCE_DIR}/../../bionic/libstdc++/include # bionic/libstdc++/include
)

add_executable(dexopt ${DEXOPT_SRC_FILES})

target_include_directories(dexopt PRIVATE ${DEXOPT_INCLUDE_DIRS})

target_compile_definitions(dexopt PRIVATE
        ANDROID_SMP=0
        HAVE_LITTLE_ENDIAN
        HAVE_STRLCPY
        HAVE_PRCTL
)

target_link_libraries(dexopt PRIVATE
        dvm
        dl
        pthread
        z
)

target_compile_options(dexopt PRIVATE
        #-Wall
        #-Werror
)

# if (WITH_HOST_DALVIK)
#     add_executable(dexopt-host ${DEXOPT_SRC_FILES})
#     target_include_directories(dexopt-host PRIVATE ${DEXOPT_INCLUDE_DIRS})
#     target_compile_definitions(dexopt-host PRIVATE ANDROID_SMP=1)
#
#     target_link_libraries(dexopt-host PRIVATE
#         dex
#         dl
#         pthread
#         # ssl-host
#         # crypto-host
#         # icuuc-host
#         # icui18n-host
#         # cutils
#         # expat
#         # log
#         # z
#     )
# endif()
