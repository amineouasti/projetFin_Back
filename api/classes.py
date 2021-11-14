from . import app ,db
import os
from flask import jsonify, request, session,flash,send_from_directory
import flask
from core.authentification import token_required

from model.classification import classification
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from tensorflow.keras.preprocessing import image as image_utils
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
import shutil
import cv2
UPLOAD_FOLDER ='./static' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/classesList/<idUser>', methods=['GET'])
@token_required
def classes(idUser):
    
    classesList = [{"id": classe.id ,"name":classe.name} for classe in classification.query.filter_by(id_user =idUser).all()]
    
    return jsonify( classesList)
@app.route('/deleteClasse/<className>/<idUser>', methods=['GET'])
def deleteClasses(className,idUser):
    folder="./static/"+className+"_"+idUser
    
    classe = classification.query.filter_by(id_user =idUser,name = className).first()
    db.session.delete(classe)
    try:
        shutil.rmtree(folder)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
    db.session.commit()
    return {"response" : "ok"}

@app.route('/classe', methods=['POST'])
@token_required
def classeInsert():
 
    data = request.form
    if 'files' not in request.files:
            flash('No file part')
            
    files = request.files.getlist('files')
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    direcoty=app.config['UPLOAD_FOLDER']+"/"+data['nameClass']+"_"+data["id_user"]
    if not os.path.exists(direcoty):
        os.mkdir(direcoty)
    for file in files :
        
        if file.filename == '':
            flash('No selected file')
        
        if file and allowed_file(file.filename):
           
            filename = secure_filename(file.filename)
            file.save(os.path.join(direcoty, filename))
      
    newClasse = classification(name = data['nameClass'], id_user = data['id_user'])
    db.session.add(newClasse)
    db.session.commit()

    return {"id":newClasse.id,"name":newClasse.name}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS