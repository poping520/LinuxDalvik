cmake_minimum_required(VERSION 3.10)
project(zlib C)

set(ZLIB_SOURCES
        src/adler32.c
        src/compress.c
        src/crc32.c
        src/deflate.c
        src/gzclose.c
        src/gzlib.c
        src/gzread.c
        src/gzwrite.c
        src/infback.c
        src/inflate.c
        src/inftrees.c
        src/inffast.c
        src/trees.c
        src/uncompr.c
        src/zutil.c
)

add_library(z SHARED ${ZLIB_SOURCES})
set_target_properties(z PROPERTIES OUTPUT_NAME z)
set_target_properties(z PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_include_directories(z
        PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_compile_definitions(z PRIVATE USE_MMAP)
target_compile_options(z PRIVATE -O3)
