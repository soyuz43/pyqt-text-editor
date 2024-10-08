# Simple Text Editor

This is a simple text editor built using PyQt5. It enables you to create, open, edit, and save text files. This project is designed to demonstrate fundamental PyQt development capabilities and serves as a starting point for more complex text editing applications.

## Features

- **Create new text files**: Start new projects quickly.
- **Open existing text files**: Edit files you've already started.
- **Edit and save changes to text files**: Make and retain changes to your documents.
- **Cut, copy, and paste text**: Easily manage your text.
- **Basic text formatting options**: Enhance your text.

## Prerequisites

To run this text editor, you need Python and PyQt5 installed on your system. This project uses Python 3.9 and PyQt5.

### Installing Python

Download and install Python from [Python's official website](https://www.python.org/downloads/).

### Installing PyQt5

You can install PyQt5 via pip or Conda. Here's how you can install it using either method:

- **Using pip**:
  ```bash
  pip install PyQt5
  ```
  
- **Using Conda**:
  ```bash
  conda install -c anaconda pyqt
  ```

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:
   Clone the project repository by running:
   ```bash
   git clone https://github.com/soyuz43/pyqt-text-editor.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd pyqt-text-editor
   ```

3. **Create and Activate Conda Environment**:
   Create the Conda environment using the `environment.yml` file:
   ```bash
   conda env create -f environment.yml
   conda activate texteditor
   ```

## Usage

To run the text editor, execute the following command within the root directory of the project, ensuring that the Conda environment is activated:
```bash
python src/main.py
```
This command launches the text editor window, allowing you to start creating and editing text files.

## Contributing

We welcome contributions to this project. To contribute:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
