from classStent import Stent
import argparse
    
def principale(chemin, longueur):
    nbr_couronne = 8
    diametre = 3
    stent1 = Stent(chemin, nbr_couronne ,longueur, diametre)
    stent1.Affichage()
    stent1.PrintCaracteristique()
    stent1.ecriture()
    
principale("c:/Users/hamri/OneDrive/Bureau/projet_stent/mailles/TERUMO/Synergy/DIAMETRE_3/Maille.csv", 9)  
'''
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="main file")
    parser.add_argument("-l","--longueur",type=int,default=1)
    parser.add_argument("-p","--path",type=str,default="r")
    args = parser.parse_args()
    principale(chemin=args.path,longueur=args.longueur)
'''


