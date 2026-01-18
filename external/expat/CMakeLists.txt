cmake_minimum_required(VERSION 3.10)

project(expat C)

add_library(expat SHARED
        lib/xmlparse.c
        lib/xmlrole.c
        lib/xmltok.c
)

target_include_directories(expat
        PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/lib
        ${CMAKE_CURRENT_LIST_DIR}
)

target_compile_definitions(expat PRIVATE
        HAVE_EXPAT_CONFIG_H
)

target_compile_options(expat PRIVATE
        -Wall
        -Wmissing-prototypes
        -Wstrict-prototypes
        -Wno-unused-parameter
        -Wno-missing-field-initializers
        -fexceptions
)

if (APPLE)
    target_compile_options($expat PRIVATE -fno-common)
endif ()


