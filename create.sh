#!/bin/bash

DEFAULT_PROJECT_FOLDER=$HOME/PythonProjects
COMMAND=$1 
PROJECT_NAME=$2
PROJECT_ROOT=$DEFAULT_PROJECT_FOLDER/$PROJECT_NAME
CURRENT_YEAR=$(date +"%Y")


function create() {
	# create default project-folder if it doesn't exist
	if ! [ -d $DEFAULT_PROJECT_FOLDER ] 
	then
		create_default_project_folder
	fi

	create_project_folder
	create_project_files_and_folders
}

function create_default_project_folder() {
	echo "Creating default project-folder... "
	mkdir $DEFAULT_PROJECT_FOLDER
}

function create_project_folder() {
	if ! [ -d $PROJECT_ROOT ]
	then
		echo "Creating project-folder... "
		mkdir $PROJECT_ROOT
	else
		printf "\n\n\n"
		echo "PROJECT_ROOT already exists!"
		exit 1
	fi
}

function create_project_files_and_folders() {
	echo "Creating project files and folders... "
	create_readme	
	create_license
	create_setup_py
	create_settings_py
	create_requirements_txt
	create_main_module
	create_tests_package
	create_makefile
	create_gitignore

	git_init_commit
}

function create_readme() {
	echo "Creating README.md... "
	touch $PROJECT_ROOT/README.md
	echo "# $PROJECT_NAME" > $PROJECT_ROOT/README.md
}

function create_license() {
	echo "Creating LICENSE... "
	touch $PROJECT_ROOT/LICENSE
	echo "MIT License

Copyright (c) $CURRENT_YEAR $USER

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
SOFTWARE." > $PROJECT_ROOT/LICENSE
}

function create_setup_py() {
	echo "Creating setup.py... "
	touch $PROJECT_ROOT/setup.py
	echo "from setuptools import setup, find_packages

with open(\"README.md\", \"r\") as file_handler:
    long_description = file_handler.read()

setup(
    name=\"$PROJECT_NAME\",
    version=\"0.0.1\",
    author=\"$USER\",
    long_description=long_description,
    long_description_content_type=\"text/markdown\",
    packages=find_packages(),
    classifiers=[
        \"Programming Language :: Python :: 3\",
        \"License :: OSI Approved :: MIT License\",
    ],
)
" > $PROJECT_ROOT/setup.py
}

function create_settings_py() {
	echo "Creating settings.py... "
	touch $PROJECT_ROOT/settings.py
	echo "import os

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
" > $PROJECT_ROOT/settings.py

	touch $PROJECT_ROOT/.env $PROJECT_ROOT/.env.dev
}

function create_requirements_txt() {
	echo "Creating requirements.txt... "
	touch $PROJECT_ROOT/requirements.txt
}

function create_main_module() {
	echo "Creating $PROJECT_NAME.py... "
	touch $PROJECT_ROOT/$PROJECT_NAME.py
	echo "def main():
    return \"hello, world\"

if __name__ == \"__main__\":
    main()
" > $PROJECT_ROOT/$PROJECT_NAME.py
}

function create_tests_package() {
	echo "Creating test_packages... "
	mkdir $PROJECT_ROOT/tests
	touch $PROJECT_ROOT/tests/test_main.py
	echo "import unittest
import context
import $PROJECT_NAME


class Test$PROJECT_NAME(unittest.TestCase):
    def test_$PROJECT_NAME(self):
        self.assertEqual($PROJECT_NAME.main(), \"hello, world\")


if __name__ == \"__main__\":
    unittest.main()
" > $PROJECT_ROOT/tests/test_main.py

	touch $PROJECT_ROOT/tests/context.py
	echo "\"\"\" Fixing the import path for importing modules from root \"\"\"

import os, sys
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)" > $PROJECT_ROOT/tests/context.py 
}

function create_makefile() {
	echo "Creating Makefile... "
	touch $PROJECT_ROOT/Makefile
	echo "
test:
	python3 tests/test_main.py" > $PROJECT_ROOT/Makefile	
}

function create_gitignore() {
	echo "Creating gitignore... "
	touch $PROJECT_ROOT/.gitignore
	echo "# vim files
*.swp
*.swo

# python cache
__pycache__/

# prod-files
.env" > $PROJECT_ROOT/.gitignore
}

function git_init_commit() {
	git init && git commit -am "initial commit"
}

create











