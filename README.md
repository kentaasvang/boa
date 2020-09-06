# Create
Create is a simple CLI for python that makes it easy to set up new python-projects. It aims to make a barebones project-layout with sensible defaults, without assuming any dependecies what-so-ever.

The CLI's API isn't decided yet. It will either stay as-is, or move towards the same API as the dotnet-CLI.

The project-layout is inspired by [this document](https://docs.python-guide.org/writing/structure/)


### Installing
For now you have first setup the `$HOME/.my_binaries/bin` and export it to your $PATH. Then you clone the project from git and run `make install`


### Usage
To create a new project run the command:
```terminal
$ create python <project-name>
```
This will create your project at `$HOME/PythonProjects/<project-name>/`


### Contributing
Contributions are very welcome. Preferably you'll create and issue beforehand, but you can just submit PR's aswell. Every contribution will be credited in this README


