import os
from typing import List, Dict

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
    if not files:
        return {}

    files = [file.encode("utf-8").decode("utf-8") for file in files]

    file_types = {}

    for file in files:
        if os.path.isfile(file):
            _, ext = os.path.splitext(file)
            file_types.setdefault(ext, []).append(file)

    return file_types


def categorize_files_by_type(files: List[str]) -> Dict[str, List[str]]:
    """
    Categorize files based on their types.

    Parameters:
    files (list): List of file names.

    Returns:
    dict: Dictionary with categories as keys and lists of file names as values.
    """
    if not files:
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

    return categorized_data


def file_count(files: list):
    category_count = 0
    file_count = 0
    categorized_data = categorize_files_by_type(files)
    for category, file_names in categorized_data.items():
        category_count += 1
        for file_name in file_names:
            file_count += 1

    return file_count, category_count
