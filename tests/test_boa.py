import sys, os
import pytest
from os import path

import boa

from pathlib import Path


TEMPORARY_TEST_DIRECTORY = "root"


def test_default_behaviour(tmpdir):
    test_directory = tmpdir.mkdir(TEMPORARY_TEST_DIRECTORY)
    os.chdir(test_directory)
    project_name = "default_project"
    boa.new(project_name)

    # check that git is initialized
    assert _find_git_folder(project_name), ".git folder is missing"

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


def test_git_init(tmpdir):
    test_directory = tmpdir.mkdir(TEMPORARY_TEST_DIRECTORY)
    os.chdir(test_directory)
    boa._git_init(test_directory)

    assert _find_git_folder(test_directory), ".git folder is missing"


def _find_git_folder(folder):
    return True if path.isdir(folder + "/.git") else False


def test_new_gitignore_cwd(tmpdir):
    # check that function creates a .gitignore file in cwd
    test_directory = tmpdir.mkdir(TEMPORARY_TEST_DIRECTORY)
    os.chdir(test_directory)
    boa.gitignore()

    assert path.isfile(test_directory + "/.gitignore"), \
        ".gitignore file is missing"


def test_new_gitignore_in_specified_path(tmpdir):
    # check that function creates a .gitignore file in specified path
    test_directory = tmpdir.mkdir(TEMPORARY_TEST_DIRECTORY)
    os.chdir(test_directory)

    # folder to initialize git in
    new_folder = Path("new_folder")
    new_folder = Path(test_directory) / new_folder
    new_folder.mkdir()

    boa.gitignore(new_folder)

    assert path.isfile(test_directory + "/new_folder/.gitignore"), \
        ".gitignore file is missing"
