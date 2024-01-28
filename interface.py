import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from classStent import Stent
from PIL import ImageTk,Image
from pathlib import Path



# Fonction pour créer et afficher la fenêtre principale
def fenetre():
     
    global fichier_label, longueur_label, diametre_label, ok_bouton, fenetre

    # Configuration de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Creation du stent")
    screen_width = fenetre.winfo_screenwidth()
    screen_height = fenetre.winfo_screenheight()
    width = int(screen_width * .33)
    height = int(screen_height * .33)
    
    center_x = int((screen_width - width) / 2)
    center_y = int((screen_height - height) / 2)
    
    fenetre.geometry(f'{width}x{height}+{center_x}+{center_y}')
    fenetre.resizable(False, False)
    fenetre.configure(background='white')
    
    # Image en arriere plan
    try:
        image = Image.open("assets/fond.png")
        img_width, img_height = image.size
        ratio = min(width / img_width, height / img_height)
        new_size = (int(img_width * ratio), int(img_height * ratio))
        image = image.resize(new_size)
        imagetk = ImageTk.PhotoImage(image)
        image_label = tk.Label(fenetre, anchor='s', image=imagetk, background='white')
        image_label.place(relwidth=1, relheight=1)
        image_label.image = imagetk
    except Exception as e:
        print(f"Image de fond non trouvee {e}")
    
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
    fichier = filedialog.askopenfilename(initialdir="Mailles/", title="Sélectionner un fichier")
    if fichier:
        absolute_path = Path(fichier)
        parent_directory = absolute_path.parent.parent.parent
        
        # Get the relative path from the parent directory
        relative_path = absolute_path.relative_to(parent_directory)
    
        fichier_label.config(text=relative_path)
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
    diametre_mm = simpledialog.askfloat("Diamètre en mm", "Entrez le diamètre en mm :")
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
    global fichier_label, longueur_label, diametre_label, fenetre
    fichier = fichier_label.cget("text")
    longueur = longueur_label.cget("text")
    longueur = int(longueur.split(":")[1].strip().split("mm")[0])
    diametre = diametre_label.cget("text")
    diametre = float(diametre.split(":")[1].strip().split("mm")[0])
    fichier = Path(fichier)
    constructeur = fichier.parent.parent.name
    modele = fichier.parent.name
    principale(constructeur, modele, longueur, diametre)
    
    fenetre.withdraw()
    messagebox.showinfo("Stent terminé", "Le stent a été exporté.")
    fenetre.deiconify()

def principale(constructeur, modele, longueur, diametre):
    
    stent1 = Stent(constructeur, modele, longueur, diametre)
    #stent1.Affichage()
    stent1.PrintCaracteristique()
    stent1.ecriture_CSV()
    stent1.ecriture()

fenetre()
