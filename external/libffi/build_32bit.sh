#!/bin/bash

set -e

FFI_DIR="/mnt/d/02_project/AOSP-4.4.4-r2.0.1/external/libffi"
BUILD_DIR="${FFI_DIR}/build_32bit"
INSTALL_DIR="${FFI_DIR}/install_32bit"

echo "Building 32-bit libffi..."
echo "Source: ${FFI_DIR}"
echo "Build:  ${BUILD_DIR}"
echo "Install: ${INSTALL_DIR}"

mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"

export CC="gcc -m32"
export CXX="g++ -m32"
export CFLAGS="-m32 -O2"
export CXXFLAGS="-m32 -O2"
export LDFLAGS="-m32"

"${FFI_DIR}/configure" \
    --host=i686-linux-gnu \
    --prefix="${INSTALL_DIR}" \
    --disable-shared \
    --enable-static

make -j$(nproc)
make install

echo ""
echo "32-bit libffi built successfully!"
echo "Static library: ${INSTALL_DIR}/lib/libffi.a"
echo "Headers: ${INSTALL_DIR}/include"
