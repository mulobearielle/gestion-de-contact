# Documentation du Projet : Gestion des Contacts

---

## **1. Aperçu du Projet**
**Objectif** : Développer une application web de gestion de contacts permettant d'ajouter, modifier, supprimer et rechercher des contacts.  
**Stack Technologique** :
- **Frontend** : HTML, CSS, JavaScript (validation de formulaire et interactions dynamiques).
- **Backend** : Flask (Python) avec API REST.
- **Base de données** : SQLite.

---

## **2. Fonctionnalités Principales**
### **Frontend**
1. **Formulaire d'ajout** :
   - Validation en temps réel (nom/prénom : lettres uniquement, téléphone : format spécifique, email : format valide).
   - Messages d'erreur explicites.
2. **Liste des contacts** :
   - Affichage dans un tableau (nom, prénom, téléphone, email, adresse).
   - Boutons pour **modifier** ou **supprimer** un contact.
3. **Recherche** :
   - Filtrage dynamique par nom, prénom, téléphone ou email.
4. **Édition/Supression** :
   - Modification via des boîtes de dialogue `prompt`.
   - Suppression instantanée avec confirmation.

### **Backend**
- **API REST** :
  - `GET /contacts` : Récupère tous les contacts.
  - `POST /contact` : Ajoute un nouveau contact.
  - `PUT /contact/<id>` : Met à jour un contact existant.
  - `DELETE /contact/<id>` : Supprime un contact.
- **Validation des données** :
  - Vérification des formats (nom, téléphone, email).
  - Gestion des doublons (nom et email uniques).

### **Base de Données**
- Table `contacts` avec champs :
  - `id` (clé primaire auto-incrémentée).
  - `nom`, `prenom`, `telephone`, `email`, `adresse`.

---

## **3. Installation et Exécution**
### **Prérequis**
- Python 3.x
- Bibliothèques Python : `flask`, `sqlite3`

### **Étapes**
1. **Cloner/Télécharger le projet**.
2. **Installer les dépendances** :
   ```bash
   pip install flask
   ```
3. **Exécuter l'application** :
   ```bash
   python eng.py
   ```
   - La base de données `contacts.db` est créée automatiquement.
   - Le navigateur s'ouvre sur `http://127.0.0.1:5000`.

---

## **4. Documentation de l'API**
| **Endpoint**         | **Méthode** | **Description**                          | **Paramètres (JSON)**                          |
|----------------------|-------------|------------------------------------------|------------------------------------------------|
| `/contacts`          | GET         | Récupère tous les contacts               | -                                              |
| `/contact`           | POST        | Ajoute un contact                        | `{nom, prenom, telephone, email?, adresse?}`   |
| `/contact/<id>`      | PUT         | Met à jour un contact par ID             | `{nom, prenom, telephone, email?, adresse?}`   |
| `/contact/<id>`      | DELETE      | Supprime un contact par ID               | -                                              |

### **Exemple de Requête POST**
```json
{
  "nom": "Dupont",
  "prenom": "Jean",
  "telephone": "0991234567",
  "email": "jean@exemple.com",
  "adresse": "Paris"
}
```

---

## **5. Points Forts et Améliorations Possibles**
### **Points Forts**
- Validation robuste côté client et serveur.
- Interface simple et intuitive.
- Recherche dynamique sans rechargement de page.

### **Améliorations Suggerées**
1. **Interface d'édition** : Remplacer les `prompt` par un formulaire dédié.
2. **Authentification** : Ajouter un système de login pour sécuriser l'accès.
3. **Notifications** : Messages de succès/erreur plus visibles.
4. **Tests automatisés** : Couvrir l'API avec des tests unitaires.

---

## **6. Démonstration**
1. **Ajouter un contact** : Remplir le formulaire et vérifier la validation.
2. **Rechercher** : Taper un nom ou un numéro pour filtrer la liste.
3. **Modifier/Supprimer** : Utiliser les boutons dans la colonne "Actions".

---

## **7. Conclusion**
Ce projet illustre une application CRUD complète avec une stack simple mais efficace. Il peut être étendu pour répondre à des besoins professionnels (gestion de clients, carnet d'adresses, etc.).  
**Code source disponible sur** : [https://github.com/mulobearielle/gestion-de-contact ].
