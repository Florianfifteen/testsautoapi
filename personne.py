#!/usr/bin/env python
# encoding: utf-8

import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine
from flask_cors import *

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'personnes',
    'host': 'localhost',
    'port': 27017
}

api_v1_cors_config = {
  "origins": ["*"],
  "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE"],
  "allow_headers": ["Authorization", "Access-Control-Allow-Origin", "content-type"]
}
CORS(app, resources={"/*": api_v1_cors_config})


db = MongoEngine()
db.init_app(app)


class Personne(db.Document):
    nom = db.StringField(max_length=255)
    prenom = db.StringField(max_length=255)
    naissance = db.StringField(max_length=255)
    postale = db.IntField()
    email = db.StringField(max_length=255)
    tel = db.StringField(max_length=255)

@app.route("/")
@cross_origin() # allow all origins all methods.
def helloWorld():
  return "<h1>Ajouter une personne</h1><form action='/personne/addtraitement' method='POST'> <input name='nom' placeholder='nom'><input name='prenom' placeholder='prenom'><input name='naissance' placeholder='naissance'><input name='postale' placeholder='postale'><input name='email' placeholder='email'><input name='tel' placeholder='tel'><input type='submit'></form><br><h1>Supprimer une personne</h1><form action='/personne/deletetraitement' method='POST'> <input name='nom' placeholder='nom'><input name='prenom' placeholder='prenom'><input type='submit'></form><br><a href='/personne'>Observer les personnes disponibles</a>"


@app.route("/up")  
def up():
    """
    Just for test if API is up

    Returns :
    {string} -- ok if API is up
    """
    return "ok"

def test_up():
    assert up() == "ok"


# Route : /personne
# Méthode : GET
# Récupérer les infos de toutes les personnes
@app.route('/personne', methods=['GET'])
def query_records():
    tab_personnes = []
    for p in Personne.objects:
        tab_personnes.append(p)
    return jsonify(tab_personnes)

# Route : /personne/only?nom=HOCHART&prenom=Florian
# Méthode : GET
# Récupérer une personne
@app.route('/personne/only', methods=['GET'])
def query_record():
    nom = request.args.get('nom')
    prenom = request.args.get('prenom')
    personne = Personne.objects(nom=nom, prenom=prenom).first()
    if not personne:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(personne.to_json())

# Route : /personne
# Méthode : POST
# Saisir une personne 
@app.route('/personne/addtraitement', methods=['GET','POST'])
@cross_origin() # allow all origins all methods.
def create_record():
    record = request.form
    pnom=record['nom']
    pprenom=record['prenom']
    pnaissance=record['naissance']
    ppostale=record['postale']
    pemail=record['email']
    ptel=record['tel']
    personne = Personne(nom=pnom, prenom=pprenom,naissance=pnaissance, postale=ppostale, email=pemail, tel=ptel)
    personne.save()
    return jsonify(personne.to_json())
    

# Route : /personne
# Méthode : DELETE
# Supprimer une personne 
@app.route('/personne/deletetraitement', methods=['GET','POST','DELETE'])
@cross_origin() # allow all origins all methods.
def delete_record():
    record = request.form
    pnom=record['nom']
    pprenom=record['prenom']
    nom = pnom
    prenom = pprenom
    personne = Personne.objects(nom=nom, prenom=prenom).first()
    if not personne:
        return jsonify({'error': 'data not found'})
    else:
        personne.delete()
    return jsonify(personne.to_json())


if __name__ == "__main__":
    app.run(debug=True)