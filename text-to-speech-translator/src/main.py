# main.py

import sys
import asyncio
from translator import Translator
from text_to_speech import TextToSpeech
from utils.language_codes import LANGUAGE_CODES

async def main():
    print("Welcome to the Text-to-Speech Translator!")
    
    # Display available languages
    print("Available languages:")
    for lang in LANGUAGE_CODES.keys():
        print(f"- {lang}")

    source_lang = input("Enter the source language: ").strip().lower()
    target_lang = input("Enter the target language: ").strip().lower()
    
    if source_lang not in LANGUAGE_CODES or target_lang not in LANGUAGE_CODES:
        print("Invalid language selection. Please try again.")
        sys.exit(1)

    text = input("Enter the text to translate: ")

    translator = Translator()
    translated_text = await translator.translate_text(LANGUAGE_CODES[source_lang], LANGUAGE_CODES[target_lang], text)

    print(f"Translated text: {translated_text}")

    tts = TextToSpeech()
    tts.speak(translated_text, LANGUAGE_CODES[target_lang])

if __name__ == "__main__":
    asyncio.run(main())