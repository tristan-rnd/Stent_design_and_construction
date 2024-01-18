import numpy as np
import os


class Maille:
    '''
    une maille est un tableau numpy a 2D 
    1ere colonne = valeur x
    2eme colonne = valeur y
    nbr de lignes = nbr de points
    '''
    def __init__(self):
        #valeur particuilere 
        self.largeur = 0
        self.longueur = 0
        self.longueur_c = 0 #longueur entre le bas de la maille et le 1er connecteur
        
        #tablau des coordonnees des point de la maille
        self.tab_maille_point = np.zeros( (2,2) )

        #liste des coordonnees des connecteurs
        self.liste_connecteurs = [] #liste de tableau
        
        #liste des coordonnees des aretes
        self.liste_aretes = [] #liste de liste de tuple. une liste = 2 tuples; 1 tuples = coordonnees (x, y)
        
        
    def SetTab(self, type_maille, fin, longueur, diametre):
        
        #redimensionnement et initialisation de la maille
        tab = np.genfromtxt(type_maille, delimiter=',', skip_header = 1)
        self.tab_maille_point = np.zeros( (len(tab[:,0]), 2) )
        self.tab_maille_point[:,:] = tab[:,:]

        #calcul echelle
        #x
        self.ex = longueur / (8*abs(np.max(tab[:,0])-np.min(tab[:,0])))

        #y
        self.ey = np.pi * diametre / abs(np.max(tab[:,1])-np.min(tab[:,1]))

        self.tab_maille_point[:,0] = self.tab_maille_point[:,0] * self.ex
        self.tab_maille_point[:,1] = self.tab_maille_point[:,1] * self.ey
        
        #recupere les fichier des connecteurs
        dossier = os.path.dirname(type_maille) + "/connecteur/"
        if os.path.exists(dossier):
            nom_fichier = []
            for fichier in os.listdir(dossier):
                chemin_fichier = os.path.join(dossier, fichier)
                if os.path.isfile(chemin_fichier):
                    nom_fichier.append(chemin_fichier)
        else:
            print("Le dossier n'existe pas.")

        if len(nom_fichier) == 4:
            x_largeur_f = 0
            x_largeur_d = 0
            y_longueur_d = 0
            y_longueur_f = 0
            y_longueur_cd = 0
            y_longueur_cf = 0
            for i in range(len(nom_fichier)):
                #initialisation connecteur
                tab_connecteur = np.genfromtxt(nom_fichier[i], delimiter=',', skip_header = 1)
                tab_connecteur[:,0] = tab_connecteur[:,0]*self.ex
                tab_connecteur[:,1] = tab_connecteur[:,1]*self.ey
                
                #calcul longueur et largeur de maille
                nom_fichier_connecteur = os.path.basename(os.path.normpath(nom_fichier[i]))
                if nom_fichier_connecteur == 'Connecteur_bas.csv':
                    self.liste_connecteurs.append(tab_connecteur)
                    for j in range(len(self.liste_connecteurs[i][:,0])-1):
                        #debut arrete
                        x_debut = self.liste_connecteurs[i][j,0]
                        y_debut = self.liste_connecteurs[i][j,1]

                        #fin arrete
                        x_fin = self.liste_connecteurs[i][j+1,0]
                        y_fin = self.liste_connecteurs[i][j+1,1]

                        #ajout a la liste d'arrete
                        self.liste_aretes.append([ (x_debut, y_debut),(x_fin, y_fin) ])
                        
                    y_longueur_f = tab_connecteur[np.argmax(tab_connecteur[:,0]), 1]
                    
                elif nom_fichier_connecteur == 'Connecteur_droit.csv':
                    x_largeur_f = max(tab_connecteur[:,0])
                    y_longueur_cf = tab_connecteur[np.argmax(tab_connecteur[:,0]), 1]

                    if(fin==False):
                        self.liste_connecteurs.append(tab_connecteur)
                        for j in range(len(self.liste_connecteurs[i][:,0])-1):
                            #debut arrete
                            x_debut = self.liste_connecteurs[i][j,0]
                            y_debut = self.liste_connecteurs[i][j,1]

                            #fin arrete
                            x_fin = self.liste_connecteurs[i][j+1,0]
                            y_fin = self.liste_connecteurs[i][j+1,1]

                            #ajout a la liste d'arrete
                            self.liste_aretes.append([ (x_debut, y_debut),(x_fin, y_fin) ])
                    else:
                        self.liste_connecteurs.append([])
                    
                elif nom_fichier_connecteur == 'Connecteur_gauche.csv':
                    x_largeur_d = max(tab_connecteur[:,0])
                    y_longueur_cd = tab_connecteur[np.argmax(tab_connecteur[:,0]), 1]
                    
                elif nom_fichier_connecteur == 'Connecteur_haut.csv':
                    self.liste_connecteurs.append(tab_connecteur)
                    for j in range(len(self.liste_connecteurs[i-1][:,0])-1):
                        #debut arrete
                        x_debut = self.liste_connecteurs[i-1][j,0]
                        y_debut = self.liste_connecteurs[i-1][j,1]

                        #fin arrete
                        x_fin = self.liste_connecteurs[i-1][j+1,0]
                        y_fin = self.liste_connecteurs[i-1][j+1,1]

                        #ajout a la liste d'arrete
                        self.liste_aretes.append([ (x_debut, y_debut),(x_fin, y_fin) ])
                        
                    y_longueur_d = tab_connecteur[np.argmax(tab_connecteur[:,0]), 1]
                    
            self.largeur =  abs(x_largeur_f - x_largeur_d)
            self.longueur = abs(y_longueur_f - y_longueur_d)
            self.longueur_c = abs(y_longueur_cf - y_longueur_cd)        
        

        #initialisation de la liste d'arrete
        for i in range(len(self.tab_maille_point[:,0])-1):
            #debut arrete
            x_debut = self.tab_maille_point[i,0]
            y_debut = self.tab_maille_point[i,1]

            #fin arrete
            x_fin = self.tab_maille_point[i+1,0]
            y_fin = self.tab_maille_point[i+1,1]

            #ajout a la liste d'arrete
            self.liste_aretes.append([ (x_debut, y_debut),(x_fin, y_fin) ])
            
        
        
    def XYTranslation(self):
        
        #mise a jour position maille
        self.tab_maille_point[:,0] = self.tab_maille_point[:,0] + self.largeur
        self.tab_maille_point[:,1] = self.tab_maille_point[:,1] + self.longueur_c

        #mise a jour position connecteur
        for i in range(len(self.liste_connecteurs)):
            if (len(self.liste_connecteurs[i])!=0):
                self.liste_connecteurs[i][:,0] = self.liste_connecteurs[i][:,0] + self.largeur
                self.liste_connecteurs[i][:,1] = self.liste_connecteurs[i][:,1] + self.longueur_c

        #mise a jour des aretes
        for i in range(len(self.liste_aretes)):
            self.liste_aretes[i][0] = (self.liste_aretes[i][0][0] + self.largeur, self.liste_aretes[i][0][1] + self.longueur_c)
            self.liste_aretes[i][1] = (self.liste_aretes[i][1][0] + self.largeur, self.liste_aretes[i][1][1] + self.longueur_c)
        
            
    def YTranslation(self):
        #mise a jour position maille
        self.tab_maille_point[:,1] = self.tab_maille_point[:,1] + self.longueur

        #mise a jour position connecteur
        for i in range(len(self.liste_connecteurs)):
            if (len(self.liste_connecteurs[i])!=0):
                self.liste_connecteurs[i][:,1] = self.liste_connecteurs[i][:,1] + self.longueur

        #mise a jour des aretes
        for i in range(len(self.liste_aretes)):
            self.liste_aretes[i][0] = (self.liste_aretes[i][0][0], self.liste_aretes[i][0][1] + self.longueur)
            self.liste_aretes[i][1] = (self.liste_aretes[i][1][0], self.liste_aretes[i][1][1] + self.longueur)
        
    
