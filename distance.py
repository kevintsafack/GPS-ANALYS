
#Cette classe calcul la distance parcouru d'un dataset
from pyroutelib3 import Router #utilisÃ© pour le calcul des distance
router = Router("car")
from Filtrage import *

class Distance :
    def __init__ (self,n_d_f):
        self.n_d_f = n_d_f
        self.Distance_total = []
    def distance(self) :
        distance_par_jour = 0
        Itineraire = []
        if len(self.n_d_f) > 1:
            for (index , row) in self.n_d_f.iterrows() :
                Itineraire.append([row.loc['lat'] , row.loc['lng']]) #matrice de la distance
        
            L = len(Itineraire)
            distance_point_par_point = [] # Tableau de distance point par point(continue)
            distance_cummul_progrssive = [] # initialisation de la distance cumulÃ©e
        
            for i in range(0, L-1,1):
                distance_point_par_point.append(router.distance(Itineraire[i],Itineraire[i+1]))#liste des distances entre deux points
            distance_cummul_progrssive.append(sum(distance_point_par_point))#liste des distances cumulÃ©es
            distance_par_jour = round(distance_cummul_progrssive[-1], 2)
        else :
            distance_par_jour = 0
        return distance_par_jour
        
        
        
# distance totale par jour, somme sur la pÃ©riode , moyene sur la pÃ©riode
    
class Dist :
    def __init__(self,dataframe,nn=1,j_s_m=0):
        self.nn = nn
        self.j_s_m = j_s_m
        self.dataframe = dataframe
    def dist(self):
        S = self.dataframe[1]
        Q = self.dataframe[2]
        Z = Ordre(Q).Periodes()
        d_1 = Groupes(Q,Z[self.j_s_m],1).G_J_S_M()
        nn_1 = len(d_1[1][0])
        d = Groupes(Q,d_1[1],self.nn).G_J_S_M()
        g = [] #☺ regrouper les intervalle de date
        if (self.nn > 1) | (nn_1 >1) :
            for i in range(len(d[1])):
                g.append(d[1][i][0]+"--"+d[1][i][-1])
        else :
            for i in range(len(d[0])):
                g.append(d[0][i][0])
        O = [] # liste des distances par intervalle
        
        for i in range(len(d[1])):
            if len(d[0][i]) == 1:
                d_1 = Distance(S.loc[d[0][i][0]]).distance()
                O.append(d_1)
                
            else :
                d_1 = Distance(S.loc[d[0][i][0]:d[0][i][-1]]).distance()
                O.append(d_1)

        return [self.dataframe[0] , O , g]

