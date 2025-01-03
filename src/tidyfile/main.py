import typer
import os
from rich import print
from rich.markdown import Markdown
from tidyfile.modules.formatter import categorize_files
from tidyfile.modules.exporter import output_as


app = typer.Typer()


@app.command()
def sort():
    files = os.listdir()

    dict2 = categorize_files(files)
    print(dict2)


@app.command()
def list():
    files = os.listdir()
    md = Markdown(output_as(files))
    print(md)


if __name__ == "__main__":
    app()
