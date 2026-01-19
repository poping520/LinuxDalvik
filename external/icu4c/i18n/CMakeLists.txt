cmake_minimum_required(VERSION 3.16)

set(_icu4c_i18n_src
        ucln_in.c decContext.c
        ulocdata.c utmscale.c decNumber.c

        indiancal.cpp dtptngen.cpp dtrule.cpp
        persncal.cpp rbtz.cpp reldtfmt.cpp
        taiwncal.cpp tzrule.cpp tztrans.cpp
        udatpg.cpp vtzone.cpp
        anytrans.cpp astro.cpp buddhcal.cpp
        basictz.cpp calendar.cpp casetrn.cpp
        choicfmt.cpp coleitr.cpp coll.cpp
        compactdecimalformat.cpp
        cpdtrans.cpp csdetect.cpp csmatch.cpp
        csr2022.cpp csrecog.cpp csrmbcs.cpp
        csrsbcs.cpp csrucode.cpp csrutf8.cpp
        curramt.cpp currfmt.cpp currunit.cpp
        dangical.cpp
        datefmt.cpp dcfmtsym.cpp decimfmt.cpp
        digitlst.cpp dtfmtsym.cpp esctrn.cpp
        fmtable_cnv.cpp fmtable.cpp format.cpp
        funcrepl.cpp gender.cpp
        gregocal.cpp gregoimp.cpp
        hebrwcal.cpp identifier_info.cpp
        inputext.cpp islamcal.cpp
        japancal.cpp measfmt.cpp measure.cpp
        msgfmt.cpp name2uni.cpp nfrs.cpp
        nfrule.cpp nfsubs.cpp nortrans.cpp
        nultrans.cpp numfmt.cpp olsontz.cpp
        quant.cpp rbnf.cpp rbt.cpp
        rbt_data.cpp rbt_pars.cpp rbt_rule.cpp
        rbt_set.cpp regexcmp.cpp regexst.cpp
        regeximp.cpp region.cpp
        rematch.cpp remtrans.cpp repattrn.cpp
        scriptset.cpp
        search.cpp simpletz.cpp smpdtfmt.cpp
        sortkey.cpp strmatch.cpp strrepl.cpp
        stsearch.cpp tblcoll.cpp timezone.cpp
        titletrn.cpp tolowtrn.cpp toupptrn.cpp
        translit.cpp transreg.cpp tridpars.cpp
        ucal.cpp ucol_bld.cpp ucol_cnt.cpp
        ucol.cpp ucoleitr.cpp ucol_elm.cpp
        ucol_res.cpp ucol_sit.cpp ucol_tok.cpp
        ucsdet.cpp ucurr.cpp udat.cpp
        umsg.cpp unesctrn.cpp uni2name.cpp
        unum.cpp uregexc.cpp uregex.cpp
        usearch.cpp utrans.cpp windtfmt.cpp
        winnmfmt.cpp zonemeta.cpp
        numsys.cpp chnsecal.cpp
        cecal.cpp coptccal.cpp ethpccal.cpp
        brktrans.cpp wintzimpl.cpp plurrule.cpp
        plurfmt.cpp dtitvfmt.cpp dtitvinf.cpp
        tmunit.cpp tmutamt.cpp tmutfmt.cpp
        currpinf.cpp uspoof.cpp uspoof_impl.cpp
        uspoof_build.cpp
        regextxt.cpp selfmt.cpp uspoof_conf.cpp
        uspoof_wsconf.cpp ztrans.cpp zrule.cpp
        vzone.cpp fphdlimp.cpp fpositer.cpp
        locdspnm.cpp ucol_wgt.cpp
        alphaindex.cpp bocsu.cpp decfmtst.cpp
        smpdtfst.cpp tzfmt.cpp
        tzgnames.cpp tznames.cpp tznames_impl.cpp
        udateintervalformat.cpp upluralrules.cpp
)

set(_icu4c_i18n_private_definitions
        _REENTRANT
        U_I18N_IMPLEMENTATION
)

set(_icu4c_i18n_cflags
        -O3
        -fvisibility=hidden
)

if (ICU4C_BUILD_SHARED)
    add_library(icui18n SHARED ${_icu4c_i18n_src})
else ()
    add_library(icui18n STATIC ${_icu4c_i18n_src})
endif ()

set_target_properties(icui18n PROPERTIES OUTPUT_NAME icui18n)
set_property(TARGET icui18n PROPERTY POSITION_INDEPENDENT_CODE ON)

target_compile_definitions(icui18n PRIVATE ${_icu4c_i18n_private_definitions})
target_compile_options(icui18n PRIVATE ${_icu4c_i18n_cflags})

target_include_directories(icui18n
        PUBLIC
        "${CMAKE_CURRENT_SOURCE_DIR}"
        "${CMAKE_CURRENT_SOURCE_DIR}/../common"
)

find_package(Threads REQUIRED)

target_link_libraries(icui18n
        PRIVATE
        icuuc
        Threads::Threads
        m
)

install(TARGETS icui18n
        LIBRARY
        DESTINATION "${INSTALL_DIR}/lib"
)
