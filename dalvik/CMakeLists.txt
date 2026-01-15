cmake_minimum_required(VERSION 3.10)
project(dvm C CXX ASM)

#set(CMAKE_CXX_STANDARD 11)
#set(CMAKE_C_STANDARD 11)

option(WITH_JIT "Enable JIT compiler" OFF)
option(WITH_COPYING_GC "Enable copying garbage collector" OFF)
option(WITH_DALVIK_ASSERT "Enable Dalvik assertions" OFF)
option(WITH_SELF_VERIFICATION "Enable JIT self-verification" OFF)
option(WITH_JIT_TUNING "Enable JIT tuning" OFF)
option(DEBUG_DALVIK_VM "Build debug VM" OFF)

set(WITH_JIT OFF)
set(WITH_JIT_TUNING OFF)

# set(DVM_ARCH "${CMAKE_SYSTEM_PROCESSOR}")
set(DVM_ARCH "x86")
set(DVM_ARCH_VARIANT "${DVM_ARCH}")
set(DVM_OS "${CMAKE_SYSTEM_NAME}")

message("DVM_ARCH: " ${DVM_ARCH})
message("DVM_OS:   " ${CMAKE_SYSTEM_NAME})

if (CMAKE_SYSTEM_NAME STREQUAL "Linux")
    set(ANDROID_SMP 1)
else ()
    set(ANDROID_SMP 0)
endif ()

set(DVM_SRC_DIR "${CMAKE_CURRENT_SOURCE_DIR}/vm")

add_subdirectory(libdex)
add_subdirectory(dexopt)

