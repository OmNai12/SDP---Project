from flask import Flask, render_template, request
from translateText import translatorFunction
from werkzeug.utils import secure_filename
# from OCR_READER.index import ocr_Function


EXT_ALLOW = set(['png', 'jpeg', 'jpg'])


def check_Allowed_Extension(fileName: str):
    return '.' in fileName and fileName.rsplit('.', 1)[1].lower() in EXT_ALLOW


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def transFunc():
    sent = request.form['textInput']
    transTextGet = translatorFunction(sent)
    return render_template('index.html', transText=transTextGet)


@app.route("/ocrreader", methods=['POST'])
def file_func():
    if request.method == 'POST':
        fileHandler = request.files['inputFile']
        fName = secure_filename(fileHandler.filename)
        # fileHandler.save(fName)
        # textObt = ocr_Function('../img_test.png')

    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)
