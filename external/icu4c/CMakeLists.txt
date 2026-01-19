cmake_minimum_required(VERSION 3.16)

project(icu4c LANGUAGES C CXX)

option(ICU4C_BUILD_SHARED "Build ICU libraries as shared libraries" ON)
option(ICU4C_INSTALL_DATA "Install/copy ICU .dat data file" ON)

add_subdirectory(stubdata)
add_subdirectory(common)
add_subdirectory(i18n)
