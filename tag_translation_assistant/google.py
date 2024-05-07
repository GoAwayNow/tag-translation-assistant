from deep_translator import GoogleTranslator
from deep_translator import exceptions as dtexceptions

def getTranslation(strIn):
    try:
        tl = GoogleTranslator(source='auto', target='en').translate(text=strIn)
    except dtexceptions as e:
        return str(e)
    else:
        return tl