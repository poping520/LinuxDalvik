cmake_minimum_required(VERSION 3.10)
project(dexopt CXX)

add_executable(dexopt
        OptMain.cpp
)

target_include_directories(dexopt PRIVATE
        ../libdex
        ../vm
        # ../../external/stlport/stlport  # external/stlport/stlport
        # ../../bionic                   # bionic/
        # ../../bionic/libstdc++/include # bionic/libstdc++/include
)

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
        compat
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

install(TARGETS ${PROJECT_NAME}
        RUNTIME DESTINATION "${INSTALL_DIR}/bin"
)
