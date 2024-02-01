# --------------------------------------------------------------------------------
# Auteurs : Nassim HAMRI & Tristan RENAUD
# Date : Janvier 2024
# 
# Ce fichier est partie intégrante de Stent_design_and_construction écrit par les mêmes auteurs.
# --------------------------------------------------------------------------------

from classMaille import Maille

class Couronne:
    '''
    une couronne est une liste de liste ou chaque liste correspond a une maille
    '''
    def __init__(self):
        self.liste_maille = []
        self.liste_aretes_couronne = []
        
    def SetCouronne(self, constructeur, modele, fin, longueur, diametre, nbr_couronne):
        def Couronnes(nbr_maille):
            for i in range(nbr_maille):
                maille = Maille()
                maille.SetTab(constructeur, modele, fin, longueur, diametre, nbr_couronne, nbr_maille)
                self.liste_maille.append(maille)
                if i != 0:
                    self.liste_maille[i].YTranslation(i)

                #mis a jour liste_aretes_couronne (liste de liste de tuple)
                for j in range(len(self.liste_maille[i].liste_aretes)):
                    self.liste_aretes_couronne.append(self.liste_maille[i].liste_aretes[j])
                
                                                  
        liste_modele_2_mailles = ["Synergy", "Ultimaster_Nagomi", "Ultimaster_Tansei"]
        liste_modele_3_mailles = []
        if modele in liste_modele_2_mailles:
            Couronnes(2)
        elif modele in liste_modele_3_mailles:
            Couronnes(3)
            
        # AUTRES NOMBRE DE MAILLES
        # 
        # ex : Si Boston_scientific & diamètre >=4 alors couronnes = 4
        #
        # if constructeur == "Boston_scientific" and diametre >= 4:
        #     couronnes(4)
        #                         
        # AUTRES NOMBRE DE MAILLES
            
