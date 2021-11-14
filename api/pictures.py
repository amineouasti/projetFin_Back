
from . import app ,db
from flask import jsonify,request, make_response, session,send_from_directory
from core.authentification import token_required
import flask
import os


@app.route('/pictures/<folderName>/<fileName>',methods=['GET'])
def getPictures(folderName,fileName):
    
    return flask.send_file("../static/"+folderName+"/"+fileName)
@app.route('/removePicture/<folderName>/<fileName>',methods=['GET'])
def removePicture(folderName,fileName):
    os.remove("./static/"+folderName+"/"+fileName)
    return {"response":"ok"}
