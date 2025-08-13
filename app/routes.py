from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

data_routes = Blueprint("data_routes", __name__)

@data_routes.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Bienvenido a la API de mi TFB",
        "endpoints": {
            "POST /data": "Insertar un nuevo registro (JSON: {name})",
            "GET /data": "Listar registros",
            "DELETE /data/<id>": "Eliminar un registro por ID"
        }
    })

@data_routes.route("/data", methods=["POST"])
def insert_data():
    data = request.json
    if not data or "name" not in data:
        return {"message": "Name is required"}, 400

    current_data = Data.query.filter_by(name=data["name"]).first()
    if current_data:
        return {"message": "Data already exists"}, 409

    new_data = Data(name=data["name"])
    db.session.add(new_data)
    db.session.commit()
    return {"message": "Data inserted successfully"}, 201

@data_routes.route("/data", methods=["GET"])
def get_all_data():
    data_list = [{"id": data.id, "name": data.name} for data in Data.query.all()]
    return jsonify(data_list), 200

@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    element_to_delete = Data.query.get(id)
    if not element_to_delete:
        return {"message": "Data not found"}, 404

    db.session.delete(element_to_delete)
    db.session.commit()
    return {"message": "Data deleted successfully"}, 200

