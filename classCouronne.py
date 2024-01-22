from classMaille import Maille

class Couronne:
    '''
    une couronne est une liste de liste ou chaque liste correspond a une maille
    '''
    def __init__(self, parent):
        self.parent = parent
        self.liste_maille = []
        self.liste_aretes_couronne = []
        
    def SetCouronne(self, type_maille, fin, longueur, diametre, nbr_couronne):
        def couronnes(nbr_maille):
            for i in range(nbr_maille):
                maille = Maille()
                maille.SetTab(type_maille, fin, longueur, diametre, nbr_couronne)
                self.liste_maille.append(maille)
                if i != 0:
                    self.liste_maille[-1].YTranslation()

                #mis a jour liste_aretes_couronne (liste de liqte de tuple)
                for j in range(len(self.liste_maille[i].liste_aretes)):
                    self.liste_aretes_couronne.append(self.liste_maille[i].liste_aretes[j])
                
                                                  
        liste_modele_2_mailles = ["Synergy", "Ultimaster_Nagomi", "Ultimaster_Tansei"]

        if self.parent.model in liste_modele_2_mailles:
            couronnes(2)
            
