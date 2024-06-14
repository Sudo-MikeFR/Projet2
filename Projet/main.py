import tkinter as tk
from Interface import InterfaceConnexion
from Classes import *

# Fonction pour vérifier les informations d'identification
def verifier_connexion(username, password):
    for employe in exemple_employe:
        if employe.username == username and employe.password == password:
            return True
    return False

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfaceConnexion(root, verifier_connexion)
    root.mainloop()
