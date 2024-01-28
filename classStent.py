import matplotlib.pyplot as plt
import csv
import os
from classCouronne import Couronne
from igeswrite import Iges

class Stent:
    '''
    le stent est une liste de liste ou chaque liste correspond a une couronne
    '''
    def __init__(self, constructeur, modele, longueur, diametre):
        
        #   TERUMO
        if constructeur == "Terumo" and modele in ["Synergy", "Ultimaster_Nagomi", "Ultimaster_Tansei"]:
            if longueur in [9, 12, 15, 18, 21, 24, 28, 33, 38, 44, 50]:
                if diametre in [2.0, 2.25, 2.50, 3.0, 3.50, 4.0, 4.5]:
                    if 2.0 <= diametre <= 3.0:
                        nbr_couronne = 8
                            
                    if 3.5 <= diametre <= 4.5:
                        nbr_couronne = 10
                        
                else:
                    raise Exception("Le diamètre ne fait pas partie des diamètres autorisés.\n Le diamètre choisi était : {}".format(diametre))
            else:
                raise Exception("La longueur ne fait pas partie des longueurs autorisées.\n La longueur choisie était : {}".format(longueur))

        else:
            raise Exception('Le constructeur et/ou le modele n\'existe pas.\n Le constructeur choisi était : {}\n Le modèle choisi était : {}'.format(constructeur, modele))

            
        #   AUTRES CONSTRUCTEURS    #
        #
        #
        #
        #   AUTRES CONSTRUCTEURS    #
        
        self.constructeur = constructeur
        self.model = modele
        self.diametre = diametre
        self.longueur = longueur
        self.liste_couronne = []
        self.liste_aretes_total = []
        self.liste_aretes = []
        
        #creation du stent
        fin = False #si on est à la fin du stent pour eviter de mettre les connecteurs
        for i in range(nbr_couronne):
            if i == (nbr_couronne - 1):
                fin = True
             
            couronne = Couronne()
            couronne.SetCouronne(constructeur, modele, fin, longueur, diametre, nbr_couronne)
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

            # Si l'ensemble de tuples n'a pas déjà été rencontré
            if ensemble_de_tuples not in tuples_deja_vus:
                self.liste_aretes.append(sous_liste)
                # Ajoutez l'ensemble de tuples à l'ensemble des tuples déjà rencontrés
                tuples_deja_vus.add(ensemble_de_tuples)
         
            
        print("stent créé")
        
    def PrintCaracteristique(self):
        print("Le manufacturier est: ", self.constructeur, "\nLe model est: ", self.model, "\nLe diametre est: ", self.diametre,"\nLa longueur est: ", self.longueur)

    def Affichage(self):
        
        for i in range(len(self.liste_couronne)):
            for j in range(len(self.liste_couronne[i].liste_maille)):
                #affichage maille
                plt.plot(self.liste_couronne[i].liste_maille[j].tab_maille_point[:,0], self.liste_couronne[i].liste_maille[j].tab_maille_point[:,1])

                for ii in range(len(self.liste_couronne[i].liste_maille[j].liste_connecteurs)):
                    #affichage connecteur
                    if (len(self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii])!=0):
                        plt.plot(self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,0], self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,1])

        plt.show()      
        
    def ecriture_CSV(self):
        #creation du dossier
        nom = "Stent_" + str(self.constructeur) + "_" + str(self.model) + "_" + str(self.diametre) + "_" + str(self.longueur)
        path = "export/" + nom + "/"
        if not os.path.exists(path):
            os.makedirs(path)
                
        #ecriture dans un fichier csv des arretes du stent
        with open(path + nom + "_segments.csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([['X1', 'Y1'], ['X2', 'Y2']])

            for arrete in self.liste_aretes_total:
                csv_writer.writerow([arrete[0][0], arrete[0][1], arrete[1][0],arrete[1][1]])

        #ecriture dans un fichier des csv des points du stent
        with open(path + nom + "_points.csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([['X', 'Y']])

            for i in range(len(self.liste_couronne)):
                for j in range(len(self.liste_couronne[i].liste_maille)):
                    csv_writer.writerow([self.liste_couronne[i].liste_maille[j].tab_maille_point[:,0], self.liste_couronne[i].liste_maille[j].tab_maille_point[:,1]])

                    for ii in range(len(self.liste_couronne[i].liste_maille[j].liste_connecteurs)):
                        if (len(self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii])!=0):
                            csv_writer.writerow([self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,0], self.liste_couronne[i].liste_maille[j].liste_connecteurs[ii][:,1]])
                            
    def ecriture(self):
        "Ecriture d'un fichier IGES a partir des aretes"
        doc = Iges()
        for arete in self.liste_aretes:
            doc.line((arete[0][0],arete[0][1],0),(arete[1][0],arete[1][1],0))

        #creation du dossier
        nom = "Stent_" + str(self.constructeur) + "_" + str(self.model) + "_" + str(self.diametre) + "_" + str(self.longueur)
        path = "export/"+nom+"/"
        if not os.path.exists(path):
            os.makedirs(path)
                
        doc.write(path+nom+".iges")
        print("fichier exporté")

    
