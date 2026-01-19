cmake_minimum_required(VERSION 3.16)

set(_icu4c_common_src
        cmemory.c cstring.c
        cwchar.c locmap.c
        punycode.cpp putil.cpp
        uarrsort.c ubidi.c
        ubidiln.c ubidi_props.c
        ubidiwrt.c ucase.cpp
        ucasemap.cpp ucat.c
        uchar.c ucln_cmn.c
        ucmndata.c
        ucnv2022.cpp ucnv_bld.cpp
        ucnvbocu.cpp ucnv.c
        ucnv_cb.c ucnv_cnv.c
        ucnvdisp.c ucnv_err.c
        ucnv_ext.cpp ucnvhz.c
        ucnv_io.cpp ucnvisci.c
        ucnvlat1.c ucnv_lmb.c
        ucnvmbcs.c ucnvscsu.c
        ucnv_set.c ucnv_u16.c
        ucnv_u32.c ucnv_u7.c
        ucnv_u8.c
        udatamem.c
        udataswp.c uenum.c
        uhash.c uinit.c
        uinvchar.c uloc.cpp
        umapfile.c umath.c
        umutex.cpp unames.cpp
        unorm_it.c uresbund.cpp
        ures_cnv.c uresdata.c
        usc_impl.c uscript.c
        uscript_props.cpp
        ushape.cpp ustrcase.cpp
        ustr_cnv.c ustrfmt.c
        ustring.cpp ustrtrns.cpp
        ustr_wcs.cpp utf_impl.c
        utrace.c utrie.cpp
        utypes.c wintz.c
        utrie2_builder.cpp icuplug.c
        propsvec.c ulist.c
        uloc_tag.c ucnv_ct.c

        bmpset.cpp unisetspan.cpp
        brkeng.cpp brkiter.cpp
        caniter.cpp chariter.cpp
        dictbe.cpp locbased.cpp
        locid.cpp locutil.cpp
        normlzr.cpp parsepos.cpp
        propname.cpp rbbi.cpp
        rbbidata.cpp rbbinode.cpp
        rbbirb.cpp rbbiscan.cpp
        rbbisetb.cpp rbbistbl.cpp
        rbbitblb.cpp resbund_cnv.cpp
        resbund.cpp ruleiter.cpp
        schriter.cpp serv.cpp
        servlk.cpp servlkf.cpp
        servls.cpp servnotf.cpp
        servrbf.cpp servslkf.cpp
        ubrk.cpp
        uchriter.cpp uhash_us.cpp
        uidna.cpp uiter.cpp
        unifilt.cpp unifunct.cpp
        uniset.cpp uniset_props.cpp
        unistr_case.cpp unistr_cnv.cpp
        unistr.cpp unistr_props.cpp
        unormcmp.cpp unorm.cpp
        uobject.cpp uset.cpp
        usetiter.cpp uset_props.cpp
        usprep.cpp ustack.cpp
        ustrenum.cpp utext.cpp
        util.cpp util_props.cpp
        uvector.cpp uvectr32.cpp
        errorcode.cpp
        bytestream.cpp stringpiece.cpp
        mutex.cpp dtintrv.cpp
        ucnvsel.cpp uvectr64.cpp
        locavailable.cpp locdispnames.cpp
        loclikely.cpp locresdata.cpp
        normalizer2impl.cpp normalizer2.cpp
        filterednormalizer2.cpp ucol_swp.cpp
        uprops.cpp utrie2.cpp
        charstr.cpp uts46.cpp
        udata.cpp appendable.cpp bytestrie.cpp
        bytestriebuilder.cpp bytestrieiterator.cpp
        messagepattern.cpp patternprops.cpp stringtriebuilder.cpp
        ucharstrie.cpp ucharstriebuilder.cpp ucharstrieiterator.cpp
        dictionarydata.cpp
        ustrcase_locale.cpp unistr_titlecase_brkiter.cpp
        uniset_closure.cpp ucasemap_titlecase_brkiter.cpp
        ustr_titlecase_brkiter.cpp unistr_case_locale.cpp
        ../stubdata/stubdata.c
)

set(_icu4c_common_private_definitions
        ICU_DATA_DIR_PREFIX_ENV_VAR=\"ANDROID_ROOT\"
        ICU_DATA_DIR=\"/usr/icu\"
        U_HAVE_NL_LANGINFO_CODESET=0
        U_TIMEZONE=timezone
        _REENTRANT
        U_COMMON_IMPLEMENTATION
)

set(_icu4c_common_cflags
        -O3
        -fvisibility=hidden
)

if (ICU4C_BUILD_SHARED)
    add_library(icuuc SHARED ${_icu4c_common_src} $<TARGET_OBJECTS:icu_stubdata_obj>)
else ()
    add_library(icuuc STATIC ${_icu4c_common_src} $<TARGET_OBJECTS:icu_stubdata_obj>)
endif ()

set_target_properties(icuuc PROPERTIES OUTPUT_NAME icuuc)
set_property(TARGET icuuc PROPERTY POSITION_INDEPENDENT_CODE ON)

target_compile_definitions(icuuc PRIVATE ${_icu4c_common_private_definitions})
target_compile_options(icuuc PRIVATE ${_icu4c_common_cflags})

target_include_directories(icuuc
        PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}"
        "${CMAKE_CURRENT_SOURCE_DIR}/../i18n"
)

find_package(Threads REQUIRED)

target_link_libraries(icuuc
        PRIVATE
        Threads::Threads
        dl
        m
)

add_dependencies(icuuc icu-data)

install(TARGETS icuuc
        LIBRARY
        DESTINATION "${INSTALL_DIR}/lib"
)
