from gtts import gTTS
from playsound import playsound
import os

#############################################################################
# text to speech reproduce por audio el mensaje pasado como parametro
# este modulo ptssx3 es simple pero para que sea en español cada PC debe
# tener habilitado el uso de voces espanolas en programas no oficiales

# def tss(msg='no message', lan = 'eng'):
#    text = ps.init()
#    text.say(msg)
#    text.runAndWait()
#############################################################################


def tss(msg='No hay mensaje', lan='es-es', file_name='audio'):
    NOMBRE_ARCHIVO = str(file_name + '.mp3')
    tts = gTTS(msg, lang=lan)
    tts.save(NOMBRE_ARCHIVO)
    playsound(NOMBRE_ARCHIVO)
    os.remove(NOMBRE_ARCHIVO)
