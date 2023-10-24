import tkinter as tk
from tkinter import filedialog, simpledialog
from main import principale

# Fonction pour créer et afficher la fenêtre principale
def fenetre():
    global fichier_label, longueur_label, ok_bouton

    # Configuration de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Sélection de fichier et longueur")

    # Étiquette pour afficher le chemin du fichier sélectionné
    fichier_label = tk.Label(fenetre, text="")
    fichier_label.pack(padx=10, pady=10)

    # Bouton pour ouvrir la boîte de dialogue de sélection de fichier
    ouvrir_bouton = tk.Button(fenetre, text="Sélectionner un fichier", command=choisir_fichier)
    ouvrir_bouton.pack(padx=10, pady=10)

    # Bouton pour demander la longueur en mm
    longueur_label = tk.Label(fenetre, text="")
    longueur_label.pack(padx=10, pady=10)
    longueur_bouton = tk.Button(fenetre, text="Demander la longueur en mm", command=demander_longueur)
    longueur_bouton.pack(padx=10, pady=10)

    # Bouton OK (initialement désactivé)
    ok_bouton = tk.Button(fenetre, text="OK", command=action_ok, state=tk.DISABLED)
    ok_bouton.pack(padx=10, pady=10)

    # Démarrer la boucle principale de l'application
    fenetre.mainloop()

# Fonction pour ouvrir la boîte de dialogue de sélection de fichier
def choisir_fichier():
    global fichier_label, ok_bouton
    fichier = filedialog.askopenfilename(initialdir="mailles/", title="Sélectionner un fichier")
    if fichier:
        fichier_label.config(text=fichier)
        activer_bouton_ok()

# Fonction pour demander à l'utilisateur d'entrer une longueur en mm
def demander_longueur():
    global longueur_label, ok_bouton
    longueur_mm = simpledialog.askinteger("Longueur en mm", "Entrez la longueur en mm :")
    if longueur_mm is not None:
        longueur_label.config(text=f"Longueur : {longueur_mm} mm")
        activer_bouton_ok()

# Fonction pour activer le bouton OK
def activer_bouton_ok():
    global fichier_label, longueur_label, ok_bouton
    if fichier_label.cget("text") and longueur_label.cget("text"):
        ok_bouton.config(state=tk.NORMAL)
    else:
        ok_bouton.config(state=tk.DISABLED)

# Fonction pour effectuer une action lorsque le bouton OK est cliqué
def action_ok():
    global fichier_label, longueur_label
    fichier = fichier_label.cget("text")
    longueur = longueur_label.cget("text")
    longueur = int(longueur.split(":")[1].strip().split("mm")[0])
    print(f"Fichier sélectionné : {fichier}")
    print(f"Longueur sélectionnée : {longueur}")
    principale(fichier, longueur)

# Appeler la fonction pour créer et afficher la fenêtre principale
fenetre()
