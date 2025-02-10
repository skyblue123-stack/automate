# AutoMate Clipboard Manager

AutoMate is a Python program designed to clean and manage the clipboard on Windows, enhancing data handling and preventing clutter. It continuously monitors the clipboard for new content, cleans it by removing unnecessary spaces and new lines, and then updates the clipboard with the cleaned content.

## Features

- **Automatic Detection**: Detects new clipboard content automatically.
- **Content Cleaning**: Cleans clipboard content by removing extra spaces and new lines.
- **Continuous Monitoring**: Runs in the background and continuously monitors clipboard changes.

## Requirements

- Windows OS
- Python 3.x
- `pywin32` library

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the `pywin32` library using pip:
    ```bash
    pip install pywin32
    ```

## Usage

1. Clone this repository or download the `automate.py` file.
2. Open a command prompt or terminal window.
3. Navigate to the directory containing the `automate.py` file.
4. Run the program:
    ```bash
    python automate.py
    ```

The program will start monitoring and managing the clipboard content automatically. You can stop the program by pressing `Ctrl + C`.

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.