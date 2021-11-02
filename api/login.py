
from . import app ,db
from flask import jsonify,request, make_response
import jwt
from model.users import users

@app.route('/login', methods=['GET','POST'])
def login():
    auth = request.authorization
    if auth and auth.password == 'test' :
        token = jwt.encode({'email' : auth.username}, app.config['SECRET_KEY'],algorithm="HS256" )
        return jsonify({'token':token})
    usersList = [{"email":user.email} for user in users.query.all()]

    return make_response('could not verify!', 401, {'Auth':'Basic ralm="login required"'})