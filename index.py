from flask import Flask, render_template, request
from sentimentAnalysis import analyse

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("assign2.html")


@app.route('/analyse', methods=['POST'])
def predict():
    return analyse(request.form.get("subject"))


if __name__ == "__main__":
    app.run(debug=True)
