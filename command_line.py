import os
import sys
import click

from boa import boa


@click.group()
def cli():
    pass


@cli.command()
@click.argument("name")
def new(name):
    """
    Creates a new project NAME
    """
    boa.new(p_name=name)


@cli.command()
@click.argument("command")
def make(command):
    try:
        with open("make.py", "r") as file_handler:
            make = file_handler.read()
            exec(make, globals())
            globals()[command]()
    except AttributeError as attribute_error:
        click.echo("The command `%s` does not exist in make.py" % command)
    except KeyError as key_error:
        click.echo("The command `%s` does not exist in make.py" % command)
