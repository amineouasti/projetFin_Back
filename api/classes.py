from . import app ,db
from flask import jsonify, request, session
from core.authentification import token_required
from model.classification import classification
@app.route('/classesList/<idUser>', methods=['GET'])
@token_required
def classes(idUser):
    
    classesList = [{"id": classe.id ,"name":classe.name} for classe in classification.query.filter_by(id_user =idUser).all()]

    return jsonify( classesList)
@app.route('/classe', methods=['POST'])
@token_required
def classeInsert():
    data = request.json
    newClasse = classification(name = data['name'], id_user = data['id_user'])
    db.session.add(newClasse)
    db.session.commit()

    return {"ok":"ok"}