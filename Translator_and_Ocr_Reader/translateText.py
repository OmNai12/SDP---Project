from googletrans import Translator


def translatorFunction(sent: str):
    translator = Translator()
    res = translator.detect(sent)
    if res.lang == 'en':
        outputText = translator.translate(sent, dest='gu')
    else:
        outputText = translator.translate(sent, dest='en')
    return outputText.text
