# Text-to-Speech Translator

This project is a simple console application that translates text from one language to another and converts the translated text into speech. It allows users to select the source and target languages for translation.

## Project Structure

```
text-to-speech-translator
├── src
│   ├── main.py
│   ├── translator.py
│   ├── text_to_speech.py
│   └── utils
│       └── language_codes.py
├── requirements.txt
└── README.md
```

## Installation

To set up the project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Run the application:

```
python src/main.py
```

2. Follow the prompts to enter the source language, target language, and the text you want to translate.

3. The application will display the translated text and play the audio of the translated text.

## Functionality

- **Translation**: The application uses an external translation API to translate text from the source language to the target language.
- **Text-to-Speech**: The translated text is converted into speech using a text-to-speech library.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License.