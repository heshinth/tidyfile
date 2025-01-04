# TidyFile

TidyFile is a CLI tool to organize and manage files in the current directory. It categorizes files based on their types and sorts them into organized directories.

## Features

- Categorizes files into predefined categories such as Documents, Images, Videos, etc.
- Supports sorting files into directories.
- Provides a summary of the files and their categories.
- Outputs categorized files in Markdown format.

## Installation

You can install TidyFile using pip:

```sh
pip install tidyfile
```

## Usage

### Sorting Files

To sort files in the current directory into categories:

```sh
tidyfile sort
```

### Preview Files

To preview all files in the current directory categorized:

```sh
tidyfile preview
```

## Build Instructions

This project uses `uv` for management. To build the project, follow these steps:

1. Install `uv` by following the [uv documentation](https://docs.astral.sh/uv/getting-started/installation/).
2. Clone the repository:
   ```sh
   git clone https://github.com/heshinth/tidyfile.git
   ```
3. Sync the project dependencies:
   ```sh
   uv sync
   ```

## Development

To contribute to TidyFile, follow these steps:

1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch for your feature or bugfix.
4. Make your changes and commit them.
5. Push your changes to your forked repository.
6. Create a pull request to the main repository.

## Future Plans

- [ ] Ability to export categorized files as Markdown, JSON and CSV formats.
- [ ] Custom Categories: Allow users to define their own file categories and extensions.
- [ ] Recursive Sorting: Add an option to sort files in subdirectories recursively.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, please open an issue on the [GitHub repository](https://github.com/heshinth/tidyfile/issues).
