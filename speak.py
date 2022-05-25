from gtts import gTTS
import playsound

def speak(text):
    tts = gTTS(text=text, lang='ko')
    filename = 'audio_sprite.mp3'
    tts.save(filename)
    # playsound.playsound(filename)

speak("스프라이트입니다")