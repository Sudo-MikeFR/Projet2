import tkinter as tk
from tkinter import messagebox


class InterfaceConnexion:
    def __init__(self, root, verifier_connexion):
        self.root = root
        self.verifier_connexion = verifier_connexion
        self.root.title("Neffix")
        self.root.geometry("300x200")

        # Titre
        self.label_title = tk.Label(root, text="Neffix", font=("Arial", 20))
        self.label_title.pack(pady=10)

        # Champ de nom d'utilisateur
        self.label_username = tk.Label(root, text="Nom d'utilisateur")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        # Champ de mot de passe
        self.label_password = tk.Label(root, text="Mot de passe")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.pack()

        # Bouton de connexion
        self.button_login = tk.Button(root, text="Connexion", command=self.connexion)
        self.button_login.pack(pady=5)

        # Bouton de quitter
        self.button_quit = tk.Button(root, text="Quitter", command=root.quit)
        self.button_quit.pack(pady=5)

    def connexion(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Appel de la fonction de vérification de connexion
        if self.verifier_connexion(username, password):
            self.ouvrir_nouvelle_fenetre()
        else:
            messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe incorrect")

    def ouvrir_nouvelle_fenetre(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("Nouvelle Fenêtre")
        new_window.geometry("300x200")
        label = tk.Label(new_window, text="Bienvenue!", font=("Arial", 20))
        label.pack(pady=50)
