from dbhelper import DBHelper
from flask import Flask, render_template, request
import json

import dbconfig
if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper


app = Flask(__name__)
DB = DBHelper()

@app.route("/")
def home():
    crimes = DB.get_all_crimes()
    print crimes
    print '-----------------'
    crimes = json.dumps(crimes)
    print crimes
    return render_template("home.html", crimes=crimes)


@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    category = request.form.get("category")
    date = request.form.get("date")
    latitude = request.form.get("latitude")
    longitude = request.form.get("longitude")
    description = request.form.get("description")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
