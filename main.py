import speech_recognition as sr
from time import ctime 
import webbrowser
import time
from gtts import gTTS
import os 
import random
import playsound

r = sr.Recognizer()

def record_voice(ask=False):  
    with sr.Microphone() as source:
        if ask:
            vega_speak(ask)
        audio = r.listen(source)
        voice_data=''
        try:

            voice_data = r.recognize_google(audio, language='fr')
        except sr.UnknownValueError:
            vega_speak('Désolé je ne comprends pas :( ')
        except sr.RequestError:
            vega_speak('Désolé mon système ne fonctionne pas')
        return voice_data


def vega_speak(audio_string):
    tts = gTTS(text=audio_string, lang='fr')
    r= random.randint(1, 10000000)
    audio_file= 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


    
def respond(voice_data):
    if "prénom" in voice_data:
        vega_speak("Je suis Vega")
    if  'Bonjour' in voice_data:
        vega_speak('Bien le bonjour a vous')
    if "recherche" in voice_data:
        search= record_voice('Que souhaitez-vous chercher?')
        url= 'https://google.fr/search?q=' + search
        webbrowser.get().open(url)
        vega_speak("Voici ce que j'ai trouve pour " + search)
    if "localisation" in voice_data:
        location = record_voice('Quel endroit recherchez-vous')
        url= 'https://google.fr/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        vega_speak('Voici la localisation de ' + location)
    if 'YouTube' in voice_data:
        youtube= record_voice('Que souhaitez vous regarder?')
        url= 'https://youtube.com/results?search_query=' + youtube
        webbrowser.get().open(url)
        vega_speak('Voici ce que vous voulez regarder')
    if 'je vais te gifler' in voice_data:
        vega_speak('et.... le chien!!')
    if 'qui est le meilleur' in voice_data:
        vega_speak("Quelle question! tout le monde sait que c'est toi, ensuite Dieudonné, et au dessus c'est le soleil wesh")
    if 'au revoir' in voice_data:
        vega_speak('A bientot, merci')
        exit()
        
        
time.sleep(1)        
vega_speak('En quoi puis-je vous aider Serge ?')
while 1:
    voice_data= record_voice()
    respond(voice_data)
