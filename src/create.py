#!/usr/local/bin//python3

""" MVP of python_create

API:
    - create new <thing>

Things we can create:
    - requirements.txt
    - setupfile
    - readme
    - license
    - python package
    - essentials (all of the above)
"""
ALLOWED_COMMANDS = ["new"]

def main(args):
    
    # Check input
    if len(args) != 2:
        raise Exception(f"We need two arguments, not {len(args)}")

    command, recipe = args

    if command not in ALLOWED_COMMANDS:
        raise NotImplementedError(f"{args[0]} is not an implemented command")
    
    create(command, recipe)


def create(command, recipe):
    template = get_template(recipe)
    write(template, **kwargs) 


def write(template, **kwargs):
    pass



if __name__ == "__main__": 
    from sys import argv
    args = argv[1:]
    main(args)
