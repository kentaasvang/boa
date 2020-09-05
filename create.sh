#!/bin/bash

DEFAULT_PROJECT_FOLDER=$HOME/PythonProjects

COMMAND=$1
PROJECT_NAME=$2
PROJECT_ROOT=$DEFAULT_PROJECT_FOLDER/$PROJECT_NAME


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
}

function create_readme() {
	echo "Creating README.md... "
	touch $PROJECT_ROOT/README.md
	echo "# $PROJECT_NAME" > $PROJECT_ROOT/README.md
}


create
