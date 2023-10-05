import matplotlib.pyplot as plt
import numpy as np
import os
import ezdxf
from classStent import Stent

def ecriture(stent):
    #spécification de la version dxf
    doc = ezdxf.new("R2010")

    #Créer une nouvelle entité dans l'espace objet
    msp = doc.modelspace() 

    #Créer une ligne droite
    for i in range(stent.tableau_maille.shape[0]):
        for j in range(stent.tableau_maille.shape[1]):
            
            for ii in range(0,stent.tableau_maille[i,j].tab_maille.shape[0]-1,2):   
                msp.add_line(start=[stent.tableau_maille[i,j].tab_maille[ii,0],stent.tableau_maille[i,j].tab_maille[ii,1]], end=[stent.tableau_maille[i,j].tab_maille[ii+1,0],stent.tableau_maille[i,j].tab_maille[ii+1,1]])

            for jj in range(len(stent.tableau_maille[i,j].tab_connecteur)):
                for p in range(0,len(stent.tableau_maille[i,j].tab_connecteur[jj][:,0])-1, 2):
                    msp.add_line(start=[stent.tableau_maille[i,j].tab_connecteur[jj][p,0],stent.tableau_maille[i,j].tab_connecteur[jj][p,1]], end=[stent.tableau_maille[i,j].tab_connecteur[jj][p+1,0],stent.tableau_maille[i,j].tab_connecteur[jj][p+1,1]])
                                   
                    
    #sauvegarder
    doc.saveas('export/stent.dxf')
    print("fichier exporté")
    
def principale(chemin, longueur):
    
    data = np.genfromtxt(chemin, delimiter=',', skip_header = 1)
    dossier = os.path.dirname(chemin) + "/connecteur/"

    if os.path.exists(dossier):
        nom_fichier = []
        for fichier in os.listdir(dossier):
            chemin_fichier = os.path.join(dossier, fichier)
            if os.path.isfile(chemin_fichier):
                nom_fichier.append(chemin_fichier)
                  
        stent1 = Stent(data, nom_fichier, longueur)
        #stent1.Affichage()
        ecriture(stent1)
        
    else:
        print("Le dossier n'existe pas.")
        
   

    
principale("c:/Users/hamri/OneDrive/Bureau/projet stent/mailles/TERUMO/Synergy/DIAMETRE 3/maille_bezier_curve_data.csv",3)
