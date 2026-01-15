cmake_minimum_required(VERSION 3.10)

set(DEX_SRC_FILES
        CmdUtils.cpp
        DexCatch.cpp
        DexClass.cpp
        DexDataMap.cpp
        DexDebugInfo.cpp
        DexFile.cpp
        DexInlines.cpp
        DexOptData.cpp
        DexOpcodes.cpp
        DexProto.cpp
        DexSwapVerify.cpp
        DexUtf.cpp
        InstrUtils.cpp
        Leb128.cpp
        OptInvocation.cpp
        sha1.cpp
        SysUtil.cpp
        ZipArchive.cpp
)

set_source_files_properties(${DEX_SRC_FILES} PROPERTIES LANGUAGE C)

set(DEX_INCLUDE_DIRS
        ${CMAKE_CURRENT_SOURCE_DIR}/..
        ${CMAKE_CURRENT_SOURCE_DIR}/../../external/zlib
        ${CMAKE_CURRENT_SOURCE_DIR}/../../external/safe-iop/include
        ${CMAKE_CURRENT_SOURCE_DIR}/../../libnativehelper/include/nativehelper
        #${CMAKE_CURRENT_SOURCE_DIR}/../../system/core/include
)

add_library(dex STATIC ${DEX_SRC_FILES})

target_include_directories(dex PUBLIC ${DEX_INCLUDE_DIRS})

target_compile_definitions(
        dex
        PRIVATE
        HAVE_POSIX_FILEMAP
        HAVE_ENDIAN_H
)
