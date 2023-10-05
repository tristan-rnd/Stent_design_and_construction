import numpy as np
import copy
import matplotlib.pyplot as plt
from classMaille import Maille

class Stent:
    def __init__(self, data, fichier, longueur):
        self.tableau_maille = np.empty( (longueur,10), dtype=object)

        for i in range(len(self.tableau_maille[:,0])):
            for j in range(len(self.tableau_maille[i,:])):
                element = Maille()
                if i==0 and j==0:
                    element.SetTab(data, fichier)
                    
                elif j==0:      
                    element.SetTab(self.tableau_maille[i-1,0].tab_maille, copy.deepcopy(self.tableau_maille[i-1,0].tab_connecteur))
                    element.YTranslation()
                    
                else:     
                    element.SetTab(self.tableau_maille[i,j-1].tab_maille, copy.deepcopy(self.tableau_maille[i,j-1].tab_connecteur))
                    element.Translation()
                
                self.tableau_maille[i,j] = element
        
             
        print("stent créé")
            
    def Affichage(self):
        for i in range(len(self.tableau_maille[:,0])):
            for j in range(len(self.tableau_maille[i,:])):
                plt.plot(self.tableau_maille[i,j].tab_maille[:,0], self.tableau_maille[i,j].tab_maille[:,1])
                
                for ii in range(len(self.tableau_maille[i,j].tab_connecteur)):
                    plt.plot(self.tableau_maille[i,j].tab_connecteur[ii][:,0], self.tableau_maille[i,j].tab_connecteur[ii][:,0]) 
                
            
        plt.show()
