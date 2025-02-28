# Documentation Complète : Application de Gestion des Contacts

---

## **1. Introduction**
**Objectif** : Développer une application web full-stack pour gérer des contacts (CRUD) avec validation des données et recherche dynamique.  
**Public Cible** : Développeurs, utilisateurs finaux cherchant à organiser des informations de contact.  
**Stack Technique** : HTML/CSS, JavaScript, Flask (Python), SQLite.

---

## **2. Technologies Utilisées**
### **Frontend**
- **HTML5** : Structure de la page (formulaire, tableau, champs de recherche).  
- **CSS3** : Styles intégrés pour le responsive design et l'apparence visuelle.  
  - Exemple : Utilisation de `flexbox` pour l'alignement.  
- **JavaScript (ES6)** :  
  - **DOM Manipulation** : Mise à jour dynamique des contacts.  
  - **Fetch API** : Communication avec le backend (méthodes `GET`, `POST`, `PUT`, `DELETE`).  
  - **Validation Client** : Regex pour les noms, téléphone, et email.  

### **Backend**
- **Flask 2.x** : Framework Python pour les routes et la logique métier.  
- **SQLite3** : Base de données embarquée (fichier `contacts.db`).  
- **Bibliothèques Python** :  
  - `webbrowser` : Ouverture automatique du navigateur.  
  - `re` : Validation des données via regex.  

### **Outils**
- **Visual Studio Code** (recommandé) : Éditeur de code.  
- **Postman** : Test des endpoints API.  

---

## **3. Installation et Configuration**
### **Prérequis**
- Python 3.8+ ([Télécharger Python](https://www.python.org/downloads/)).  
- Pip (gestionnaire de paquets Python).  

### **Étapes**
1. **Cloner le dépôt** :  
   ```bash
   git clone [https://github.com/mulobearielle/gestion-de-contact]
   cd [gestion-de-contact]
   ```
2. **Installer Flask** :  
   ```bash
   pip install flask
   ```
3. **Lancer l'application** :  
   ```bash
   python eng.py
   ```
   - La base de données `contacts.db` est créée automatiquement.  
   - L'application s'ouvre dans le navigateur à `http://127.0.0.1:5000`.  

---

## **4. Structure du Projet**
```
📁 projet/
├── 📄 eng.py            # Backend Flask
├── 📁 templates/
│   └── 📄 eng.html      # Frontend HTML/CSS/JS

```

---

## **5. Fonctionnalités Détaillées**
### **1. Ajout de Contact**
- **Champs requis** : Nom, Prénom, Téléphone.  
- **Validation** :  
  - Nom/Prénom : Lettres, espaces, et tirets uniquement (`[A-Za-zÀ-ÿ\s-]+`).  
  - Téléphone : Format `0991234567` (commence par `099`, `085`, etc.).  
  - Email : Format standard (`user@domain.com`).  

### **2. Recherche Dynamique**
- Filtrage en temps réel par nom, prénom, téléphone, ou email.  
- **Technique** : Événement `onkeyup` et méthode `filter()` en JS.  

### **3. Modification/Suppression**
- **Modification** : Via boîtes de dialogue `prompt()`.  
- **Suppression** : Confirmation implicite (suppression immédiate).  

---

## **6. Documentation de l'API**
| **Endpoint**         | **Méthode** | **Description**                          | **Paramètres (JSON)**                          |
|----------------------|-------------|------------------------------------------|------------------------------------------------|
| `/contacts`          | `GET`       | Liste tous les contacts                  | -                                              |
| `/contact`           | `POST`      | Ajoute un contact                        | `{nom, prenom, telephone, email?, adresse?}`   |
| `/contact/<id>`      | `PUT`       | Met à jour un contact                    | `{nom, prenom, telephone, email?, adresse?}`   |
| `/contact/<id>`      | `DELETE`    | Supprime un contact                      | -                                              |

### **Exemple de Requête POST**
```bash
curl -X POST http://localhost:5000/contact \
  -H "Content-Type: application/json" \
  -d '{
    "nom": "Dupont",
    "prenom": "Marie",
    "telephone": "0997654321",
    "email": "marie@exemple.com"
  }'
```

---

## **7. Validation des Données**
### **Côté Client**
- **HTML5** : Attributs `required`, `pattern`, et `title` pour les messages d'erreur.  
- **JavaScript** :  
  ```javascript
  const nameRegex = /^[A-Za-zÀ-ÿ\s-]+$/;
  const phoneRegex = /^(099|085|081|098|089)\d{7}$/;
  ```

### **Côté Serveur**
- **Flask** : Vérification des regex et gestion des doublons (email/nom).  
  ```python
  def validate_contact(data):
      if not re.match(r"^[A-Za-zÀ-ÿ\s-]+$", data["nom"]):
          return "Nom invalide."
  ```

---

## **8. Base de Données**
### **Schéma de la Table**
```sql
CREATE TABLE contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    telephone TEXT,
    email TEXT,
    adresse TEXT
);
```

### **Requêtes SQL Exemple**
- **Insertion** :  
  ```sql
  INSERT INTO contacts (nom, prenom, telephone) 
  VALUES ('Martin', 'Luc', '0819876543');
  ```

---

## **9. Tests**
### **Scénarios de Test**
1. **Ajout d'un contact invalide** : Vérifier l'affichage des erreurs.  
2. **Recherche** : Tester avec des termes partiels (ex: "Mar" pour "Marie").  
3. **Suppression** : Confirmer la disparition du contact du tableau.  

---

## **10. Déploiement**
### **Options**
- **Local** : Exécution avec `python eng.py` (développement uniquement).  
- **Production** :  
  - Utiliser un serveur WSGI (ex: Gunicorn).  
  - Déploiement sur Heroku/AWS avec configuration de la base de données.  

---

## **11. Améliorations Futures**
1. **Interface d'Édition Graphique** : Remplacer les `prompt()` par un formulaire modal.  
2. **Authentification** : Ajouter un système de login avec Flask-Login.  
3. **Export de Données** : CSV/Excel via un endpoint `/export`.  

---

## **12. Conclusion**
Cette application démontre une implémentation complète d'un CRUD avec validation robuste et interactions dynamiques. Elle sert de base pour des projets plus complexes tels qu'un CRM ou un annuaire d'entreprise.  

**Code Source** : [[Lien vers GitHub](https://github.com/mulobearielle/gestion-de-contact)] | **Contact** : [mulobearielle0@gmail.com]  
