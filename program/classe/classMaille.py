import numpy as np
import matplotlib.pyplot as plt

class Maille:
    def __init__(self):
        #coordonnes particulieres
        self.x_fin = 0
        self.y_fin = 0
        self.x_debut = 0
        self.y_debut = 0

        #tablau des coordonnees de la maille
        self.tab_maille = np.zeros( (2,2) )

        self.tab_connecteur = []
        
    def SetTab(self, tab, fichier):
        #redimensionnement des tableaux
        self.tab_maille = np.zeros( (len(tab[:,0]), 2) )
        self.tab_connecteur = []
        
        #initialisation
        self.tab_maille[:,:] = tab[:,:]

        indice_x_fin = np.argmax(self.tab_maille[:,1])
        indice_x_debut = np.argmin(self.tab_maille[:,1])
        
        self.x_fin = self.tab_maille[indice_x_fin, 0]
        self.y_fin = self.tab_maille[indice_x_fin, 1]
        self.x_debut = self.tab_maille[indice_x_debut, 0]
        self.y_debut = self.tab_maille[indice_x_debut, 1]

        if type(fichier[0]) == type(" "):
            for i in range(len(fichier)):
                data = np.genfromtxt(fichier[i], delimiter=',', skip_header = 1)
                self.tab_connecteur.append(data)
        else:
            for i in range(len(fichier)):
                self.tab_connecteur.append(fichier[i])
        
    def Translation(self):
        #calcule translation sur x et y 
        x_translation = abs(np.max(self.tab_connecteur[0][:,0]) - np.max(self.tab_connecteur[1][:,0]))
        y_translation = abs(np.max(self.tab_connecteur[0][:,1]) - np.max(self.tab_connecteur[1][:,1]))

        #mise a jour position maille
        self.tab_maille[:,0] = self.tab_maille[:,0] + x_translation
        self.tab_maille[:,1] = self.tab_maille[:,1] + y_translation

        #mise a jour position connecteur
        for i in range(len(self.tab_connecteur)):
            self.tab_connecteur[i][:,0] = self.tab_connecteur[i][:,0] + x_translation
            self.tab_connecteur[i][:,1] = self.tab_connecteur[i][:,1] + y_translation
            
    def YTranslation(self):
        y_translation = abs(self.y_debut - self.y_fin)
        self.tab_maille[:,1] = self.tab_maille[:,1] + y_translation

        for i in range(len(self.tab_connecteur)):
            self.tab_connecteur[i][:,1] = self.tab_connecteur[i][:,1] + y_translation
        
        
    
