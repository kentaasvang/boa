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
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE." > $PROJECT_ROOT/LICENSE
}


create
