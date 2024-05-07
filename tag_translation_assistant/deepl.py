import deepl
from . import config as tataconfig

deeplAuth = tataconfig.config['deepl']['apikey']
deeplTranslator = deepl.Translator(deeplAuth)

def getTranslation(tag):
    try:
        t = deeplTranslator.translate_text(tag, target_lang="EN-US")
    except deepl.DeepLException as e:
        return str(e)
    else:
        return t.text
