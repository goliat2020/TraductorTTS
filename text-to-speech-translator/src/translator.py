from googletrans import Translator as GoogleTranslator

class Translator:
     # Inicializa el traductor de Google
    def __init__(self):
        self.translator = GoogleTranslator()

    async def translate_text(self, source_lang, target_lang, text):
        # Traduce el texto especificando idioma de origen y destino
        result = await self.translator.translate(text, src=source_lang, dest=target_lang)
        return result.text