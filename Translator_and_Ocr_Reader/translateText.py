from googletrans import Translator
# import gtts


def translatorFunction(sent: str):
    translator = Translator()
    res = translator.detect(sent)
    if res.lang == 'en':
        outputText = translator.translate(sent, dest='gu')
        # speakLang = gtts.gTTS(outputText, lang='gu')
    else:
        outputText = translator.translate(sent, dest='en')
        # speakLang = gtts.gTTS(outputText, lang='en')
    return outputText.text
