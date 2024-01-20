from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "test"

@app.route("/getAppointment")
def appointment():
    return

@app.route("/availableAppoint")
def available():
    return

app.run(debug=True)