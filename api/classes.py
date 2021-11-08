from . import app ,db
from flask import jsonify, request, session,flash
from core.authentification import token_required
from model.classification import classification
UPLOAD_FOLDER ='/static' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
@app.route('/classesList/<idUser>', methods=['GET'])
@token_required
def classes(idUser):
    
    classesList = [{"id": classe.id ,"name":classe.name} for classe in classification.query.filter_by(id_user =idUser).all()]

    return jsonify( classesList)
@app.route('/classe', methods=['POST'])
@token_required
def classeInsert():
    print("here")
    print(request.form)
    data = request.form
    '''if 'files' not in request.files:
            flash('No file part')
            
    files = request.files['files']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    for file in files :
        if file.filename == '':
            flash('No selected file')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      '''
    newClasse = classification(name = "data['name']", id_user = "data['id_user']")
    db.session.add(newClasse)
    #db.session.commit()

    return {"id":newClasse.id,"name":newClasse.name}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS