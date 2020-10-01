#!/usr/bin/env python3

from os.path import expanduser
from os import path, mkdir
import os
import sys
import datetime
import getpass

default_project_dir = expanduser("~") + "/PythonProjects"
command = sys.argv[1]
project_name = sys.argv[2]
project_root = default_project_dir + "/" + project_name
current_year = datetime.datetime.now().year
current_user = getpass.getuser()

LICENSE_CONTENT = """MIT License

Copyright (c) {} {}
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the \"Software\"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""".format(current_year, current_user)

SETUP_CONTENT =	"""from setuptools import setup, find_packages

with open(\"README.md\", \"r\") as file_handler:
    long_description = file_handler.read()

setup(
    name=\"{}\",
    version=\"0.0.1\",
    author=\"{}\",
    long_description=long_description,
    long_description_content_type=\"text/markdown\",
    packages=find_packages(),
    classifiers=[
        \"Programming Language :: Python :: 3\",
        \"License :: OSI Approved :: MIT License\",
    ],
)\n""".format(project_name, current_user)


SETTINGS_CONTENT = """import os

DEVELOPMENT = True


filename = \".env.dev\" if DEVELOPMENT else \".env\"

# Read in key/values from environment file and load
# them into the enrironment
try:
    with open(filename, \"r\") as file_handler:
        arguments = []

        # read lines in file and append to arguments-list
        while argument := file_handler.readline():
            arguments.append(argument.split(\"=\"))

        # load key/values into environment so they can be reached with
        # os.getenv()
        for key, value in arguments:
            os.environ[key] = value

except FileNotFoundError as file_not_found:
    print(f\"The file {filename} was not found. Make sure it's created\")

"""

MAIN_CONTENT="""def main():
    return \"hello, world\"

if __name__ == \"__main__\":
    main()
"""

TEST_CONTENT="""import unittest
import context
import {}

class Test{}(unittest.TestCase):
    def test_{}(self):
        self.assertEqual({}.main(), \"hello, world\")

if __name__ == \"__main__\":
    unittest.main()
""".format(project_name, project_name, project_name, project_name, project_root)

CONTEXT_CONTENT="""\"\"\" Fixing the import path for importing modules from root \"\"\"

import os, sys
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)
"""



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
    create_file(project_root, "LICENSE", LICENSE_CONTENT)
    # Create setup.py
    create_file(project_root, "setup.py", SETUP_CONTENT)
    # Create settings.py
    create_file(project_root, "settings.py", SETTINGS_CONTENT)
    # Create .env and .env.dev
    create_file(project_root, ".env", "")
    create_file(project_root, ".env.dev", "")
    # Create requirements.txt
    create_file(project_root, "requirements.txt", "")
    # Create main_module
    create_file(project_root, project_name + '.py', MAIN_CONTENT)
    # Create test packages
    os.mkdir(project_root + "/tests")
    create_file(project_root + "/tests", "test_main.py", TEST_CONTENT)
    # context.py
    create_file(project_root + "/tests", "context.py", CONTEXT_CONTENT)
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


create()
