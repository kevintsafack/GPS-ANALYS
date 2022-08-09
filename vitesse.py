#Cette classe calcule la vitesse moyenne d'un dataset
class Vitesse:
    def __init__ (self,n_d_f):
        self.n_d_f = n_d_f
    def vitesse(self) :
        vites=[]
        for (index, row) in self.n_d_f .iterrows():
            vites.append(row.loc['speed'])
        v2=[]
        for i in range(len(vites)) : 
            if vites[i]!=0 : 
                v2.append(vites[i])
            
        if len(v2)>0:
            p=sum(v2)/len(v2)
            d=round(p, 2)
            return d
        else :
            v2=[0]
            p=sum(v2)/len(v2)
            d=round(p,2)   
            return d
        
        