set(DVM_COMMON_SOURCES
        ${DVM_SRC_DIR}/AllocTracker.cpp
        ${DVM_SRC_DIR}/Atomic.cpp
        ${DVM_SRC_DIR}/AtomicCache.cpp
        ${DVM_SRC_DIR}/BitVector.cpp
        ${DVM_SRC_DIR}/CheckJni.cpp
        ${DVM_SRC_DIR}/Ddm.cpp
        ${DVM_SRC_DIR}/Debugger.cpp
        ${DVM_SRC_DIR}/DvmDex.cpp
        ${DVM_SRC_DIR}/Exception.cpp
        ${DVM_SRC_DIR}/Hash.cpp
        ${DVM_SRC_DIR}/IndirectRefTable.cpp
        ${DVM_SRC_DIR}/Init.cpp
        ${DVM_SRC_DIR}/InitRefs.cpp
        ${DVM_SRC_DIR}/InlineNative.cpp
        ${DVM_SRC_DIR}/Inlines.cpp
        ${DVM_SRC_DIR}/Intern.cpp
        ${DVM_SRC_DIR}/Jni.cpp
        ${DVM_SRC_DIR}/JarFile.cpp
        ${DVM_SRC_DIR}/LinearAlloc.cpp
        ${DVM_SRC_DIR}/Misc.cpp
        ${DVM_SRC_DIR}/Native.cpp
        ${DVM_SRC_DIR}/PointerSet.cpp
        ${DVM_SRC_DIR}/Profile.cpp
        ${DVM_SRC_DIR}/RawDexFile.cpp
        ${DVM_SRC_DIR}/ReferenceTable.cpp
        ${DVM_SRC_DIR}/SignalCatcher.cpp
        ${DVM_SRC_DIR}/StdioConverter.cpp
        ${DVM_SRC_DIR}/Sync.cpp
        ${DVM_SRC_DIR}/Thread.cpp
        ${DVM_SRC_DIR}/UtfString.cpp
        ${DVM_SRC_DIR}/alloc/Alloc.cpp
        ${DVM_SRC_DIR}/alloc/CardTable.cpp
        ${DVM_SRC_DIR}/alloc/HeapBitmap.cpp
        ${DVM_SRC_DIR}/alloc/HeapDebug.cpp
        ${DVM_SRC_DIR}/alloc/Heap.cpp
        ${DVM_SRC_DIR}/alloc/DdmHeap.cpp
        ${DVM_SRC_DIR}/alloc/Verify.cpp
        ${DVM_SRC_DIR}/alloc/Visit.cpp
        ${DVM_SRC_DIR}/analysis/CodeVerify.cpp
        ${DVM_SRC_DIR}/analysis/DexPrepare.cpp
        ${DVM_SRC_DIR}/analysis/DexVerify.cpp
        ${DVM_SRC_DIR}/analysis/Liveness.cpp
        ${DVM_SRC_DIR}/analysis/Optimize.cpp
        ${DVM_SRC_DIR}/analysis/RegisterMap.cpp
        ${DVM_SRC_DIR}/analysis/VerifySubs.cpp
        ${DVM_SRC_DIR}/analysis/VfyBasicBlock.cpp
        ${DVM_SRC_DIR}/hprof/Hprof.cpp
        ${DVM_SRC_DIR}/hprof/HprofClass.cpp
        ${DVM_SRC_DIR}/hprof/HprofHeap.cpp
        ${DVM_SRC_DIR}/hprof/HprofOutput.cpp
        ${DVM_SRC_DIR}/hprof/HprofString.cpp
        ${DVM_SRC_DIR}/interp/Interp.cpp
        ${DVM_SRC_DIR}/interp/Stack.cpp
        ${DVM_SRC_DIR}/jdwp/ExpandBuf.cpp
        ${DVM_SRC_DIR}/jdwp/JdwpAdb.cpp
        ${DVM_SRC_DIR}/jdwp/JdwpConstants.cpp
        ${DVM_SRC_DIR}/jdwp/JdwpEvent.cpp
        ${DVM_SRC_DIR}/jdwp/JdwpHandler.cpp
        ${DVM_SRC_DIR}/jdwp/JdwpMain.cpp
        ${DVM_SRC_DIR}/jdwp/JdwpSocket.cpp
        ${DVM_SRC_DIR}/mterp/Mterp.cpp
        ${DVM_SRC_DIR}/mterp/out/InterpC-portable.cpp
        ${DVM_SRC_DIR}/native/InternalNative.cpp
        ${DVM_SRC_DIR}/native/dalvik_bytecode_OpcodeInfo.cpp
        ${DVM_SRC_DIR}/native/dalvik_system_DexFile.cpp
        ${DVM_SRC_DIR}/native/dalvik_system_VMDebug.cpp
        ${DVM_SRC_DIR}/native/dalvik_system_VMRuntime.cpp
        ${DVM_SRC_DIR}/native/dalvik_system_VMStack.cpp
        ${DVM_SRC_DIR}/native/dalvik_system_Zygote.cpp
        ${DVM_SRC_DIR}/native/java_lang_Class.cpp
        ${DVM_SRC_DIR}/native/java_lang_Double.cpp
        ${DVM_SRC_DIR}/native/java_lang_Float.cpp
        ${DVM_SRC_DIR}/native/java_lang_Math.cpp
        ${DVM_SRC_DIR}/native/java_lang_Object.cpp
        ${DVM_SRC_DIR}/native/java_lang_Runtime.cpp
        ${DVM_SRC_DIR}/native/java_lang_String.cpp
        ${DVM_SRC_DIR}/native/java_lang_System.cpp
        ${DVM_SRC_DIR}/native/java_lang_Throwable.cpp
        ${DVM_SRC_DIR}/native/java_lang_VMClassLoader.cpp
        ${DVM_SRC_DIR}/native/java_lang_VMThread.cpp
        ${DVM_SRC_DIR}/native/java_lang_reflect_AccessibleObject.cpp
        ${DVM_SRC_DIR}/native/java_lang_reflect_Array.cpp
        ${DVM_SRC_DIR}/native/java_lang_reflect_Constructor.cpp
        ${DVM_SRC_DIR}/native/java_lang_reflect_Field.cpp
        ${DVM_SRC_DIR}/native/java_lang_reflect_Method.cpp
        ${DVM_SRC_DIR}/native/java_lang_reflect_Proxy.cpp
        ${DVM_SRC_DIR}/native/java_util_concurrent_atomic_AtomicLong.cpp
        ${DVM_SRC_DIR}/native/org_apache_harmony_dalvik_NativeTestTarget.cpp
        ${DVM_SRC_DIR}/native/org_apache_harmony_dalvik_ddmc_DdmServer.cpp
        ${DVM_SRC_DIR}/native/org_apache_harmony_dalvik_ddmc_DdmVmInternal.cpp
        ${DVM_SRC_DIR}/native/sun_misc_Unsafe.cpp
        ${DVM_SRC_DIR}/oo/AccessCheck.cpp
        ${DVM_SRC_DIR}/oo/Array.cpp
        ${DVM_SRC_DIR}/oo/Class.cpp
        ${DVM_SRC_DIR}/oo/Object.cpp
        ${DVM_SRC_DIR}/oo/Resolve.cpp
        ${DVM_SRC_DIR}/oo/TypeCheck.cpp
        ${DVM_SRC_DIR}/reflect/Annotation.cpp
        ${DVM_SRC_DIR}/reflect/Proxy.cpp
        ${DVM_SRC_DIR}/reflect/Reflect.cpp
        ${DVM_SRC_DIR}/test/AtomicTest.cpp
        ${DVM_SRC_DIR}/test/TestHash.cpp
        ${DVM_SRC_DIR}/test/TestIndirectRefTable.cpp
)

