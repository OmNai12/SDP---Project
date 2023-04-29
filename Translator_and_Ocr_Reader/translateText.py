from googletrans import Translator
import gtts
import playsound

pathOfPlayPound = ""


def translatorFunction(sent: str):
    translator = Translator()
    res = translator.detect(sent)
    if res.lang == 'en':
        outputText = translator.translate(sent, dest='gu')
        sound = gtts.gTTS(outputText.text, lang='gu')
        sound.save("tts.mp3")
        global pathOfPlayPound
        pathOfPlayPound = "tts.mp3"
    else:
        outputText = translator.translate(sent, dest='en')
        sound = gtts.gTTS(outputText.text, lang='en')
        sound.save("etts.mp3")
        pathOfPlayPound = "etts.mp3"
    return outputText.text


def translatorFunctionFile(sent: str):
    translator = Translator()
    res = translator.detect(sent)
    if res.lang == 'en':
        outputText = translator.translate(sent, dest='gu')
        # speakLang = gtts.gTTS(outputText, lang='gu')
    else:
        outputText = translator.translate(sent, dest='en')
        # speakLang = gtts.gTTS(outputText, lang='en')
    return outputText.text


def playSoundFunction():
    if pathOfPlayPound == "":
        return "Error"
    else:
        playsound.playsound(pathOfPlayPound)
    return "Done"
