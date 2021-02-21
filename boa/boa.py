#!/usr/bin/env python3
import os

from pathlib import Path


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
    if not Path.exists(project_root):
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
    os.system(f"git init {root} --quiet")


# TODO: replace with string.Template.substitute
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


def run():
    """
    run python project
    """
    pass


def new(path):
    """
    Entrypoint
    """
    root = Path(path)

    # abort if path exists
    if root.exists():
        raise FileExistsError("path already exists")

    # create project folder
    root.mkdir(parents=True)

    # create requirements.txt
    requirements = root / Path("requirements.txt")
    requirements.touch()

    # create main-module
    main = root / Path("main.py")
    main.touch()

    # hello world-example in main-module
    with open(main, "w") as file_handler:
        file_handler.write(
            "\ndef main():\n\tprint(\"hello, world\")\n\n\nif __name__ == \"__main__\":\n\tmain()\n".expandtabs(4)
        )

    # git init
    git_init(root)


if __name__ == "__main__":
    new("var/www/user/name")
