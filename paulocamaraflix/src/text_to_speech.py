class tts():

    def generate_audio(self, text, filename):
        """"""
        from gtts import gTTS
        from pathlib import Path
        
        tts= gTTS(text= text, lang="pt")
        tts.save(Path(f'audios/{filename}.mp3'))

