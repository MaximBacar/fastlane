from flask import Flask
from flask_cors import CORS
import database.connector as db


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "test"

@app.route("/getAppointments")
def appointment():
    data = [
            { 
                "id"        : 1,
                "start"     : "8:00",
                "end"       : "8:30",
                "type"      : "Compact",
                "full_name" : "Maxim Bacar",
                "phone"     : "(514) 123-4567"
            },
            {
                "id"        : 2,
                "start"     : "8:00",
                "end"       : "9:00",
                "type"      : "Class-1",
                "full_name" : "Asmae Loulidi",
                "phone"     : "(514) 123-4567"
            },
            { 
                "id"        : 3,
                "start"     : "8:00",
                "end"       : "8:30",
                "type"      : "Compact",
                "full_name" : "Maxim Bacar",
                "phone"     : "(514) 123-4567"
            },
            {
                "id"        : 4,
                "start"     : "8:00",
                "end"       : "9:00",
                "type"      : "Class-1",
                "full_name" : "Asmae Loulidi",
                "phone"     : "(514) 123-4567"
            },
            { 
                "id"        : 5,
                "start"     : "8:00",
                "end"       : "8:30",
                "type"      : "Compact",
                "full_name" : "Maxim Bacar",
                "phone"     : "(514) 123-4567"
            },
            {
                "id"        : 6,
                "start"     : "8:00",
                "end"       : "9:00",
                "type"      : "Class-1",
                "full_name" : "Asmae Loulidi",
                "phone"     : "(514) 123-4567"
            }
    ]
    return data

@app.route("/isAppointmentValid", methods=['Post'])
def isAvailable():

    db.is_slot_valid(3,3)

app.run(debug=True)