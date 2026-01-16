cmake_minimum_required(VERSION 3.10)

project(libffi C ASM)

enable_language(ASM)

set(FFI_TARGET_OS "")
if (APPLE)
    set(FFI_TARGET_OS "darwin")
else ()
    # Android uses the linux-* layout in this tree as well.
    set(FFI_TARGET_OS "linux")
endif ()

set(ANDROID_ABI "x86")

set(FFI_TARGET_ARCH "")
if (DEFINED ANDROID_ABI)
    if (ANDROID_ABI STREQUAL "armeabi" OR ANDROID_ABI STREQUAL "armeabi-v7a")
        set(FFI_TARGET_ARCH "arm")
    elseif (ANDROID_ABI STREQUAL "x86")
        set(FFI_TARGET_ARCH "x86")
    elseif (ANDROID_ABI STREQUAL "mips")
        set(FFI_TARGET_ARCH "mips")
    else ()
        set(FFI_TARGET_ARCH "")
    endif ()
elseif (DEFINED CMAKE_SYSTEM_PROCESSOR)
    string(TOLOWER "${CMAKE_SYSTEM_PROCESSOR}" _ffi_proc)
    if (_ffi_proc MATCHES "^(arm|armv[0-9]+|armv[0-9]+l)$")
        set(FFI_TARGET_ARCH "arm")
    elseif (_ffi_proc MATCHES "^(i[3-6]86|x86)$")
        set(FFI_TARGET_ARCH "x86")
    elseif (_ffi_proc MATCHES "mips")
        set(FFI_TARGET_ARCH "mips")
    else ()
        set(FFI_TARGET_ARCH "")
    endif ()
endif ()

set(_ffi_platform_dir "${CMAKE_CURRENT_LIST_DIR}/${FFI_TARGET_OS}-${FFI_TARGET_ARCH}")

set(FFI_SOURCES
        src/debug.c
        src/java_raw_api.c
        src/prep_cif.c
        src/raw_api.c
        src/types.c
)

if (FFI_TARGET_OS STREQUAL "linux" AND FFI_TARGET_ARCH STREQUAL "arm")
    list(APPEND FFI_SOURCES
            src/arm/sysv.S
            src/arm/ffi.c
    )
elseif (FFI_TARGET_OS STREQUAL "linux" AND FFI_TARGET_ARCH STREQUAL "mips")
    list(APPEND FFI_SOURCES
            src/mips/ffi.c
            src/mips/o32.S
    )
elseif ((FFI_TARGET_OS STREQUAL "linux" AND FFI_TARGET_ARCH STREQUAL "x86"))
    list(APPEND FFI_SOURCES
            src/x86/ffi.c
            src/x86/sysv.S
    )
elseif ((FFI_TARGET_OS STREQUAL "darwin" AND FFI_TARGET_ARCH STREQUAL "x86"))
    list(APPEND FFI_SOURCES
            src/x86/ffi.c
            src/x86/darwin.S
    )
else ()
    message(FATAL_ERROR "The os/architecture ${FFI_TARGET_OS}-${FFI_TARGET_ARCH} is not supported by libffi in this tree.")
endif ()

message("FFI_TARGET_OS: ${FFI_TARGET_OS}; FFI_TARGET_ARCH: ${FFI_TARGET_ARCH}")

add_library(ffi STATIC ${FFI_SOURCES})

set_target_properties(ffi PROPERTIES
        POSITION_INDEPENDENT_CODE ON
)

target_include_directories(ffi
        PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/include
        ${_ffi_platform_dir}
)

# Some libffi sources include internal headers from src/.
target_include_directories(ffi
        PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/src
)
