cmake_minimum_required(VERSION 3.10)
project(libcore_native C CXX)

add_library(javacore SHARED
        ${CMAKE_CURRENT_SOURCE_DIR}/dalvik/src/main/native/org_apache_harmony_dalvik_NativeTestTarget.cpp

        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/AsynchronousSocketCloseMonitor.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/ExecStrings.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/IcuUtilities.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/JniException.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/NetworkUtilities.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/Register.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/ZipUtilities.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/cbigint.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_io_Console.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_io_File.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_io_ObjectStreamClass.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_Character.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_Double.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_Float.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_Math.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_ProcessManager.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_RealToString.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_StrictMath.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_StringToReal.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_lang_System.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_math_NativeBN.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_nio_ByteOrder.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_nio_charset_Charsets.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_text_Bidi.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_util_regex_Matcher.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_util_regex_Pattern.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_util_zip_Adler32.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_util_zip_CRC32.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_util_zip_Deflater.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/java_util_zip_Inflater.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_AlphabeticIndex.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_DateIntervalFormat.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_ICU.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativeBreakIterator.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativeCollation.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativeConverter.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativeDecimalFormat.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativeIDN.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativeNormalizer.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_NativePluralRules.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_TimeZoneNames.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_icu_Transliterator.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_io_AsynchronousCloseMonitor.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_io_Memory.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_io_OsConstants.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_io_Posix.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/libcore_net_RawSocket.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/org_apache_harmony_xml_ExpatParser.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/readlink.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/realpath.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/sun_misc_Unsafe.cpp
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native/valueOf.cpp
)

set_target_properties(javacore PROPERTIES OUTPUT_NAME javacore)

target_include_directories(javacore
        PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        ${CMAKE_CURRENT_SOURCE_DIR}/luni/src/main/native
        ${CMAKE_CURRENT_SOURCE_DIR}/../external/icu4c/common
        ${CMAKE_CURRENT_SOURCE_DIR}/../external/icu4c/i18n
        ${CMAKE_CURRENT_SOURCE_DIR}/../external/openssl/include
        ${CMAKE_CURRENT_SOURCE_DIR}/../external/zlib
        ${CMAKE_CURRENT_SOURCE_DIR}/../external/expat/lib
)

# target_compile_options(javacore PRIVATE -Wall -Wextra -Werror)

if (NOT CMAKE_CXX_STANDARD)
    set_target_properties(javacore PROPERTIES CXX_STANDARD 11)
endif ()

target_link_libraries(javacore
        PRIVATE
        nativehelper
        z
        fdlibm
#        crypto
#        expat
#        icuuc
#        icui18n
)



target_compile_definitions(javacore PRIVATE OS_SHARED_LIB_FORMAT_STR="lib%s.so")

if (ANDROID_BUILD)
    target_link_libraries(javacore PRIVATE log)
else ()
    target_link_libraries(javacore PRIVATE dl pthread rt)
endif ()
