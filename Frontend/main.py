from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def transFunc():
    sent = request.form['textInput']
    translator = Translator()
    res = translator.detect(sent)
    if res.lang == 'en':
        outputText = translator.translate(sent, dest='gu')
    else:
        outputText = translator.translate(sent, dest='en')
    return render_template('index.html', transText=outputText.text)


if __name__ == "__main__":
    app.run(debug=True)
