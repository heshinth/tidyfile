from tidyfile.modules.file_classifier import categorize_files_by_type, file_count
from tidyfile.utils.logger_setup import logger

import time


def output_as(files: list, type: str):
    data = categorize_files_by_type(files)
    if type == "markdown":
        markdown = dict_to_markdown(data)
        count = file_count(files)
        markdown += f"\nThere are **{count[0]}** files which can be sorted into **{count[1]}** categories."
        return markdown


def dict_to_markdown(data: dict, level: int = 0):
    """
    Convert a Python dictionary to a Markdown formatted string.

    Args:
        data (dict): The dictionary to convert.
        level (int): Current depth level for nested dictionaries.

    Returns:
        str: Markdown formatted representation of the dictionary.
    """

    markdown = ""
    indent = "  " * level

    for key, value in data.items():
        if key == "":
            key = "No file type"

        if isinstance(value, dict):
            markdown += f"{indent}- **{key}**:\n"
            markdown += dict_to_markdown(value, level + 1)
        elif isinstance(value, list):
            markdown += f"{indent}- **{key}**:\n"
            for item in value:
                markdown += f"{indent}  - {item}\n"
        else:
            markdown += f"{indent}- **{key}**: {value}\n"

    return markdown


def create_export(data, type):
    logger.debug(f"Export as {type}")
    if type == "markdown":
        s = time.strftime("%Y%m%d_%H%M%S")
        filename = f"TidyFile_Export_{s}.md"
        file = open(filename, "w")
        file.write(data)
        logger.debug(f"Created Export as {filename}")
        return filename
