cmake_minimum_required(VERSION 3.10)
project(compat CXX)

add_library(
        compat
        SHARED
        ashmem-host.c
        compat_log.c
        fs.c
        multiuser.c
        process_name.c
        sched_policy.c
        sockets.c
)

target_compile_definitions(compat PRIVATE
        HAVE_PRCTL
)

target_include_directories(compat PRIVATE
        include
)

install(TARGETS compat
        LIBRARY DESTINATION "${INSTALL_DIR}/lib"
)

