# Password Generator App

A simple and secure password generator application built with Python and PyQt5. This tool creates strong, memorable passwords by combining random words and numbers.

## Features

- *Random Password Generation*: Creates passwords using a combination of words and numbers
- *Copy to Clipboard*: One-click copying of generated passwords
- *Password History*: Automatically saves generated passwords with associated usernames/emails
- *User-Friendly Interface*: Clean and intuitive GUI built with PyQt5

## How It Works

The application generates passwords in the format: word-number-word-number-word-number-word-number

Example: apple-3-book-7-car-2-dog-5

## Installation

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Dependencies

Install the required packages:

bash
```
pip install PyQt5 pyperclip
```

### Project Structure


password-generator/
├── main.py          # Main application file
├── word_list.py     # Contains the words_list for password generation
└── generated_list.txt # Auto-generated file storing password history


## Usage

1. Run the application:
bash
```
python main.py
```

2. Enter your email or username in the input field
3. Click "Generate Password" to create a new password
4. Click "Copy" to copy the password to your clipboard
5. The password and associated username will be saved to generated_list.txt

## Code Overview

### Main Components

- *sample Class*: Main application window inheriting from QWidget
- *generate_text()*: Creates the password from random words and numbers
- *copy_text()*: Handles copying to clipboard and saving to file
- *generate_pass()*: Triggers password generation


## File Format

Generated passwords are saved in generated_list.txt in the format:

username : generated-password
email : generated-password


## Customization

To modify the password generation:
1. Edit the words_list in word_list.py
2. Adjust the format in the generate_text() method

## License

This project is open source and available under the MIT License.
