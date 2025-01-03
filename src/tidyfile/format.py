import os
import unicodedata


def format(files):
    files = [unicodedata.normalize("NFKC", file) for file in files]
    file_types = {}
    filehandler = open("test.json", "wt")

    for file in files:
        if os.path.isfile(file):
            name, ext = os.path.splitext(file)
            if ext not in file_types:
                file_types[ext] = []
            file_types[ext].append(file)

    return file_types

    data = str(file_types)
    filehandler.write(data)

    print(file_types)
