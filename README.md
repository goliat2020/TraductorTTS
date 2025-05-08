# Traductor TTS con detección de texto en imágenes utilizando OCR

Este proyecto permite traducir texto extraído de imágenes a diferentes idiomas y convertirlo en audio utilizando Python.

## Características
- Extrae texto de imágenes utilizando `easyocr`.
- Traduce el texto extraído a diferentes idiomas utilizando `googletrans`.
- Convierte el texto traducido en audio utilizando `gTTS` y lo reproduce con `pygame`.

## Requisitos
Asegúrate de tener instalado Python 3.8 o superior.

## Instalación
Sigue estos pasos para instalar las dependencias necesarias:

1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Instala las dependencias ejecutando el siguiente comando:

   ```bash
   pip install googletrans==4.0.0-rc1 gTTS==2.2.3 pygame==2.5.0 easyocr==1.7.0
   ```

## Project Structure

```
text-to-speech-translator
├── src
│   ├── main.py
│   ├── translator.py
│   ├── text_to_speech.py
│   ├── ocr.py
│   └── utils
│       └── language_codes.py
└── README.md
```

## Ejecución

1. Ejecuta la aplicación:

   ```bash
   python src/main.py
   ```

2. Sigue las instrucciones para cargar una imagen, seleccionar el idioma de origen y el idioma de destino.

3. La aplicación mostrará el texto traducido y reproducirá el audio del texto traducido.

## Funcionalidad

- **OCR (Reconocimiento Óptico de Caracteres)**: Extrae texto de imágenes utilizando `easyocr`.
- **Translation**: Traduce el texto extraído a diferentes idiomas utilizando `googletrans`.
- **Text-to-Speech**: Convierte el texto traducido en audio utilizando `gTTS` y lo reproduce con `pygame`.
