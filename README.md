# LeoAI

LeoAI is a speech recognition application system built with Python. It utilizes OpenAI's API for AI functionalities and incorporates a rule-based system for additional features such as opening specific browser links and playing music from local storage.

## Features

- **Speech Recognition**: Convert spoken language into text using the `speech_recognition` library.
- **AI Integration**: Use OpenAI's API to process and respond to user queries.
- **Rule-Based Functions**:
  - Open specific URLs in a web browser.
  - Play music files stored on local storage.

## Requirements

Ensure you have the following libraries installed. You can install them using the provided `requirements.txt` file:

- `win32com.client`
- `speech_recognition`
- `openai`
- `webbrowser` (Standard library, no installation required)
- `datetime` (Standard library, no installation required)
- `os` (Standard library, no installation required)

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

## Setup

1. API Key Configuration: Create a file named API_KEY in the root directory of the project. This file should contain your OpenAI API key. Ensure the file is not included in version control by adding it to .gitignore.

2. Running the Application: Once the API key is set up, you can run the application by executing:

```bash
python app.py
```

## Usage

1. Speech Recognition: Speak into your microphone, and the application will convert your speech to text and process it using OpenAI's API.
2. Opening URLs: You can use specific commands to open predefined URLs in your web browser.
3. Playing Music: Use commands to play music files stored locally.
4. etc

## Contributing

If you'd like to contribute to the development of LeoAI, please fork the repository and submit a pull request with your changes. Ensure that your contributions adhere to the project's coding standards and include appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or issues, please contact me.
