cmake_minimum_required(VERSION 3.16)

project(dx_jar NONE)

find_package(Java REQUIRED)
include(UseJava)

find_program(JAVAC_EXECUTABLE javac REQUIRED)
find_program(JAR_EXECUTABLE jar REQUIRED)

set(DX_SRC_DIR "${CMAKE_CURRENT_LIST_DIR}/src")
set(DX_LIBCORE_DEX_SRC_DIR "${CMAKE_CURRENT_LIST_DIR}/../../libcore/dex/src/main/java")
set(DX_MANIFEST "${CMAKE_CURRENT_LIST_DIR}/etc/manifest.txt")

if(NOT EXISTS "${DX_LIBCORE_DEX_SRC_DIR}")
  message(FATAL_ERROR "Missing libcore dex sources at: ${DX_LIBCORE_DEX_SRC_DIR}")
endif()

file(GLOB_RECURSE DX_JAVA_SOURCES CONFIGURE_DEPENDS
  "${DX_SRC_DIR}/*.java"
  "${DX_LIBCORE_DEX_SRC_DIR}/*.java"
)

if(DX_JAVA_SOURCES STREQUAL "")
  message(FATAL_ERROR "No Java sources found under: ${DX_SRC_DIR} and ${DX_LIBCORE_DEX_SRC_DIR}")
endif()

set(DX_CLASSES_DIR "${CMAKE_CURRENT_BINARY_DIR}/classes")
set(DX_JAR_OUT "${CMAKE_CURRENT_BINARY_DIR}/dx.jar")

set(DX_JAVAC_RELEASE "8" CACHE STRING "javac --release")
set(DX_JAVAC_JVM_OPTS "" CACHE STRING "Extra JVM options passed to javac, e.g. -J-Xmx2g")
option(DX_JAVAC_DEBUG "Emit debug info (-g). Turn OFF to speed up compilation." ON)
set(DX_JAVAC_EXTRA_ARGS "" CACHE STRING "Extra javac args, e.g. -Xlint:-options")

set(DX_JAVAC_JVM_OPTS_LIST "${DX_JAVAC_JVM_OPTS}")
set(DX_JAVAC_EXTRA_ARGS_LIST "${DX_JAVAC_EXTRA_ARGS}")
separate_arguments(DX_JAVAC_JVM_OPTS_LIST)
separate_arguments(DX_JAVAC_EXTRA_ARGS_LIST)

set(DX_JAVAC_DEBUG_FLAG "")
if(DX_JAVAC_DEBUG)
  set(DX_JAVAC_DEBUG_FLAG "-g")
endif()

add_custom_command(
  OUTPUT "${DX_JAR_OUT}"
  COMMAND "${CMAKE_COMMAND}" -E make_directory "${DX_CLASSES_DIR}"
  COMMAND "${JAVAC_EXECUTABLE}"
          ${DX_JAVAC_JVM_OPTS_LIST}
          --release "${DX_JAVAC_RELEASE}"
          -encoding UTF-8
          ${DX_JAVAC_DEBUG_FLAG}
          ${DX_JAVAC_EXTRA_ARGS_LIST}
          -d "${DX_CLASSES_DIR}"
          ${DX_JAVA_SOURCES}
  COMMAND "${JAR_EXECUTABLE}" cfm "${DX_JAR_OUT}" "${DX_MANIFEST}" -C "${DX_CLASSES_DIR}" .
  DEPENDS ${DX_JAVA_SOURCES} "${DX_MANIFEST}"
  WORKING_DIRECTORY "${CMAKE_CURRENT_LIST_DIR}"
  VERBATIM
  COMMAND_EXPAND_LISTS
)

add_custom_target(dx_jar ALL DEPENDS "${DX_JAR_OUT}")

set_property(TARGET dx_jar PROPERTY OUTPUT_NAME "dx")

install(FILES "${DX_JAR_OUT}" DESTINATION ".")
