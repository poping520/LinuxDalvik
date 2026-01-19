cmake_minimum_required(VERSION 3.16)

set(_icu4c_stubdata_dir "${CMAKE_CURRENT_SOURCE_DIR}")

file(GLOB _icu4c_all_dat_files RELATIVE "${_icu4c_stubdata_dir}" "${_icu4c_stubdata_dir}/*-all.dat")

if (_icu4c_all_dat_files)
    list(GET _icu4c_all_dat_files 0 _icu4c_all_dat_file)
    get_filename_component(_icu4c_all_dat_file_name "${_icu4c_all_dat_file}" NAME)
    string(REGEX REPLACE "-all\\.dat$" "" ICU4C_DATA_ROOT "${_icu4c_all_dat_file_name}")
else ()
    set(ICU4C_DATA_ROOT "")
endif ()

set(ICU4C_DATA_ALL_DAT "${_icu4c_stubdata_dir}/${ICU4C_DATA_ROOT}-all.dat")
set(ICU4C_DATA_OUTPUT "${CMAKE_BINARY_DIR}/usr/icu/${ICU4C_DATA_ROOT}.dat")

add_library(icu_stubdata_obj OBJECT stubdata.c)
set_property(TARGET icu_stubdata_obj PROPERTY POSITION_INDEPENDENT_CODE ON)

target_include_directories(icu_stubdata_obj PUBLIC "${_icu4c_stubdata_dir}")

add_custom_target(icu-data)

if (ICU4C_INSTALL_DATA AND ICU4C_DATA_ROOT)
    add_custom_command(
            TARGET icu-data
            COMMAND ${CMAKE_COMMAND} -E make_directory "${CMAKE_BINARY_DIR}/usr/icu"
            COMMAND ${CMAKE_COMMAND} -E copy_if_different "${ICU4C_DATA_ALL_DAT}" "${ICU4C_DATA_OUTPUT}"
            BYPRODUCTS "${ICU4C_DATA_OUTPUT}"
            VERBATIM
    )

    install(
            FILES "${ICU4C_DATA_ALL_DAT}"
            DESTINATION "${INSTALL_DIR}/usr/icu"
            RENAME "${ICU4C_DATA_ROOT}.dat"
    )
endif ()
