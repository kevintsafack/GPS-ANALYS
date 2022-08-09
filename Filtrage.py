import streamlit as st
from dataset import DataSet
from datetime import datetime
from datetime import date
import calendar
import pandas as pd

class Coupure:
    def __init__ (self,n_d_f) :
        self.n_d_f = n_d_f
    def DecoupeEnJour(self):
        F = []
        jour_graphe_abscisse = []
        for i in self.n_d_f.dt :
            
            F.append(str(i)[:10])
        for i in F :
            if F.count(i) > 1 :
                if jour_graphe_abscisse.count(i) == 0 :
                    jour_graphe_abscisse.append(i)
        #st.write(len(self.n_d_f.dt))
       # st.write(jour_graphe_abscisse)
        return jour_graphe_abscisse

#################################################################################################################
#Cette classe permet de filtrer le dataset en fonction des horaise de travai
#Il s'agit d'un masque horaire
#on à egalement la possibilitér de fabriquer un masque qe vitesse en eliminant des valeurs de vitesse inférieur un 
#il prend en entré le fichier , et les horaires de début et de fin
#il hérite de la classe Coupure
#il donne également en sorti le temps journalier
class SeparationEnJour(Coupure):
    def __init__ ( self , n_d_f , debut:str = "00:00:00" , fin:str = "23:59:59" ):
        super().__init__(n_d_f)
        self.debut = " " + debut
        self.fin = " " + fin
        self.time = [fin,debut]
        self.dataset_en_jour = [] 
        for i in super().DecoupeEnJour():
            self.dataset_en_jour.append( n_d_f.loc[i+self.debut : i+self.fin] )
        def c_h(t):
            h=[0]
            y=0
            for i in range(len(t)):
                if t[i].isnumeric():
                    y=y+1
                else:
                    h.append(i)
            h
            return round(int(t[h[0]:h[1]]) + (int(t[h[1]+1:h[2]])/60) + int(t[h[2]+1:])/3600 , 3)
        
        self.x=c_h(self.time[0])-c_h(self.time[1])
        
    def Separe(self):
        E = self.dataset_en_jour
        dataset_construit = E[0]
        for i in range(1,len(E),1):
            dataset_construit = pd.concat( [dataset_construit,E[i]] ,axis=0 )
        
        return dataset_construit , super().DecoupeEnJour()
################################################################################################################
#Cette classe donnes les demaine ainsi que les mois qui contiennent les jours sur lesquels le dataset est répartit
#Cette classe prend en paramètre le fichier (dataset), elle hérite de la class Coupure; 
#car on a besoin des jours sur lesquels le dataset est reparti 

class Ordre :
    def __init__(self , n_d_f ):
        self.n_d_f = n_d_f
        

    def Periodes(self):
        
        def Mois(a1,a2):
            # a1 == année
            # a2 == moi
            # cette fonction retourne les jours du moi dans le format : aaaa-mm-jj
            x=[]
            x_1 = []
            for j in obj.itermonthdates(a1,a2):
                x.append(str(j))
            for i in x:
                if i[5:7].count(str(a2)):
                    x_1.append(i)
            return x_1
        
        Q = self.n_d_f
        #print(len(Q))
        #print(Q)
        #print(len(Q))
        A=[int(Q[0][:4]),int(Q[0][5:7])]
        B=[int(Q[-1][:4]),int(Q[-1][5:7])]
        # A[0],B[0] == l'année
        # A[1],B[1] == mois
        obj = calendar.Calendar()
        #print(len(Q))
        sd = [] # liste de semaines
        d = [] # liste de mois ordonées
        if (A[0]==B[0]) & (A[1]==B[1]) :
            sd.append( obj.monthdatescalendar(A[0], A[1]) )
            d.append(Mois(A[0],A[1]))

        elif (A[0]==B[0]) & (A[1]!=B[1]) :
            obj = calendar.Calendar()
            for i in range(A[1],B[1]+1,1):
                    sd.append(obj.monthdatescalendar(A[0], i))
                    d.append(Mois(A[0],i))
        S=[]
        D=[]
        for i in range(len(sd)):
             for j in sd[i]:
                S.append(j)

        D=[S[0]]
        for k in range(1,len(S),1):
             if S[k]!=D[-1]:

                D.append(S[k])
        Z = [] # liste de semaines ordonées
        for j in range(0,len(D),1):
            s=[]
            for f in range(0,len(D[j]),1):
                s.append(str(D[j][f]))
            Z.append(s)
        
        return Q , Z , d ## liste de semaines ordonées ## liste de mois ordonées


#################################################################################################################
#Cette classe permet de grgrouper les in formation soit en packet de jours, semaine , ou de mois avant de les traiter 
#Elle hérite de la classe  Coupur
class Groupes:
    def __init__(self, n_d_f ,p,n):
        self.n_d_f = n_d_f
        self.n=n
        self.p=p
    def G_J_S_M(self):
        
        def Groupe(p,n):
            # p == liste de semaine ou de jours ou de mois
            # n == nombre de subdivision
            h=[0] # indice de slicing
            z=[]   # liste de subdivision
            #print(len(p))
            if n<=len(p):
                for i in range(0,len(p),1):
                    if i%n==n-1:
                        h.append(i+1)
                h
                for i in range(0,len(h)-1,1):
                    if type(p[0]) != str:
                        z_1=p[h[i]:h[i+1]]
               #         print(1)
                        z_2=z_1[0]
                        for j in range(1,len(z_1),1):
                            z_2 = z_2 + z_1[j]
                        z.append(z_2)
                    else:
                        print(2)
              #          print(p[h[i]:h[i+1]])
                        z.append(p[h[i]:h[i+1]])

                if len(p)%n!=0:
                    q = []
                    try :
                        for i in range(len(p[h[-1]:])):
                            
                            q = q + p[h[-1]:][i]
                        z.append(q)
                    except :
             #           print(p[h[-1]:])
                        z.append(p[h[-1]:])
            else:
                print("La valeur de subdivision doit être infériéure à ",len(p))
            #print(h)
            return z 
        
        S=Groupe(self.p,self.n)
        H=[] # jours , semaines , mois regroupés
        S_1=[] # les jours selectioné dans le liste des jours du dataframe
        for i in range(len(S)):
            G = []
            for j in self.n_d_f :
                if S[i].count(j):
                    G.append(j)
            #print("a",i,G)
            if len(G)!=0:
                H.append(G)
                S_1.append(S[i])
    
    
    
        return H , S_1 # jour du dataset , jour des semaine ou mois