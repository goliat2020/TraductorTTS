from gtts import gTTS
import pygame
import os

class TextToSpeech:
        # Convierte el texto a voz usando Google Text-to-Speech y se guarda en el archivo output.mp3
    def speak(self, text, lang):
        tts = gTTS(text=text, lang=lang)
        audio_file = "output.mp3"
        tts.save(audio_file)

    # Reproduce el audio
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

     
        pygame.mixer.quit()
        os.remove(audio_file)