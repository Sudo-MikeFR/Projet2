from typing import List

# Classe de base représentant une personne
class Personne:
    def __init__(self, nom: str, prenom: str, sexe: str):
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

# Classe Client héritant de Personne
class Client(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_inscription: str, courriel: str, password: str):
        super().__init__(nom, prenom, sexe)
        self.date_inscription = date_inscription  # Date d'inscription
        self.courriel = courriel  # Courriel unique
        self.password = password  # Mot de passe
        self.cartes_credit: List[CarteCredit] = []  # Liste pour les cartes de crédit

# Classe Acteur héritant de Personne
class Acteur(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_debut_emploi: str, date_fin_emploi: str, nom_personnage: str, salaire: str):
        super().__init__(nom, prenom, sexe)
        self.date_debut_emploi = date_debut_emploi  # Date de début d'emploi
        self.date_fin_emploi = date_fin_emploi  # Date de fin d'emploi
        self.nom_personnage = nom_personnage  # Nom du personnage joué
        self.salaire = salaire  # Salaire de l'acteur
        self.films: List[Film] = []  # Liste des films

# Classe Employe héritant de Personne
class Employe(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_debut_emploi: str, username: str, password: str, type_acces: str):
        super().__init__(nom, prenom, sexe)
        self.date_debut_emploi = date_debut_emploi  # Date de début d'emploi
        self.username = username  # Nom d'utilisateur
        self.password = password  # Mot de passe
        self.type_acces = type_acces  # Type d'accès (admin ou lecture)

# Classe représentant une carte de crédit
class CarteCredit:
    def __init__(self, numero: str, date_expire: str, secret: str):
        self.numero = numero  # Numéro de la carte
        self.date_expire = date_expire  # Date d'expiration
        self.secret = secret  # Code secret (3 chiffres)

# Classe représentant un film
class Film:
    def __init__(self, nom_film: str, duree_film: str, description_film: str):
        self.nom_film = nom_film  # Nom du film
        self.duree_film = duree_film  # Durée du film
        self.description_film = description_film  # Description du film
        self.categories: List[Categorie] = []  # Liste des catégories

# Classe représentant une catégorie de film
class Categorie:
    def __init__(self, nom_categorie: str, description_categorie: str):
        self.nom_categorie = nom_categorie  # Nom de la catégorie
        self.description_categorie = description_categorie  # Description de la catégorie

#création d'un exemple d'employe pour la connexion
exemple_employe = [
    Employe(nom="test",prenom="test",sexe="M",date_debut_emploi="2024-01-06",username="admin",password="admin",type_acces="admin"),
    Employe(nom="test2",prenom="test2",sexe="M",date_debut_emploi="2024-01-06",username="test",password="test",type_acces="lecture")
    ]
