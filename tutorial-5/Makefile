# Copyright (c) 2023, Mastering Monero

builddir := build
topdir   := ../..

#   cd $(builddir)/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=$(topdir)/cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=$(shell cd ${MINGW_PREFIX}/.. && pwd -W) $(topdir) && $(MAKE)

tutorial-5:
	mkdir -p $(builddir)/release
	cd $(builddir)/release && cmake -G "MSYS Makefiles" -D STATIC=ON -D ARCH="x86-64" -D BUILD_64=ON -D CMAKE_BUILD_TYPE=Release -D BUILD_TAG="win-x64" -D CMAKE_TOOLCHAIN_FILE=$(topdir)/../../monero/cmake/64-bit-toolchain.cmake -D MSYS2_FOLDER=$(shell cd ${MINGW_PREFIX}/.. && pwd -W) $(topdir) && $(MAKE)

fuzz:
	mkdir -p $(builddir)/fuzz
	cd $(builddir)/fuzz && cmake -D STATIC=ON -D SANITIZE=ON -D BUILD_TESTS=ON -D USE_LTO=OFF -D CMAKE_C_COMPILER=afl-gcc -D CMAKE_CXX_COMPILER=afl-g++ -D ARCH="x86-64" -D CMAKE_BUILD_TYPE=fuzz -D BUILD_TAG="linux-x64" $(topdir) && $(MAKE)

clean-build-dir:
	@echo "WARNING: Back-up your wallet if it exists within ./build!" ; \
	read -r -p "This will destroy all build directories, continue (y/N)?: " CONTINUE; \
	[ $$CONTINUE = "y" ] || [ $$CONTINUE = "Y" ] || (echo "Exiting."; exit 1;)
	rm -rf ./build

tags:
	ctags -R --sort=1 --c++-kinds=+p --fields=+iaS --extra=+q --language-force=C++ src contrib tests/gtest

.PHONY: all cmake-debug debug debug-test debug-all cmake-release release release-test release-all clean tags
