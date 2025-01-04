from tidyfile.modules.file_classifier import categorize_files_by_type, file_count


def output_as(files: list):
    data = categorize_files_by_type(files)
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
