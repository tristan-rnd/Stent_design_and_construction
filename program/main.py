import matplotlib.pyplot as plt
import numpy as np
from classMaille import Maille
        
def segmentation(x, y, nbr_echantillon):
    tab = np.zeros( (nbr_echantillon,2) )
    ii = 0
    pas = int(len(x)/nbr_echantillon)
    for i in range(0, nbr_echantillon-1, pas):
        #echantillonage
       tab[ii,0] = x[i*pas]
       tab[ii,1] = y[i*pas]
       tab[ii+1,0] = x[i*pas+1]
       tab[ii+1,1] = y[i*pas+1]
       ii += 2

    #ajout connecteur 1
    connecteur1 = np.array([[tab[-1,0], -0.55], [tab[-1,0], -0.25], [tab[-1,0], 0.3], [tab[-1,0], 0.6]])    
    
    #ajout connecteur 2
    connecteur2 = np.array([[2*np.pi/3, -0.55], [2*np.pi/3, -0.75], [2*np.pi/3, -1], [2*np.pi/3, -1.3]])    

    return tab, connecteur1, connecteur2


def principale():
    x = np.linspace(0, np.pi, 1000)
    a = 0.55
    y = a * np.sin(6*x - np.pi/2)

    connecteur = np.zeros( (2,4, 2) )
    liste, connecteur[0,:,:], connecteur[1,:,:] = segmentation(x, y, 500)

    maille1 = Maille()
    maille1.setTab(liste, connecteur)

    plt.plot(maille1.tab[:,0], maille1.tab[:,1], "+")
    plt.plot(x,y)
    plt.show()

principale()
