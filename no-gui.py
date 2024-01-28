# --------------------------------------------------------------------------------
# Auteurs : Nassim HAMRI & Tristan RENAUD
# Date : Janvier 2024
# 
# Ce fichier est partie intégrante de Stent_design_and_construction écrit par les mêmes auteurs.
# --------------------------------------------------------------------------------

import argparse

from classStent import Stent
def principale(constructeur, modele, longueur, diametre, verbose):

        
    stent1 = Stent(constructeur, modele, longueur, diametre)
    #stent1.Affichage()
    if verbose: 
        stent1.PrintCaracteristique()
    stent1.ecriture_CSV()
    stent1.ecriture()
    
parser = argparse.ArgumentParser(
                    prog='Construction de stent',
                    description='Ce programme construit un stent 2D complet a partir des entrees',
                    add_help=False)
parser.add_argument('Constructeur', help="Constructeur du stent (Terumo)")
parser.add_argument('Modele', help="Modele du stent (Synergy)")
parser.add_argument('Diametre', type=float, help="Diametre du stent (en mm)")
parser.add_argument('Longueur', type=float, help="Longueur du stent (en mm)")
parser.add_argument('-v', '--verbose', action='store_true', help="Affiche les caractéristiques retenus pour le stent")
parser.add_argument('-h', '--help', action='help', help="Affiche l'aide et termine le programme")
args = parser.parse_args()

principale(args.Constructeur, args.Modele, args.Longueur, args.Diametre, args.verbose)
