from flask import Flask, render_template, request
from translateText import translatorFunction, translatorFunctionFile, playSoundFunction
from werkzeug.utils import secure_filename
from helper import ocr_Reader_function

transTextGet = sent = ""

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/soundplay", methods=['POST'])
def newRoute():
    playSoundFunction()
    return render_template('index.html', transText=transTextGet, otext=sent)


@app.route("/", methods=['POST'])
def transFunc():
    global sent
    sent = request.form['textInput']
    global transTextGet
    transTextGet = translatorFunction(sent)
    return render_template('index.html', transText=transTextGet, otext=sent)


@app.route("/ocrreader", methods=['POST'])
def file_func():
    if request.method == 'POST':
        fileHandler = request.files['inputFile']
        fName = secure_filename(fileHandler.filename)
        fileHandler.save(fName)
        textObt = ocr_Reader_function()
        transTextGet = translatorFunctionFile(textObt)
    return render_template('ocrreader.html', originalText=textObt, translatedText=transTextGet)


if __name__ == "__main__":
    app.run(debug=True)
