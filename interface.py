import tkinter as tk
from tkinter import filedialog, simpledialog
from classStent import Stent
import argparse

# Fonction pour créer et afficher la fenêtre principale
def fenetre():
    global fichier_label, longueur_label, diametre_label, ok_bouton

    # Configuration de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Creation du stent")

    # Étiquette pour afficher le chemin du fichier sélectionné
    fichier_label = tk.Label(fenetre, text="")
    fichier_label.pack(padx=10, pady=10)

    # Bouton pour ouvrir la boîte de dialogue de sélection de fichier
    ouvrir_bouton = tk.Button(fenetre, text="Sélectionner un fichier", command=choisir_fichier)
    ouvrir_bouton.pack(padx=10, pady=10)

    # Bouton pour demander le diamètre en mm
    diametre_label = tk.Label(fenetre, text="")
    diametre_label.pack(padx=10, pady=10)
    diametre_bouton = tk.Button(fenetre, text="Demander le diamètre en mm", command=demander_diametre)
    diametre_bouton.pack(padx=10, pady=10)
    
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

# Fonction pour demander à l'utilisateur d'entrer le diametre en mm
def demander_diametre():
    global diametre_label, ok_bouton
    diametre_mm = simpledialog.askinteger("Diamètre en mm", "Entrez le diamètre en mm :")
    if diametre_mm is not None:
        diametre_label.config(text=f"Diamètre : {diametre_mm} mm")
        activer_bouton_ok()

# Fonction pour activer le bouton OK
def activer_bouton_ok():
    global fichier_label, longueur_label, diametre_label, ok_bouton
    if fichier_label.cget("text") and longueur_label.cget("text") and diametre_label.cget("text"):
        ok_bouton.config(state=tk.NORMAL)
    else:
        ok_bouton.config(state=tk.DISABLED)

# Fonction pour effectuer une action lorsque le bouton OK est cliqué
def action_ok():
    global fichier_label, longueur_label, diametre_label
    fichier = fichier_label.cget("text")
    longueur = longueur_label.cget("text")
    longueur = int(longueur.split(":")[1].strip().split("mm")[0])
    diametre = diametre_label.cget("text")
    diametre = int(diametre.split(":")[1].strip().split("mm")[0])
    principale(fichier, longueur, diametre)

def stent_fini():
    # Création de la fenêtre 
    fenetre = tk.Tk()
    fenetre.title("Stent exporte")

    # Création d'un widget Label (étiquette) pour afficher le texte
    etiquette = tk.Label(fenetre, text="stent exporte")

    # Placement du widget Label dans la fenêtre
    etiquette.pack(padx=10, pady=10)

    # Lancement de la boucle principale Tkinter
    fenetre.mainloop()

def principale(chemin, longueur, diametre):
    nbr_couronne = 8
    stent1 = Stent(chemin, nbr_couronne, longueur, diametre)
    stent1.Affichage()
    stent1.PrintCaracteristique()
    stent1.ecriture()
    stent_fini()

fenetre()
