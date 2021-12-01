from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from werkzeug.wrappers import response

app = Flask(__name__)
app.config["DEBUG"] = True

api = Api(app)

CORS(app)

# variable kosong type dictionary == json
identitas = {} # global variabel

# membuat class Resource
class ContohResource(Resource):
    # methode get dan post
    def get(self):
        # response = {"msg":"Hallo Sapi, ini restfull pertama saya"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil dimasukkan"}
        return response

api.add_resource(ContohResource, "/api", methods=["GET", "POST"])
if __name__ == "__name_":
    app.run(debug=True, port=5000)

