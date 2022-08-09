#import pandas as pd
from distance import *
from vitesse import *
class Temps:
    def __init__ (self,D,V,n_j,t_j=24):
        self.D = D #Distance parcourue
        self.V = V #Vitesse moyenne
        self.n_j = n_j #Nombre de jours sur lesquels'etale le dataset
        self.t_j = t_j # temps journalier
    def temps(self):
        
        #cette methode convertir une heure en valeur réel en tenant compte de la duré d'une journée
        #elle le met sous format texte  : '65j1h0m0s'
        def conve1(heure,n):
              if int(heure) < n:
                    h=int(heure)
                    m=(heure%1)*60
                    mi=int(m)
                    s=int((m%1)*60)
                    p=f'{h}h{mi}m{s}s' 
                    return p
              else :
                    j=int((heure-heure%n)/n)
                    x=heure%n
                    h=int(x)
                    m=(x%1)*60
                    mi=int(m)
                    s=int((m%1)*60)
                    p=f'{j}j{h}h{mi}m{s}s' 
                    return p
        
        def division_d_v(D,V):
            if V != 0 :
                T = round(D/V , 2)
            else :
                T = 0
            return T
        
        temps_mobil = division_d_v(self.D,self.V)
        temps_immobile =round(self.t_j*self.n_j - temps_mobil , 2)
        
        return temps_mobil , temps_immobile , conve1(temps_mobil,self.t_j) , conve1(temps_immobile,self.t_j)
        
#temps _immobile; période d'immobilité ; nom de la voiture

# PP == valeur de date traçable qui sera  utilise pour le graphe tu temps mis
# tp1 == la valeur en text du temps mis qui sera affiché sur le graphe
# t == valeur de la vitsse en nombre réel
# 
class Tem :
    def __init__(self,dataframe,nn=1,p=24):
        self.nn = nn
        self.p = p
        self.dataframe = dataframe
    def temps(self):
        S = self.dataframe[1]
        Q = self.dataframe[2]
        Z = Ordre(Q).Periodes()
        d_1 = Groupes(Q,Z[0],1).G_J_S_M()
        d = Groupes(Q,d_1[1],self.nn).G_J_S_M()
        g = [] #☺ regrouper les intervalle de date
        if self.nn > 1 :
            for i in range(len(d[0])):
                g.append(d[0][i][0]+"--"+d[0][i][-1])
        else :
            for i in range(len(d[0])):
                g.append(d[0][i][0])
        O = [] # liste des distances par intervalle
        V = [] 
        T = []
        for i in range(len(d[1])):
            if len(d[0][i]) == 1:
                print(i)
                d_1 = Distance(S.loc[d[0][i][0]]).distance()
                v=Vitesse(S.loc[d[0][i][0]]).vitesse()
                O.append(d_1)
                V.append(v)
                T.append(Temps(d_1,v,self.nn,self.p).temps())
                
            else :
                print(i)
                d_1 = Distance(S.loc[d[0][i][0]:d[0][i][-1]]).distance()
                v=Vitesse(S.loc[d[0][i][0]:d[0][i][-1]]).vitesse()
                O.append(d_1)
                V.append(v)
                T.append(Temps(d_1,v,self.nn,self.p).temps())
        t_m = []
        t_i = []
        j_m = []
        j_i = []
        for i in range(len(T)):
            t_m.append(T[i][0])
            t_i.append(T[i][1])
            j_m.append(T[i][2])
            j_i.append(T[i][3])
        Tem = [t_m , j_m , t_i , j_i]
        Tem

        return [self.dataframe[0] , Tem[0] , g , Tem[1]] , [self.dataframe[0] , Tem[2] , g , Tem[3]] # Mobile , Immobile


