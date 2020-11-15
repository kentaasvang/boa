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
