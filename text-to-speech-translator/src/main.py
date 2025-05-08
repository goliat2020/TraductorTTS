# main.py

import sys
import asyncio
from translator import Translator
from text_to_speech import TextToSpeech
from utils.language_codes import LANGUAGE_CODES
from ocr import extraer_texto_de_imagen

async def main():
    print("Welcome to the Text-to-Speech Translator with OCR!")
    
    # Mostrar idiomas disponibles
    print("Opciones de idioma:")
    for lang in LANGUAGE_CODES.keys():
        print(f"- {lang}")
    # convertir a minúsculas para comparar con el diccionario
    source_lang = input("Introduce idioma de origen: ").strip().lower()
    target_lang = input("Introduce idioma para traducir: ").strip().lower()
    
    if source_lang not in LANGUAGE_CODES or target_lang not in LANGUAGE_CODES:
        print("Lenguaje no válido")
        sys.exit(1)


    image_path = input("Dirección de la imágen: ").strip()

    # Extraer texto
    print("Extrayendo texto...")
    try:
        text = extraer_texto_de_imagen(image_path)
        if not text.strip():
            print("No se encontró texto en la imagen.")
            sys.exit(1)
    except Exception as e:
        print(f"Error leyendo el texto: {e}")
        sys.exit(1)

    print(f"Texto extraído: {text}")

    # Traducir el texto 
    translator = Translator()
    translated_text = await translator.translate_text(LANGUAGE_CODES[source_lang], LANGUAGE_CODES[target_lang], text)

    print(f"Translated text: {translated_text}")

    # Convertir a TTS y reproducir
    tts = TextToSpeech()
    tts.speak(translated_text, LANGUAGE_CODES[target_lang])

if __name__ == "__main__":
    asyncio.run(main())