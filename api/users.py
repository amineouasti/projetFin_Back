
from . import app ,db
from flask import jsonify
from core.authentification import token_required
from model.users import users
@app.route('/usersList', methods=['GET'])
@token_required
def Users():
    usersList = [{"email":user.email} for user in users.query.all()]

    return jsonify( usersList)