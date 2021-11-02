
from . import app 

@app.route('/classes', methods=['GET'])
def Classes():
    return 'it works'