import typer
import os
from rich import print
from rich.markdown import Markdown
from typing_extensions import Annotated

from tidyfile.modules.file_classifier import file_count
from tidyfile.modules.file_exporter import output_as, create_export
from tidyfile.modules.file_organiser import move_files_to_categories


app = typer.Typer(
    add_completion=False,
    no_args_is_help=True,
    help="A CLI tool to organize and manage files in the current directory.",
)


@app.command()
def sort():
    """
    Sort files in the current directory into categories based on their type.
    """

    files = os.listdir()

    count = file_count(files)
    print(f"There are {count[0]} files which can be sorted into {count[1]} categories ")

    confirmation = typer.confirm("Continue?")
    if confirmation:
        move_files_to_categories(files)
    else:
        print("[bold red]Aborted!![/bold red]")


@app.command()
def preview(
    export: Annotated[
        bool, typer.Option(help="Export the preview as a markdown file")
    ] = False,
):
    """
    Preview all files in the current directory categorized.
    """
    files = os.listdir()
    md_view = output_as(files, "markdown")
    preview = Markdown(md_view)
    print(preview)
    if export:
        export_file = create_export(output_as(files, "markdown"), "markdown")
        print(f"The preview is exported as [bold green]{export_file}[/bold green]")


if __name__ == "__main__":
    app()
