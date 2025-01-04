import os
import unicodedata
from typing import List, Dict

file_category = {
    "documents": [
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
    "compressed": [
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
    "images": [
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
    "video": [
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
    "audio": [
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
    "programs": [
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
    "code": [
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

    files = [unicodedata.normalize("NFKC", file) for file in files]
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
            "others",
        )

        categorized_data.setdefault(category, []).extend(filenames)

    return categorized_data
