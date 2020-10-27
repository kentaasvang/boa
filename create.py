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


def create_file(file_path, file_name, file_content):
    print("Creating ", file_name, "...")
    file = open(file_path + "/" + file_name, "w")
    file.write(file_content + "\n")
    file.close()

def create_project_folder():
    print(project_root)
    if not path.isdir(project_root):
        print("Creating project folder...")
        os.mkdir(project_root)

def create_project_files_and_folders():
    print("Creating project files and folders...")
    # Create README.md
    create_file(project_root, "README.md", "# " + project_name)
    # Create LICENSE
    create_file(project_root, "LICENSE", LICENSE)
    # Create setup.py
    create_file(project_root, "setup.py", SETUP)
    # Create settings.py
    create_file(project_root, "settings.py", SETTINGS)
    # Create .env and .env.dev
    create_file(project_root, ".env", "")
    create_file(project_root, ".env.dev", "")
    # Create requirements.txt
    create_file(project_root, "requirements.txt", "")
    # Create main_module
    create_file(project_root, project_name + '.py', MAIN)
    # Create test packages
    os.mkdir(project_root + "/tests")
    create_file(project_root + "/tests", "test_main.py", TEST)
    # context.py
    create_file(project_root + "/tests", "context.py", CONTEXT)
    # Create Makefile
    create_file(project_root, "Makefile", "test:\n\tpython3 tests/test_main.py")
    # Create gitignore
    create_file(project_root, ".gitignore", "# vim files\n*.swp\n*.swo\n# python cache\n__pycache__/\n# prod-files\n.env") 

def git_initial_commit():
    print("git init and commit!...")
    os.system("git init --quiet && git add . && git commit --quiet -m \"initial commit\"");

def create():
    if not path.isdir(default_project_dir):
        print("Creating default project folder...")
        os.mkdir(default_project_dir)

    create_project_folder()
    create_project_files_and_folders()


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


class File:
    name: str
    content: str


if __name__ == "__main__":
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

    CONTEXT = templates.CONTEXT
    

    create()

