
from . import app ,db
from flask import jsonify,request, make_response, session
import jwt
from model.users import users
import datetime
from flask_cors import CORS, cross_origin


app.permanent_session_lifetime = datetime.timedelta(minutes=30)

@app.route('/login', methods=['GET','POST'])

def login():
    auth = request.authorization
    
    if auth :
        user = users.query.filter_by(email = auth.username,password =auth.password ).first()
        if user:
           
            session.permanent = True
            token = jwt.encode({'email' : auth.username,'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm="HS256" )
        
            return jsonify({'token':token, 'id':user.id})
    

    return make_response('could not verify!', 401, {'Auth':'Basic ralm="login required"'})
