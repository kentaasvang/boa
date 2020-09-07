![issues](https://img.shields.io/github/issues/kentaasvang/python_create) ![pythonversion](https://img.shields.io/badge/python-%3E%3D%203.8-blue) ![platforms](https://img.shields.io/badge/platform-macos-lightgrey)

# Create
Create is a simple CLI for python that makes it easy to set up new python-projects. It aims to make a clean project-layout with sensible defaults, without assuming any dependecies what-so-ever. 

The CLI's API isn't decided yet. It will either stay as-is, or move towards the same API as the dotnet-CLI.

The project-layout is inspired by [this document](https://docs.python-guide.org/writing/structure/)


### Installing
For now you have to first setup the `$HOME/.my_binaries/bin`-directory and export it to your $PATH. Then you clone the project from git, cd into the cloned project and run `make install`


### Usage
To create a new project run the command:
```terminal
$ create python <project-name>
```
This will create your project at `$HOME/PythonProjects/<project-name>/`


### Contributing
Contributions are very welcome. Preferably you'll create and issue beforehand, but you can just submit PR's aswell. Every contribution will be credited in this README


