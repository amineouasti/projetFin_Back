import jwt
from flask import jsonify,request
from api import app
from functools import wraps
def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'token is missing'}), 403
        
        data = jwt.decode(token, app.config['SECRET_KEY'],algorithms='HS256')
   
        return f(*args, **kwargs)
    return decorated