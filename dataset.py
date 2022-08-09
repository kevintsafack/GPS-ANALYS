"""
DataSet permet de reorganiser les données
#on a remplacer les indice en date et on retiré les paramètres
creation des jours"""
# SUPER PARENT
import pandas as pd
import streamlit as st
#############################################################
class Uplaodss:
    def __init__(self):
        self.data=[]
    def uploid(self):
        st.title("Inserez un fichier CSV ")
        uploaded_files = st.file_uploader("",accept_multiple_files=True)
        S = []
        N = []
        if uploaded_files is not None:
            try:
                for uploaded_file in uploaded_files:
                    dataframe = pd.read_csv(uploaded_file)
                    S.append(dataframe)
                    N.append(uploaded_file.name)
                return S , N
            except:
                return st.write("Please enter an CSV file ")
###########################################################################
###########################################################################
class DataSet :
    def __init__(self,n_d_f):
        self.n_d_f = n_d_f # n_d_f == nom du fichier
    def DataFrame(self):
        data = self.n_d_f #ouverture du fichier en memoir
        data = data.drop(['params'],axis=1) #retire la colone "params"
        data.dt = pd.to_datetime(data.dt) #on converti la colone "dt" en date lisible par pandas
        dte = data.dt # on crée la serie dte (dtaframe à une colone)
        data1 = data.rename(columns={'dt':'dte', 'lat':'lat', 'lng':'lng', 'altitude':'altitude',
                                'angle':'angle', 'speed':"speed"})
        #on renome les colonnes 
        p = pd.concat( [data1,dte] , axis=1 ) # on crée un dataframe par concaténation
        p1= p.set_index('dte') # on l'intancie en fissant son indice comme date
        return p1
########################################################################################################################
        


