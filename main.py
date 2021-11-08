import api.users
import api.classes
import api.login
from api import app 
from flask_cors import CORS
#api.add_resource(Users)
if __name__ == "__main__":
    CORS(app)
    app.run(debug=True)