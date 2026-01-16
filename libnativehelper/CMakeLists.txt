cmake_minimum_required(VERSION 3.10)
project(nativehelper CXX)

set(CMAKE_CXX_STANDARD 11)

set(NATIVEHELPER_SOURCES
        ${CMAKE_CURRENT_SOURCE_DIR}/JNIHelp.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/JniConstants.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/toStringArray.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/JniInvocation.cpp
)

set(NATIVEHELPER_INCLUDE_DIRS
        ${CMAKE_CURRENT_SOURCE_DIR}/include/nativehelper
        ${CMAKE_CURRENT_SOURCE_DIR}/../libcore/include
        # ${CMAKE_CURRENT_SOURCE_DIR}/../system/core/include
        ../compat/include
)

add_library(
        nativehelper
        SHARED
        ${NATIVEHELPER_SOURCES}
)

target_include_directories(nativehelper PUBLIC ${NATIVEHELPER_INCLUDE_DIRS})

target_link_libraries(nativehelper PRIVATE
        compat
)

install(TARGETS nativehelper
        LIBRARY DESTINATION "${INSTALL_DIR}/lib"
)
