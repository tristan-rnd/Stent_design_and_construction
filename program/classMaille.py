import numpy as np

class Maille:

    nbr_mailles = 0
    def __init__(self):
        #coordonnes particulieres
        self.x_fin = 0
        self.y_fin = 0
        self.x_debut = 0
        self.y_debut = 0

        #tablau des coordonnees de la maille
        self.tab_maille = np.zeros( (2,2) )

        #tableau 3D des coordonnees des connecteurs
        #1ere dimension = nbr de connecteur
        self.tab_connecteur = np.zeros( (2,2,2) )

        #tableau contenant la maille + les connecteurs
        self.tab = np.zeros( (2,2) )
        
        #met a jour le nombre de mailles cree
        Maille.nbr_mailles += 1

        print("maille créé")
        
    def setTab(self, tab, tab_connecteur):
        #redimensionnement des tableaux
        self.tab = np.zeros( (len(tab[:,0]), 2) )
        self.tab_maille = np.zeros( (len(tab[:,0]), 2) )
        self.tab_connecteur = np.zeros( (len(tab_connecteur), len(tab_connecteur[1,:,1]), 2 ) )

        #initialisation
        self.tab_maille[:,:] = tab[:,:]
        self.tab[:,:] = self.tab_maille[:,:]
        
        self.x_fin = self.tab_maille[-1,0]
        self.y_fin = self.tab_maille[-1,-1]
        self.x_debut = self.tab_maille[0,0]
        self.y_debut = self.tab_maille[0,1]

        for i in range(len(tab_connecteur)):
            self.tab_connecteur[i,:,:] = tab_connecteur[i,:,:]
            self.tab = np.vstack( (self.tab, self.tab_connecteur[i,:,:]) )
