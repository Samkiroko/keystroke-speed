
# Keystroke Speed Capture Application

## Overview

The Keystroke Speed Capture Application is a Python-based tool designed to measure and analyze typing speed in terms of keystrokes per minute (KPM). It provides a graphical interface for users to type text within a specified timeframe, captures all keystrokes including special keys (e.g., space, delete, command, control), and logs the session's details to a text file.

## Features

- **Customizable Typing Duration**: Users can specify the duration of each typing session in seconds via the console before the typing window appears.
- **Graphical Typing Interface**: A simple and intuitive graphical window where users can type their text.
- **Comprehensive Keystroke Logging**: Captures and logs every keystroke, including alphanumeric characters and special keys like space, backspace, and enter.
- **Typing Analysis Report**: Calculates the typing speed in keystrokes per minute (KPM) and generates a report that includes the typed text, the total number of keystrokes, and a detailed keystroke log.

## Setup

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- pynput library

### Installation

1. Ensure Python and Tkinter are installed on your system.
   
   You can check if Python is installed by running:
   ```sh
   python3 --version
   ```

   Verify Tkinter installation by running:
   ```sh
   python3 -m tkinter
   ```

2. Install the `pynput` library using pip:
   ```sh
   pip3 install pynput
   ```

## Usage

1. **Start the Application**: Navigate to the directory containing the script and run it using Python:
   ```sh
   python3 main.py
   ```
   
2. **Enter the Typing Duration**: When prompted in the console, enter the duration for the typing session in seconds.

3. **Type Your Text**: The typing window will open. Start typing your text. The window will automatically close when the specified time is up, or you can close it manually if needed.

4. **View the Results**: After the session ends, the application calculates your typing speed and generates a report. This report is saved to `typing_analysis.txt` in the same directory as the script, containing the typed text, keystrokes per minute, total keystrokes, and a detailed log of all keystrokes.

5. **Review the Keystroke Log**: Open `typing_analysis.txt` to review the detailed report of your typing session, including each keystroke logged during the session.

## How It Works

The application utilizes the `tkinter` library for the graphical interface and `pynput` for capturing keystrokes. When the user starts typing, it records the start time and counts every keystroke, including special keys. Upon closing the typing window or when the time is up, it calculates the total typing duration, speed (KPM), and logs the session details to a file.

## Contributing

Feel free to fork the repository and submit pull requests to contribute to this project. Whether it's adding new features, fixing bugs, or improving documentation, all contributions are welcome.

## License

This project is open source and available under the [MIT License](LICENSE).
