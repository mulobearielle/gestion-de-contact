from flask import Flask, request, jsonify, render_template
import sqlite3
import webbrowser
import time
import re

app = Flask(__name__)

# Fonction pour exécuter les requêtes SQL
def execute_script(script, params=None, fetch=False):
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(script, params)
        else:
            cursor.execute(script)

        if fetch:  
            result = cursor.fetchall()
        else:
            result = None

        conn.commit()
        return result

    except sqlite3.Error as e:
        print(f"Erreur SQL: {e}")
        return None

    finally:
        cursor.close()
        conn.close()

# Création de la table si elle n'existe pas
execute_script('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    telephone TEXT,
    email TEXT,
    adresse TEXT
);
''')

# Fonction de validation des données
def validate_contact(data):
    # Vérifie si les champs obligatoires sont présents
    if not all(k in data for k in ["nom", "prenom", "telephone"]):
        return "Tous les champs obligatoires (nom, prenom, telephone) doivent être fournis."

    # Vérification du format du nom et prénom (lettres uniquement)
    if not re.match(r"^[A-Za-zÀ-ÿ\s-]+$", data["nom"]):
        return "Le nom ne doit contenir que des lettres et espaces."

    if not re.match(r"^[A-Za-zÀ-ÿ\s-]+$", data["prenom"]):
        return "Le prénom ne doit contenir que des lettres et espaces."

    # Vérification du numéro de téléphone (chiffres uniquement)
    if not re.match(r"^\d+$", data["telephone"]):
        return "Le numéro de téléphone doit contenir uniquement des chiffres."

    return None  # Aucune erreur, la validation est réussie

@app.route("/")
def index():
    return render_template("eng.html")

@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = execute_script("SELECT * FROM contacts", fetch=True)
    return jsonify(contacts)

@app.route("/contact", methods=["POST"])
def add_contact():
    data = request.json
    
    # Validation des données
    error_message = validate_contact(data)
    if error_message:
        return jsonify({"error": error_message}), 400  # Code 400 pour erreur de validation

    execute_script('''
    INSERT INTO contacts (nom, prenom, telephone, email, adresse)
    VALUES (?, ?, ?, ?, ?)
    ''', (data["nom"], data["prenom"], data["telephone"], data.get("email", ""), data.get("adresse", "")))

    return jsonify({"message": "Contact ajouté avec succès"}), 201

@app.route("/contact/<int:id>", methods=["PUT"])
def update_contact(id):
    data = request.json
    
    # Validation des données
    error_message = validate_contact(data)
    if error_message:
        return jsonify({"error": error_message}), 400

    execute_script('''
    UPDATE contacts
    SET nom = ?, prenom = ?, telephone = ?, email = ?, adresse = ?
    WHERE id = ?
    ''', (data["nom"], data["prenom"], data["telephone"], data.get("email", ""), data.get("adresse", ""), id))

    return jsonify({"message": "Contact mis à jour"}), 200

@app.route("/contact/<int:id>", methods=["DELETE"])
def delete_contact(id):
    execute_script("DELETE FROM contacts WHERE id = ?", (id,))
    return jsonify({"message": "Contact supprimé"}), 200

if __name__ == "__main__":
    url = "http://127.0.0.1:5000"
    print(f"Le serveur démarre sur {url}...")

    time.sleep(1)  # Attendre un peu pour s'assurer que le serveur est prêt
    webbrowser.open(url)  # Ouvre le navigateur automatiquement

    app.run(debug=True)
