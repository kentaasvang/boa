import sys, os
import pytest
from os import path

import boa


TEMPORARY_TEST_DIRECTORY = "root"


def test_default_behaviour(tmpdir):
    test_directory = tmpdir.mkdir(TEMPORARY_TEST_DIRECTORY)
    os.chdir(test_directory)
    project_name = "default_project"
    boa.new(project_name)

    # check that project directory is created
    assert path.isdir(project_name), \
        "folder is missing"

    # check that the projects main module is created
    assert path.isfile(f"{project_name}/{project_name}.py"), \
        "main module is missing"


def test_default_behaviour_with_cwd_as_project_dir(tmpdir):
    test_directory = tmpdir.mkdir(TEMPORARY_TEST_DIRECTORY)
    os.chdir(test_directory)
    project_name = "default_project"
    boa.new(project_name, ".")

    # check that main module is created at cwd
    assert path.isfile(f"{project_name}.py"), \
        "Main module is missing"

