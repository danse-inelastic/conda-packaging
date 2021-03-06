# docker 

IF( "${CONDA_BUILD_MAKE_CMD}" STREQUAL "")
  set(CONDA_BUILD_MAKE_CMD "cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DDEPLOYMENT_PREFIX=$PREFIX .. && make -j $CORES && make install")
ENDIF()

configure_file(make_meta.py make_meta.py)
configure_file(meta.yaml.template meta.yaml.template)
configure_file(bld.bat bld.bat)
configure_file(build.sh build.sh)

add_custom_command(
  OUTPUT meta.yaml
  COMMAND python make_meta.py
  DEPENDS make_meta.py meta.yaml.template
  )

# this will build the conda package
# remember to set anaconda automatic upload so any build
# will be uploaded to anaconda
# $ conda config --set anaconda_upload yes
# See http://conda.pydata.org/docs/build_tutorials/pkgs2.html
add_custom_target( 
  conda-build-pkg
  COMMAND conda build .
  WORKING_DIRECTORY .
  DEPENDS meta.yaml
  )
