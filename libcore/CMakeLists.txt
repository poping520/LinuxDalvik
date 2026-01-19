cmake_minimum_required(VERSION 3.10)
project(libcore_native C CXX)

add_library(javacore SHARED
        dalvik/src/main/native/org_apache_harmony_dalvik_NativeTestTarget.cpp
        luni/src/main/native/AsynchronousSocketCloseMonitor.cpp
        luni/src/main/native/ExecStrings.cpp
        luni/src/main/native/IcuUtilities.cpp
        luni/src/main/native/JniException.cpp
        luni/src/main/native/NetworkUtilities.cpp
        luni/src/main/native/Register.cpp
        luni/src/main/native/ZipUtilities.cpp
        luni/src/main/native/cbigint.cpp
        luni/src/main/native/java_io_Console.cpp
        luni/src/main/native/java_io_File.cpp
        luni/src/main/native/java_io_ObjectStreamClass.cpp
        luni/src/main/native/java_lang_Character.cpp
        luni/src/main/native/java_lang_Double.cpp
        luni/src/main/native/java_lang_Float.cpp
        luni/src/main/native/java_lang_Math.cpp
        luni/src/main/native/java_lang_ProcessManager.cpp
        luni/src/main/native/java_lang_RealToString.cpp
        luni/src/main/native/java_lang_StrictMath.cpp
        luni/src/main/native/java_lang_StringToReal.cpp
        luni/src/main/native/java_lang_System.cpp
        luni/src/main/native/java_math_NativeBN.cpp
        luni/src/main/native/java_nio_ByteOrder.cpp
        luni/src/main/native/java_nio_charset_Charsets.cpp
        luni/src/main/native/java_text_Bidi.cpp
        luni/src/main/native/java_util_regex_Matcher.cpp
        luni/src/main/native/java_util_regex_Pattern.cpp
        luni/src/main/native/java_util_zip_Adler32.cpp
        luni/src/main/native/java_util_zip_CRC32.cpp
        luni/src/main/native/java_util_zip_Deflater.cpp
        luni/src/main/native/java_util_zip_Inflater.cpp
        luni/src/main/native/libcore_icu_AlphabeticIndex.cpp
        luni/src/main/native/libcore_icu_DateIntervalFormat.cpp
        luni/src/main/native/libcore_icu_ICU.cpp
        luni/src/main/native/libcore_icu_NativeBreakIterator.cpp
        luni/src/main/native/libcore_icu_NativeCollation.cpp
        luni/src/main/native/libcore_icu_NativeConverter.cpp
        luni/src/main/native/libcore_icu_NativeDecimalFormat.cpp
        luni/src/main/native/libcore_icu_NativeIDN.cpp
        luni/src/main/native/libcore_icu_NativeNormalizer.cpp
        luni/src/main/native/libcore_icu_NativePluralRules.cpp
        luni/src/main/native/libcore_icu_TimeZoneNames.cpp
        luni/src/main/native/libcore_icu_Transliterator.cpp
        luni/src/main/native/libcore_io_AsynchronousCloseMonitor.cpp
        luni/src/main/native/libcore_io_Memory.cpp
        luni/src/main/native/libcore_io_OsConstants.cpp
        luni/src/main/native/libcore_io_Posix.cpp
        luni/src/main/native/libcore_net_RawSocket.cpp
        luni/src/main/native/org_apache_harmony_xml_ExpatParser.cpp
        luni/src/main/native/readlink.cpp
        luni/src/main/native/realpath.cpp
        luni/src/main/native/sun_misc_Unsafe.cpp
        luni/src/main/native/valueOf.cpp
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
        icuuc
        icui18n
#        crypto
#        expat
)



target_compile_definitions(javacore PRIVATE OS_SHARED_LIB_FORMAT_STR="lib%s.so")

if (ANDROID_BUILD)
    target_link_libraries(javacore PRIVATE log)
else ()
    target_link_libraries(javacore PRIVATE dl pthread rt)
endif ()

install(TARGETS javacore
        LIBRARY
        DESTINATION "${INSTALL_DIR}/lib"
)