if (DVM_ARCH MATCHES "arm|mips")
    list(APPEND DVM_COMMON_SOURCES ${DVM_SRC_DIR}/os/android.cpp)
else ()
    list(APPEND DVM_COMMON_SOURCES ${DVM_SRC_DIR}/os/linux.cpp)
endif ()

if (WITH_COPYING_GC)
    list(APPEND DVM_COMMON_SOURCES ${DVM_SRC_DIR}/alloc/Copying.cpp)
else ()
    list(APPEND DVM_COMMON_SOURCES
            ${DVM_SRC_DIR}/alloc/DlMalloc.cpp
            ${DVM_SRC_DIR}/alloc/HeapSource.cpp
            ${DVM_SRC_DIR}/alloc/MarkSweep.cpp
    )
endif ()

if (WITH_JIT)
    list(APPEND DVM_COMMON_SOURCES
            ${DVM_SRC_DIR}/compiler/Compiler.cpp
            ${DVM_SRC_DIR}/compiler/Frontend.cpp
            ${DVM_SRC_DIR}/compiler/Utility.cpp
            ${DVM_SRC_DIR}/compiler/InlineTransformation.cpp
            ${DVM_SRC_DIR}/compiler/IntermediateRep.cpp
            ${DVM_SRC_DIR}/compiler/Dataflow.cpp
            ${DVM_SRC_DIR}/compiler/SSATransformation.cpp
            ${DVM_SRC_DIR}/compiler/Loop.cpp
            ${DVM_SRC_DIR}/compiler/Ralloc.cpp
            ${DVM_SRC_DIR}/interp/Jit.cpp
    )
endif ()

set(DVM_INCLUDE_DIRS
        ${CMAKE_CURRENT_SOURCE_DIR}
        ${DVM_SRC_DIR}
        ${CMAKE_CURRENT_SOURCE_DIR}/../external/zlib
        ${CMAKE_CURRENT_SOURCE_DIR}/../libcore/include
        ${CMAKE_CURRENT_SOURCE_DIR}/../libnativehelper/include/nativehelper
        # ${CMAKE_CURRENT_SOURCE_DIR}/../system/core/include
)

set(DVM_COMPILE_DEFINITIONS
        ARCH_VARIANT="${DVM_ARCH_VARIANT}"
        ANDROID_SMP=${ANDROID_SMP}
        DVM_SHOW_EXCEPTION=1
        HAVE_LITTLE_ENDIAN
        HAVE_STRLCPY
        OS_SHARED_LIB_FORMAT_STR="lib%s.so"
)

if (DEBUG_DALVIK_VM)
    list(APPEND DVM_COMPILE_DEFINITIONS
            WITH_INSTR_CHECKS
            WITH_EXTRA_OBJECT_VALIDATION
            WITH_TRACKREF_CHECKS
            WITH_EXTRA_GC_CHECKS=1
            EASY_GDB
            DEBUG=1
            LOG_NDEBUG=1
            WITH_DALVIK_ASSERT
    )
endif ()

if (WITH_JIT)
    list(APPEND DVM_COMPILE_DEFINITIONS WITH_JIT)
endif ()

if (WITH_COPYING_GC)
    list(APPEND DVM_COMPILE_DEFINITIONS WITH_COPYING_GC)
endif ()

if (WITH_DALVIK_ASSERT)
    list(APPEND DVM_COMPILE_DEFINITIONS WITH_DALVIK_ASSERT DEBUG=1 LOG_NDEBUG=1)
endif ()

if (WITH_SELF_VERIFICATION)
    list(APPEND DVM_COMPILE_DEFINITIONS WITH_SELF_VERIFICATION)
endif ()

