"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200



@api.route('/signup', methods=['POST'])
def handle_signup():
    body = request.get_json()
    
    if not body or "email" not in body or "password" not in body:
        return jsonify({"msg": "Faltan datos obligatorios (email y password)"}), 400
        
    user_exists = User.query.filter_by(email=body["email"]).first()
    if user_exists:
        return jsonify({"msg": "El correo ya está registrado"}), 400

    new_user = User(email=body["email"], password=body["password"], is_active=True)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "Usuario creado con éxito"}), 201


@api.route('/login', methods=['POST'])
def handle_login():
    body = request.get_json()
    
    if not body or "email" not in body or "password" not in body:
        return jsonify({"msg": "Faltan datos de inicio de sesión"}), 400

    user = User.query.filter_by(email=body["email"], password=body["password"]).first()
    if not user:
        return jsonify({"msg": "Credenciales inválidas"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({"token": access_token, "user_id": user.id}), 200


@api.route('/private', methods=['GET'])
@jwt_required() 
def handle_private():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    
    if not user:
        return jsonify({"msg": "Usuario no encontrado"}), 404
        
    return jsonify({"msg": f"Acceso concedido al usuario: {user.email}"}), 200
