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
        import make
        getattr(make, command)()
    except AttributeError as attribute_error:
        click.echo("There is no command in make.py with the name %s" % command)
