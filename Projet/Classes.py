from typing import List

# Classe personne
class Personne:
    def __init__(self, nom: str, prenom: str, sexe: str):
        # Initialisation des attributs de base d'une personne
        self.nom = nom
        self.prenom = prenom
        self.sexe = sexe

# Classe Client héritant de Personne
class Client(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_inscription: str, courriel: str, password: str):
        # Appel du constructeur de la classe parente pour initialiser les attributs de Personne
        super().__init__(nom, prenom, sexe)
        # Initialisation des attributs spécifiques à Client
        self.date_inscription = date_inscription
        self.courriel = courriel
        self.password = password
        # Initialisation d'une liste vide pour les cartes de crédit associées
        self.cartes_credit: List[CarteCredit] = []

# Classe Acteur héritant de Personne
class Acteur(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_debut_emploi: str, date_fin_emploi: str, nom_personnage: str, salaire: str):
        # Appel du constructeur de la classe parente pour initialiser les attributs de Personne
        super().__init__(nom, prenom, sexe)
        # Initialisation des attributs spécifiques à Acteur
        self.date_debut_emploi = date_debut_emploi
        self.date_fin_emploi = date_fin_emploi
        self.nom_personnage = nom_personnage
        self.salaire = salaire
        # Initialisation d'une liste vide pour les films associés
        self.films: List[Film] = []

# Classe Employe héritant de Personne
class Employe(Personne):
    def __init__(self, nom: str, prenom: str, sexe: str, date_debut_emploi: str, username: str, password: str, type_acces: bool):
        # Appel du constructeur de la classe parente pour initialiser les attributs de Personne
        super().__init__(nom, prenom, sexe)
        self.date_debut_emploi = date_debut_emploi
        self.username = username
        self.password = password
        self.type_acces = type_acces

# Classe représentant une carte de crédit
class CarteCredit:
    def __init__(self, numero: str, date_expire: str, secret: str):
        self.numero = numero
        self.date_expire = date_expire
        self.secret = secret

# Classe représentant un film
class Film:
    def __init__(self, nom_film: str, duree_film: str, description_film: str):
        self.nom_film = nom_film
        self.duree_film = duree_film
        self.description_film = description_film
        # Initialisation d'une liste vide pour les catégories associées
        self.categories: List[Categorie] = []

# Classe catégorie de film
class Categorie:
    def __init__(self, nom_categorie: str, description_categorie: str):
        self.nom_categorie = nom_categorie
        self.description_categorie = description_categorie
