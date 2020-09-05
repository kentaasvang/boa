# Python Project Setup

A simple script that quickly sets up a basic structure for your python-project. It makes no assumptions whatsoever besides that you'll be using Git, which should be reasonable to expect.

The project-structure is heavily inspired by [this document](https://docs.python-guide.org/writing/structure/)

### What gets created
	- README.md
	- LICENSE
	- setup.py
	- settings.py
	- requirements.txt
	- <project-name>.py
	- tests/test\_basic.py
	- Makefile
	- .gitignore

**README.md**
Simple Readme Template

**LICENSE**
Permissive MIT License

**setup.py**
Packaging and distribution

**settings.py**
A settings-file for configuration and stuff

**requirements.txt**
Project dependecies

**tests/**
Basic test-folder with simple sample-test

**Makefile**
project management

**.gitignore**
files to be ignored from version control

The only operation that is done besides this is a git init and commit with a basic commit message
