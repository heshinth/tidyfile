import typer
import os
from rich import print
from rich.markdown import Markdown

from tidyfile.modules.file_classifier import file_count
from tidyfile.modules.exporter import output_as
from tidyfile.modules.file_organiser import move_files_to_categories


app = typer.Typer()


@app.command()
def sort():
    files = os.listdir()

    count = file_count(files)
    print(f"There are {count[0]} files which can be sorted into {count[1]} categories ")

    confirmation = typer.confirm("Continue?")
    if confirmation:
        move_files_to_categories(files)
    else:
        print("[bold red]Aborted!![/bold red]")


@app.command()
def list():
    files = os.listdir()
    md = Markdown(output_as(files))
    print(md)


if __name__ == "__main__":
    app()
