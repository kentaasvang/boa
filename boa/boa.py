#!/usr/bin/env python3

import os
import datetime
import getpass

from argparse import ArgumentParser
from os import path
from boa import (settings, templates)


def run_make_command(command):
    """
    Runs the method COMMAND in the make.py module if it exists
    """
    try:
        with open("make.py", "r") as file_handler:
            make = file_handler.read()
            exec(make, globals())
            globals()[command]()
    except KeyError as key_error:
        raise KeyError("The command `%s` does not exist in make.py" % command)


def create_file(directory, name, content):
    """
    Creates a file in the given directory and fills with given content
    """
    with open(f"{directory}/{name}", "w") as f:
        f.write(f"{content}")


def create_project_folder(project_root):
    """ 
    Creates the project root folder
    """
    if not path.isdir(project_root):
        os.mkdir(project_root)


def create_project_files_and_folders(root, files):
    """
    Creates all the project files that are needed
    """
    for name, content in files.items():
        create_file(root, name, content)

    # Create Makefile
    create_file(root, "make.py", "import os\n\ndef test():\n\tos.system('python3 tests.py')")
    # Create gitignore
    create_file(
        root, 
        ".gitignore", 
        "# vim files\n*.swp\n*.swo\n# python cache\n__pycache__/\n# prod-files\n.env") 


def git_init(root):
    """
    Sets up git in project root
    """
    os.system(f"git init {root} --quiet")


def parse_command_line_arguments():
    """ 
    Parses command line arguments and returns the project name
    """
    parser = ArgumentParser(settings.DESCRIPTION)
    parser.add_argument(
        "name", 
        type=str,
        help="The name of the project")

    return parser.parse_args().name


def template_engine(template, data):
    """
    Takes a template and a dict and insert the values
    in the dict to the corresponding keys in a template

    Example:
        template_engine("hello, (( name ))", {"name": "world"})
        returns: "hello, world" 
    """
    for key, value in data.items():
        template = template.replace(f"(( {key} ))", str(value))
        template = template.replace(f"(({key}))", str(value))
    return template


def new(p_name, test, p_root):
    """
    Program entrypoint

    Note:
        All parameters in this function are the result of a quick
        hack to be able to run tests. Should be refactored in the future
    """

    # This if-statement is a quick hack to be able to run 
    # a test on the boa-function
    if test:
        assert p_name
        assert p_root != ""

        default_project_dir = p_root
        project_name = p_name
        project_root = default_project_dir / p_name
    elif p_name:
        default_project_dir = os.getcwd()
        project_name = p_name
        project_root = default_project_dir + "/" + project_name
    else:
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
        "LICENSE":            LICENSE, 
        "setup.py":           SETUP, 
        "settings.py":        SETTINGS, 
        f"{project_name}.py": MAIN, 
        "tests.py":           TEST, 
    }
   
    # This if-statement is a quick hack to be able to run 
    # a test on the boa-function
    if test:
        create_project_folder(project_root)
    else:
        create_project_folder(project_name)

    create_project_files_and_folders(project_root, files)
    git_init(project_root)

