from flask import Flask , request, jsonify
from flask_cors import CORS
import db_functions
import business_functions
import json

app = Flask(__name__)
CORS(app)

@app.route("/insert", methods = ["POST"])
def insert():
    data = request.get_data()
    data_list = business_functions.read_from_workbook(data)
    invalid_data_list = db_functions.insert_after_check(data_list)
    return json.dumps(invalid_data_list), 200

if __name__== '__main__':
    app.run(debug=True)