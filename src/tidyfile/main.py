import typer
import os
from rich import print
from tidyfile import format


app = typer.Typer()


@app.command()
def sort():
    files = os.listdir()
    format(files)


@app.command()
def show():
    print("test")


if __name__ == "__main__":
    app()
