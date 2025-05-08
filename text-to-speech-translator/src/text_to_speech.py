from gtts import gTTS
import pygame
import os

class TextToSpeech:
    def speak(self, text, lang):
        tts = gTTS(text=text, lang=lang)
        audio_file = "output.mp3"
        tts.save(audio_file)

    
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

     
        pygame.mixer.quit()
        os.remove(audio_file)