import typer
from calculator import core

app = typer.Typer(help="A simple command line calculator.")

@app.command()
def sum(a: float, b: float) -> None:
    """
    This method adds two numbers together and returns the result.
    :param a: the first number
    :param b: the second number
    :return: the result is printed at video
    """
    typer.echo(core.sum(a, b))

@app.command()
def sub(a: float, b: float) -> None:
    """
    This method allows users to select two numbers from cli and get back the subtraction
    :param a: the first number
    :param b: the second number
    :return: the result is printed at video
    """
    typer.echo(core.sub(a, b))

@app.command()
def mul(a: float, b: float) -> None:
    """
    This method allows users to select two numbers from cli and get back the multiplication
    :param a: the first number
    :param b: the second number
    :return: the result is printed at video
    """
    typer.echo(core.mul(a, b))

@app.command()
def div(a: float, b: float) -> None:
    """
    This method allows users to select two numbers from cli and get back the division
    :param a: the first number
    :param b: the second number
    :return: the result is printed at video
    """
    if b == 0:
        raise ZeroDivisionError
    typer.echo(core.div(a, b))

if __name__ == "__main__":
    app()
