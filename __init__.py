from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm3

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
  
@app.route('/decrypt/<string:valeur_chiffree>')
def decryptage(valeur_chiffree):
    try:
        valeur_bytes = valeur_chiffree.encode()  # Conversion str -> bytes
        valeur_dechiffree = f.decrypt(valeur_bytes).decode()  # Déchiffrement + conversion en str
        return f"Valeur décryptée : {valeur_dechiffree}"
    except Exception as e:
        return f"Erreur lors du déchiffrement : {str(e)}"


if __name__ == "__main__":
  app.run(debug=True)

