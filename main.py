from classe.classStent import Stent
from igeswrite import Iges

def ecriture(stent):
    "Ecriture d'un fichier IGES a partir des aretes"

    doc = Iges()
    for arete in stent.liste_aretes:
        doc.line((arete[0][0],arete[0][1],0),(arete[1][0],arete[1][1],0))

    doc.write("stent.iges")
    print("fichier exporté")
       
def principale(chemin, longueur):    
    stent1 = Stent( chemin, 2,longueur)
    #stent1.Affichage()
    ecriture(stent1)     
   
    
principale('/workspaces/Stent_design_and_construction/Mailles/Terumo/Synergy/Maille.csv',3)
