import matplotlib.pyplot as plt
import numpy as np
from classe.classCouronne import Couronne
        
class Stent:
    '''
    le stent est une liste de liste ou chaque liste correspond a une couronne
    '''
    def __init__(self, type_maille, nbr_couronne, longueur):
        self.constructeur = type_maille.split('/')[-3]
        self.model = type_maille.split('/')[-2]
        self.liste_couronne = []
        self.liste_aretes_total = []
        self.liste_aretes = []
        
        #creation du stent 
        for i in range(nbr_couronne):
            couronne = Couronne(self)
            couronne.SetCouronne(type_maille)
            self.liste_couronne.append(couronne) 
            
            if i != 0:  
                for j in range(len(self.liste_couronne[i].liste_maille)):
                    for jj in range(i):
                        self.liste_couronne[i].liste_maille[j].XYTranslation()
                        
            for ii in range(len(self.liste_couronne[i].liste_aretes_couronne)):
                self.liste_aretes_total.append(self.liste_couronne[i].liste_aretes_couronne[ii])
                

        #suppression des doublons dans la liste d'aretes
        # Créez un ensemble pour stocker les tuples déjà rencontrés
        tuples_deja_vus = set()

        for sous_liste in self.liste_aretes_total:
            ensemble_de_tuples = str(sous_liste)

            # Si l'ensemble de tuples n'a pas déjà été rencontré, ajoutez-le au résultat
            if ensemble_de_tuples not in tuples_deja_vus:
                self.liste_aretes.append(sous_liste)
                # Ajoutez l'ensemble de tuples à l'ensemble des tuples déjà rencontrés
                tuples_deja_vus.add(ensemble_de_tuples)
         
            
        print("stent créé")
        
    def PrintCaracteristique(self):
        print("le manufacturier est: ", self.constructeur, "\nle model est: ", self.model, "\nle diametre est: ", self.diametre)

    def Affichage(self):
        
        fig1 = plt.subplot(2, 1, 1)
        for i in range(len(self.liste_couronne)):
            for j in range(len(self.liste_couronne[i].liste_maille)):
                #affichage maille
                fig1.plot(self.liste_couronne[i].liste_maille[j].tab_maille_point[:,0], self.liste_couronne[i].liste_maille[j].tab_maille_point[:,1])
                #plt.plot(self.liste_couronne[i].liste_maille[j].tab_maille_point[:,0], self.liste_couronne[i].liste_maille[j].tab_maille_point[:,1])

                for ii in range(len(self.liste_couronne[i].liste_maille[j].liste_connecteurs)):
                    #affichage connecteur
                    fig1.plot(self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,0], self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,1])
                    #plt.plot(self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,0], self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,1])

                 
        fig2 = plt.subplot(2, 1, 2)
        for i in range(len(self.liste_aretes)):
            x = [self.liste_aretes[i][0][0], self.liste_aretes[i][1][0] ]
            y = [self.liste_aretes[i][0][1], self.liste_aretes[i][1][1] ]
            fig2.plot(x, y)
        
        plt.show()

    
