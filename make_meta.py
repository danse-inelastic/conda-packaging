#!/usr/bin/env python

name = "${PKG_NAME}"
version = "${VERSION}"
git_revision = "${GIT_RELEASE_TAG}" or ('v'+version)
git_clone_url = "${GITHUB_URL}.git"

build_deps = "${CONDA_PKGING_BUILD_DEPS}".split()
build_deps.append('cmake')
run_deps = "${CONDA_PKGING_RUN_DEPS}".split()

build_requirements = '\n'.join("    - %s" % d for d in build_deps)
run_requirements = '\n'.join("    - %s" % d for d in run_deps)

import_test = "${PKG_NAME}"
test_script = "${CONDA_TEST_SCRIPT}"
home_url = "${HOME_URL}"

template = open("meta.yaml.template").read()
content = template % locals()
open("meta.yaml", 'wt').write(content)
