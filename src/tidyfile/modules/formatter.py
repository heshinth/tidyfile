import os
import unicodedata


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
}


def data_formatter(files: list) -> dict:
    files = [unicodedata.normalize("NFKC", file) for file in files]
    file_types = {}

    for file in files:
        if os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if ext not in file_types:
                file_types[ext] = []
            file_types[ext].append(file)

    return file_types


def categorize_files(files: list):
    d_types = data_formatter(files)
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

        if category not in categorized_data:
            categorized_data[category] = []
        categorized_data[category].extend(filenames)

    return categorized_data