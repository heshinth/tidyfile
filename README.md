# TidyFile

**TidyFile**: Declutter your workspace with this command-line tool that automatically categorizes and sorts your files into organized directories.

## Features

- Automatically categorizes files into predefined groups like Documents, Images, Videos, Archives, and more.
- Provides a summary of the files and their categories.
- Generates a report of categorized files in Markdown format.

## Installation

You can install TidyFile using pip:

```sh
pip install tidyfile
```

## Usage

### Sorting Files

To sort files in the current directory into categorized directories:

```sh
tidyfile sort
```

### Preview Files

To preview all files in the current directory categorized without moving the files:

```sh
 tidyfile preview
```

A simplified example of the output:

```sh
- Documents
  - document1.pdf
  - report.docx

- Images
  - image1.jpg
  - photo.png

```

## Build Instructions

This project uses `uv` for management. To build the project, follow these steps:

1. Install `uv` by following the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/).
2. Clone the repository:

```sh
git clone https://github.com/heshinth/tidyfile.git
```

3. Sync the project dependencies using uv sync:

```sh
uv sync
```

## Future Plans

- [ ] Ability to export categorized files as Markdown, JSON and CSV formats.
- [ ] Custom Categories: Allow users to define their own file categories and extensions.
- [ ] Recursive Sorting: Add an option to sort files in subdirectories recursively.

## Contact

For any inquiries or issues, please open an issue on the [GitHub repository](https://github.com/heshinth/tidyfile/issues).

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.
