from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from prediction import prediction

# Initializing flask application
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def home():
    return render_template('index.html', title='Home')


@app.route("/predict", methods=["POST"])
def Req():
    data = request.files["img"]
    data.save("img.jpg")

    resp = prediction("img.jpg")

    text = "it is a <b>"+resp['label']

    return render_template("prediction.html",prediction=text)
if __name__=='__main__':
    app.run(port=5000,debug=True)