if (WITH_JIT_TUNING)
    list(APPEND DVM_COMPILE_DEFINITIONS WITH_JIT_TUNING)
endif ()

set(DVM_COMPILE_OPTIONS
        -fstrict-aliasing
        -Wstrict-aliasing=2
        -Wall
        -Wextra
        -Wno-unused-parameter
)

if (NOT CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    list(APPEND DVM_COMPILE_OPTIONS -fno-align-jumps)
endif ()

if (DVM_ARCH MATCHES "arm")
    list(APPEND DVM_COMPILE_OPTIONS -Werror)
    list(APPEND DVM_ARCH_SOURCES
            ${DVM_SRC_DIR}/arch/arm/CallOldABI.S
            ${DVM_SRC_DIR}/arch/arm/CallEABI.S
            ${DVM_SRC_DIR}/arch/arm/HintsEABI.cpp
            ${DVM_SRC_DIR}/mterp/out/InterpC-${DVM_ARCH_VARIANT}.cpp
            ${DVM_SRC_DIR}/mterp/out/InterpAsm-${DVM_ARCH_VARIANT}.S
    )
    if (WITH_JIT)
        list(APPEND DVM_ARCH_SOURCES
                ${DVM_SRC_DIR}/compiler/codegen/RallocUtil.cpp
                ${DVM_SRC_DIR}/compiler/codegen/arm/${DVM_ARCH_VARIANT}/Codegen.cpp
                ${DVM_SRC_DIR}/compiler/codegen/arm/${DVM_ARCH_VARIANT}/CallingConvention.S
                ${DVM_SRC_DIR}/compiler/codegen/arm/Assemble.cpp
                ${DVM_SRC_DIR}/compiler/codegen/arm/ArchUtility.cpp
                ${DVM_SRC_DIR}/compiler/codegen/arm/LocalOptimizations.cpp
                ${DVM_SRC_DIR}/compiler/codegen/arm/GlobalOptimizations.cpp
                ${DVM_SRC_DIR}/compiler/codegen/arm/ArmRallocUtil.cpp
                ${DVM_SRC_DIR}/compiler/template/out/CompilerTemplateAsm-${DVM_ARCH_VARIANT}.S
        )
    endif ()
elseif (DVM_ARCH MATCHES "mips")
    list(APPEND DVM_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/../external/libffi/${DVM_OS}-${DVM_ARCH})
    list(APPEND DVM_ARCH_SOURCES
            ${DVM_SRC_DIR}/arch/mips/CallO32.S
            ${DVM_SRC_DIR}/arch/mips/HintsO32.cpp
            ${DVM_SRC_DIR}/arch/generic/Call.cpp
            ${DVM_SRC_DIR}/mterp/out/InterpC-mips.cpp
            ${DVM_SRC_DIR}/mterp/out/InterpAsm-mips.S
    )
    if (WITH_JIT)
        list(APPEND DVM_ARCH_SOURCES
                ${DVM_SRC_DIR}/compiler/codegen/mips/RallocUtil.cpp
                ${DVM_SRC_DIR}/compiler/codegen/mips/${DVM_ARCH_VARIANT}/Codegen.cpp
                ${DVM_SRC_DIR}/compiler/codegen/mips/${DVM_ARCH_VARIANT}/CallingConvention.S
                ${DVM_SRC_DIR}/compiler/codegen/mips/Assemble.cpp
                ${DVM_SRC_DIR}/compiler/codegen/mips/ArchUtility.cpp
                ${DVM_SRC_DIR}/compiler/codegen/mips/LocalOptimizations.cpp
                ${DVM_SRC_DIR}/compiler/codegen/mips/GlobalOptimizations.cpp
                ${DVM_SRC_DIR}/compiler/template/out/CompilerTemplateAsm-${DVM_ARCH_VARIANT}.S
        )
    endif ()
elseif (DVM_ARCH MATCHES "x86|i386|i686")
    if (DVM_OS STREQUAL "Linux")
        list(APPEND DVM_COMPILE_DEFINITIONS DVM_JMP_TABLE_MTERP=1 MTERP_STUB)
        #        list(APPEND DVM_ARCH_SOURCES
        #                ${DVM_SRC_DIR}/arch/x86/Hints386ABI.cpp
        #                ${DVM_SRC_DIR}/mterp/out/InterpC-x86.cpp
        #                ${DVM_SRC_DIR}/arch/x86/Call386ABI.S
        #                ${DVM_SRC_DIR}/mterp/out/InterpAsm-x86.S
        #        )

        # portable
        list(APPEND DVM_INCLUDE_DIRS ${CMAKE_CURRENT_SOURCE_DIR}/../external/libffi/${DVM_OS}-${DVM_ARCH})
        list(APPEND DVM_COMPILE_DEFINITIONS
                dvmAsmInstructionStart=0
                dvmAsmInstructionEnd=0
                dvmAsmSisterStart=0
                dvmAsmSisterEnd=0
                DVM_NO_ASM_INTERP=1
        )
        list(APPEND DVM_ARCH_SOURCES
                ${DVM_SRC_DIR}/arch/generic/Call.cpp
                ${DVM_SRC_DIR}/arch/generic/Hints.cpp
                ${DVM_SRC_DIR}/mterp/out/InterpC-allstubs.cpp
        )

        if (WITH_JIT)
            list(APPEND DVM_COMPILE_DEFINITIONS ARCH_IA32)
            list(APPEND DVM_INCLUDE_DIRS ${DVM_SRC_DIR}/compiler/codegen/x86/libenc)
            list(APPEND DVM_ARCH_SOURCES
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerAlu.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerConst.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerMove.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/Lower.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerHelper.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerJump.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerObject.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/AnalysisO1.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/BytecodeVisitor.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/NcgAot.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/CodegenInterface.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerInvoke.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerReturn.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/NcgHelper.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/LowerGetPut.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/libenc/enc_base.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/libenc/dec_base.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/libenc/enc_wrapper.cpp
                    ${DVM_SRC_DIR}/compiler/codegen/x86/libenc/enc_tabl.cpp
            )
        endif ()
    endif ()
else ()
    list(APPEND DVM_COMPILE_DEFINITIONS
            dvmAsmInstructionStart=0
            dvmAsmInstructionEnd=0
            dvmAsmSisterStart=0
            dvmAsmSisterEnd=0
            DVM_NO_ASM_INTERP=1
    )
    list(APPEND DVM_ARCH_SOURCES
            ${DVM_SRC_DIR}/arch/generic/Call.cpp
            ${DVM_SRC_DIR}/arch/generic/Hints.cpp
            ${DVM_SRC_DIR}/mterp/out/InterpC-allstubs.cpp
    )
endif ()

function(add_dvm_library TARGET_NAME)

    add_library(${TARGET_NAME} SHARED
            ${DVM_COMMON_SOURCES}
            ${DVM_ARCH_SOURCES}
    )

    target_include_directories(${TARGET_NAME} PRIVATE ${DVM_INCLUDE_DIRS})
    target_compile_definitions(${TARGET_NAME} PRIVATE ${DVM_COMPILE_DEFINITIONS})
    target_compile_options(${TARGET_NAME} PRIVATE ${DVM_COMPILE_OPTIONS})

    target_link_libraries(${TARGET_NAME}
            dl
            nativehelper
            z
            dex
            ffi
    )

    if (DVM_OS STREQUAL "Linux")
        target_link_libraries(${TARGET_NAME} pthread rt)
    else ()
        target_link_libraries(${TARGET_NAME} pthread)
    endif ()
endfunction()

add_dvm_library(dvm)

if (WITH_DALVIK_ASSERT)
    add_dvm_library(dvm_assert)
endif ()

if (WITH_SELF_VERIFICATION AND NOT DVM_ARCH MATCHES "mips")
    add_dvm_library(dvm_sv)
endif ()

add_library(dvm_interp SHARED
        ${DVM_COMMON_SOURCES}
        ${DVM_ARCH_SOURCES}
)

target_include_directories(dvm_interp PRIVATE ${DVM_INCLUDE_DIRS})
target_compile_definitions(dvm_interp PRIVATE ${DVM_COMPILE_DEFINITIONS})
target_compile_options(dvm_interp PRIVATE ${DVM_COMPILE_OPTIONS})
target_compile_definitions(dvm_interp PRIVATE -DWITH_JIT=FALSE)

target_link_libraries(dvm_interp
        # corkscrew
        cutils
        dl
        log
        nativehelper
        z
        stlport
        dex
)

if (DVM_OS STREQUAL "Linux")
    target_link_libraries(dvm_interp pthread rt)
else ()
    target_link_libraries(dvm_interp pthread)
endif ()
