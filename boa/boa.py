#!/usr/bin/env python3
from os.path import expanduser
from os import path, mkdir
import os
import sys
import datetime
import getpass

from argparse import ArgumentParser
import settings
import templates

from typing import Dict


def create_file(directory: str, name: str, content: str) -> None:
    """
    Creates a file in the given directory and fills with given content
    """
    with open(f"{directory}/{name}", "w") as f:
        f.write(f"{content}\n")


def create_project_folder(project_root: str) -> None:
    """
    Creates the project root folder
    """
    if not path.isdir(project_root):
        os.mkdir(project_root)


def create_project_files_and_folders(root: str, files: Dict[str, str]) -> None:
    """
    Creates all the project files that are needed
    """
    for name, content in files.items():
        create_file(root, name, content)

    # Create Makefile
    create_file(root, "Makefile", "test:\n\tpython3 tests.py")
    # Create gitignore
    create_file(root, ".gitignore", "# vim files\n*.swp\n*.swo\n# python cache\n__pycache__/\n# prod-files\n.env") 


def git_initial_commit() -> None:
    """
    Sets up git in project root
    """
    print("git init and commit!...")
    os.system("git init --quiet && git add . && git commit --quiet -m \"initial commit\"");



def parse_command_line_arguments() -> str:
    """ 
    Parses command line arguments and returns project name 
    """
    parser = ArgumentParser(settings.DESCRIPTION)
    parser.add_argument(
        "name", 
        type=str,
        help="The name of the project"
    )

    return parser.parse_args().name


def template_engine(template: str, data: dict) -> str:
    """
    Takes a template and a dict and insert the values
    in the dict to the corresponding keys in a template

    Example:
        template_engine("hello, (( name ))", {"name": "world"})
        returns: "hello, world" 
    """
    for key, value in data.items():
        template = template.replace(f"(( {key} ))", str(value))
    return template


def boa() -> None:
    """
    Program entrypoint
    """
    default_project_dir = os.getcwd()
    project_name = parse_command_line_arguments()
    project_root = default_project_dir + "/" + project_name
    current_year = datetime.datetime.now().year
    current_user = getpass.getuser()

    LICENSE = template_engine(
        templates.LICENSE, {"name": project_name, "year": current_year})

    SETUP = template_engine(
        templates.SETUP, {"name": project_name, "user": current_user})

    SETTINGS = templates.SETTINGS

    MAIN = templates.MAIN

    TEST = template_engine(templates.TEST, {"name": project_name})

    if not path.isdir(default_project_dir):
        os.mkdir(default_project_dir)

    files = {
        "LICENSE": LICENSE, 
        "setup.py": SETUP, 
        "settings.py": SETTINGS, 
        f"{project_name}.py": MAIN, 
        "tests.py": TEST, 
    }

    create_project_folder(project_name)
    create_project_files_and_folders(project_root, files)

