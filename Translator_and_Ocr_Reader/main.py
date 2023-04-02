from flask import Flask, render_template, request
from translateText import translatorFunction
from werkzeug.utils import secure_filename
from helper import ocr_Reader_function


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def transFunc():
    sent = request.form['textInput']
    transTextGet = translatorFunction(sent)
    return render_template('index.html', transText=transTextGet, otext=sent)


@app.route("/ocrreader", methods=['POST'])
def file_func():
    if request.method == 'POST':
        fileHandler = request.files['inputFile']
        fName = secure_filename(fileHandler.filename)
        fileHandler.save(fName)
        textObt = ocr_Reader_function()
        transTextGet = translatorFunction(textObt)
    return render_template('ocrreader.html', originalText=textObt, translatedText=transTextGet)


if __name__ == "__main__":
    app.run(debug=True)
