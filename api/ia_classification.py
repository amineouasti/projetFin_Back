
from . import app ,db
import os
from flask import jsonify, request, session,flash
from core.authentification import token_required
from model.classification import classification
from werkzeug.utils import secure_filename
from core.image_resolution import imageResolution
from werkzeug.datastructures import  FileStorage
from tensorflow.keras.preprocessing import image as image_utils
from tensorflow.keras.applications.imagenet_utils import decode_predictions
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
import cv2
import json
from pycocotools.coco import COCO
UPLOAD_FOLDER ='./static' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
@app.route('/classification/<folderName>', methods=['GET'])

def getClassification(folderName):
    result = []   
    folderClasse ="./static/"+folderName
    if not os.path.exists(folderClasse+"/data.json"):
        result = classif(folderClasse,folderName)
        
        with open(folderClasse+"/data.json","w") as data:
            json.dump(result,data)
        return jsonify(result)
    else:
        with open(folderClasse+"/data.json", 'r') as outfile:
           return jsonify(json.load(outfile))

@app.route('/updateClasse/<folderName>', methods=['GET'])

def updateClassification(folderName):
    os.remove("./static/"+folderName+"/data.json")
    return getClassification(folderName)
def classif(folderClasse,folderName):
    result = []
    dataDir='..'
    dataType='val2017'
    
    for file in os.listdir(folderClasse):
        filePath = folderClasse+"/"+file
        image = image_utils.load_img(filePath, target_size=(224, 224))
        image = image_utils.img_to_array(image)
        
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)
        # load the VGG16 network pre-trained on the ImageNet dataset
        print("[INFO] loading network...")
        model = VGG16(weights="imagenet")
        preds = model.predict(image)
        P = decode_predictions(preds)
        (imagenetID, label, prob) = P[0][0]
        result.append({ "image":"http://localhost:5000/pictures/"+folderName+"/"+file, "label":label.replace("_"," "),"prob":prob*100 })
        print("Label: {}, {:.2f}%".format(label, prob * 100))  
    return result

@app.route('/updateResolution/<folderName>/<fileName>', methods=['GET'])

def updateResolution(folderName,fileName):
    imageResolution(folderName+"/"+fileName)
   
    return {"ok":"ok"}