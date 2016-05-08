#!/usr/bin/env bash

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DDEPLOYMENT_PREFIX=$PREFIX .. && make && make install
