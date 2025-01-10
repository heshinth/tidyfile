import os
from typing import List, Dict
from tidyfile.utils.logger_setup import logger

file_category = {
    "Documents": [
        ".pdf",
        ".doc",
        ".docx",
        ".txt",
        ".rtf",
        ".odt",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".csv",
        ".md",
    ],
    "Compressed": [
        ".zip",
        ".rar",
        ".7z",
        ".tar",
        ".gz",
        ".bz2",
        ".tar.gz",
        ".tgz",
        ".iso",
    ],
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".tiff",
        ".webp",
        ".svg",
        ".ico",
        ".raw",
        ".heic",
    ],
    "Video": [
        ".mp4",
        ".mov",
        ".avi",
        ".wmv",
        ".flv",
        ".webm",
        ".mkv",
        ".m4v",
        ".mpg",
        ".mpeg",
    ],
    "Audio": [
        ".mp3",
        ".wav",
        ".ogg",
        ".m4a",
        ".flac",
        ".aac",
        ".wma",
        ".aiff",
        ".opus",
    ],
    "Programs": [
        ".exe",
        ".app",
        ".dmg",
        ".msi",
        ".deb",
        ".rpm",
        ".apk",
        ".bat",
        ".sh",
        ".com",
    ],
    "Code": [
        ".py",
        ".js",
        ".java",
        ".cpp",
        ".c",
        ".cs",
        ".php",
        ".html",
        ".css",
        ".sql",
        ".rb",
        ".swift",
        ".go",
        ".rs",
        ".ts",
        ".jsx",
        ".tsx",
    ],
}


def normalize_and_group_files(files: List[str]) -> Dict[str, List[str]]:
    """
    Normalize file names and group files by their extension.

    Parameters:
    files (list): List of file names.

    Returns:
    dict: Dictionary with file extensions as keys and lists of file names as values.
    """
    logger.debug(f"Normalizing and grouping files: {files}")
    if not files:
        logger.debug("No files provided.")
        return {}

    files = [file.encode("utf-8").decode("utf-8") for file in files]
    logger.debug(f"Normalized files: {files}")

    file_types = {}

    for file in files:
        if os.path.isfile(file):
            _, ext = os.path.splitext(file)
            file_types.setdefault(ext, []).append(file)
            logger.debug(f"File '{file}' grouped under extension '{ext}'")

    logger.debug(f"Grouped file types: {file_types}")
    return file_types


def categorize_files_by_type(files: List[str]) -> Dict[str, List[str]]:
    """
    Categorize files based on their types.

    Parameters:
    files (list): List of file names.

    Returns:
    dict: Dictionary with categories as keys and lists of file names as values.
    """
    logger.debug(f"Categorizing files by type: {files}")
    if not files:
        logger.debug("No files provided.")
        return {}

    d_types = normalize_and_group_files(files)
    categorized_data = {}

    for extension, filenames in d_types.items():
        category = next(
            (
                category
                for category, extensions in file_category.items()
                if extension in extensions
            ),
            "Others",
        )
        categorized_data.setdefault(category, []).extend(filenames)
        logger.debug(
            f"Files with extension '{extension}' categorized under '{category}'"
        )

    logger.debug(f"Categorized data: {categorized_data}")
    return categorized_data


def file_count(files: list):
    """
    Counts the total number of files and categories in the given list of files.

    Args:
        files (list): A list of file paths to be categorized and counted.

    Returns:
        tuple: A tuple containing the total number of files and the total number of categories.
    """
    logger.debug(f"Counting files and categories for: {files}")
    category_count = 0
    file_count = 0
    categorized_data = categorize_files_by_type(files)
    for category, file_names in categorized_data.items():
        category_count += 1
        for file_name in file_names:
            file_count += 1

    logger.debug(
        f"Total file count: {file_count}, Total category count: {category_count}"
    )
    return file_count, category_count
