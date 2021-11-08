
from . import app ,db
from flask import jsonify,request
from core.authentification import token_required
from model.users import users
@app.route('/usersList', methods=['GET'])
@token_required
def Users():
    usersList = [{"email":user.email} for user in users.query.all()]

    return jsonify( usersList)
@app.route('/user', methods=['POST'])
def UserCreate():
    data = request.json
    newUser = users(email = data['email'], password = data['password'])
    db.session.add(newUser)
    db.session.commit()

    return {"ok":"ok"}