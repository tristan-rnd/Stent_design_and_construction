# --------------------------------------------------------------------------------
# Auteurs : Nassim HAMRI & Tristan RENAUD
# Date : Janvier 2024
# 
# Ce fichier est partie intégrante de Stent_design_and_construction écrit par les mêmes auteurs.
# --------------------------------------------------------------------------------

import argparse

from classStent import Stent
def Principale(constructeur, modele, longueur, diametre, verbose, plot_stent):

        
    stent1 = Stent(constructeur, modele, longueur, diametre)
    if plot_stent:
        stent1.Affichage()
    if verbose: 
        stent1.PrintCaracteristique()
    stent1.Ecriture_CSV()
    stent1.Ecriture()
    
parser = argparse.ArgumentParser(
                    prog='Construction de stent',
                    description='Ce programme construit un stent 2D complet a partir des entrees',
                    add_help=False)
parser.add_argument('Constructeur', help="Constructeur du stent (Terumo)")
parser.add_argument('Modele', help="Modele du stent (Synergy)")
parser.add_argument('Diametre', type=float, help="Diametre du stent (en mm)")
parser.add_argument('Longueur', type=int, help="Longueur du stent (en mm)")
parser.add_argument('-v', '--verbose', action='store_true', help="Affiche les caracteristiques retenus pour le stent")
parser.add_argument('-p', '--plot', action='store_true', help="Trace le stent construit dans une nouvelle fenetre")
parser.add_argument('-h', '--help', action='help', help="Affiche l'aide et termine le programme")
args = parser.parse_args()

Principale(args.Constructeur, args.Modele, args.Longueur, args.Diametre, args.verbose, args.plot)
