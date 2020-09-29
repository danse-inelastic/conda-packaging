# conda-packaging
This was used by danse.ins packages to create conda packages. 
Recently the danse.ins packages are mostly built using recipes in https://github.com/mcvine/conda-recipes/tree/master/danse instead.

A danse.ins package will need to modify CMakeLists.txt to
first obtain the danse-inelastic/cmake_utils:

# get cmake_utils
IF(EXISTS "cmake_utils/")
  execute_process(
    COMMAND git pull
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/cmake_utils
    )
ELSE(EXISTS "cmake_utils/")
  execute_process(
    COMMAND git clone https://github.com/danse-inelastic/cmake_utils
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )
ENDIF(EXISTS "cmake_utils/")
set(CMAKE_MODULE_PATH ${PROJECT_BINARY_DIR}/cmake_utils)

and then include the conda tools:
include(conda)

Also one must make sure to define some cmake variables.
For example, for the danse.ins package, we need:

set (HOMEPAGE "https://github.com/danse-inelastic/danse.ins")
set (CONDA_PKGING_BUILD_DEPS "python")
set (CONDA_PKGING_RUN_DEPS "python")
