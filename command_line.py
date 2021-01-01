import os
import sys
import click

from boa import boa


@click.group()
def cli():
    pass


@cli.command()
@click.argument("name")
@click.argument("project_dir", required=False, default=None)
def new(name, project_dir):
    """
    Creates a new project NAME
    """
    boa.new(name, project_dir)


@cli.command()
@click.argument("command")
def make(command):
    """
    Runs the method named COMMAND located in make.py
    """
    try:
        boa.run_make_command(command)
    except Exception as e:
        click.echo(e)
