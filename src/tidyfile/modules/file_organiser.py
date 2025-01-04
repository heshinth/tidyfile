import os
import shutil

from tidyfile.utils.logger_setup import logger
from tidyfile.modules.file_classifier import categorize_files_by_type


def move_files_to_categories(files: list):
    """
    Moves files into categorized folders based on their type.

    Args:
        files (list): A list of file paths to be categorized and moved.

    The function categorizes the given files by their type and moves them into corresponding folders.
    If the category folder does not exist, it creates the folder. Logs the actions performed and any errors encountered.
    """
    categorised_files = categorize_files_by_type(files)

    for category, filenames in categorised_files.items():
        category_folder = os.path.join("", category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            logger.debug(f"Created category folder : {category}")

        for file in filenames:
            destination_file = os.path.join(category_folder, os.path.basename(file))
            try:
                shutil.move(file, destination_file)
                logger.debug(f"Moved {file} to {destination_file}")
            except Exception as e:
                logger.error(f"Error moving {file} to {destination_file}: {e}")

    print("done")
