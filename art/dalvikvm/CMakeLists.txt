cmake_minimum_required(VERSION 3.10)

project(dalvikvm)

add_executable(${PROJECT_NAME}
        dalvikvm.cc
)

target_include_directories(
        ${PROJECT_NAME}
        PRIVATE
        ../../libnativehelper/include
)

target_link_libraries(
        ${PROJECT_NAME}
        PRIVATE
        nativehelper
)

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION "${INSTALL_DIR}/bin"
)