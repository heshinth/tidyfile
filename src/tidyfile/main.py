import typer
import os
from rich import print
from rich.markdown import Markdown

from tidyfile.modules.file_classifier import categorize_files_by_type
from tidyfile.modules.exporter import output_as
from tidyfile.modules.file_organiser import move_files_to_categories


app = typer.Typer()


@app.command()
def sort():
    files = os.listdir()

    dict2 = categorize_files_by_type(files)
    print(dict2)
    move_files_to_categories(files)


@app.command()
def list():
    files = os.listdir()
    md = Markdown(output_as(files))
    print(md)


if __name__ == "__main__":
    app()
