import os
import shutil
import logging

from tidyfile.modules.file_classifier import categorize_files_by_type


def move_files_to_categories(files: list):
    categorised_files = categorize_files_by_type(files)

    logging.basicConfig(filename="file_mover.log", level=logging.INFO)

    for category, filenames in categorised_files.items():
        category_folder = os.path.join("", category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
            logging.info(f"Created category folder : {category}")

        for file in filenames:
            destination_file = os.path.join(category_folder, os.path.basename(file))
            try:
                shutil.move(file, destination_file)
                logging.info(f"Moved {file} to {destination_file}")
            except Exception as e:
                logging.error(f"Error moving {file} to {destination_file}: {e}")

    print("done")
