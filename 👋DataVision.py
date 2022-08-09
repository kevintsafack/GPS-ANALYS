import streamlit as st

from dataset import DataSet
from dataset import Uplaodss
from Filtrage import *
from distance import *
from vitesse import *
from temps_mis import *
from graph import *
import json
from streamlit_lottie import st_lottie
import numpy as np
import altair as alt
########## page configuration #############
st.set_page_config(
     page_title=" ",
     page_icon="👋",
     layout="wide",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)
########Calcul de l'horaire d'une journée ##############♦
def c_h(t):
    h=[0]
    y=0
    for i in range(len(t)):
        if t[i].isnumeric():
            y=y+1
        else:
            h.append(i)
    
    return round(int(t[h[0]:h[1]]) + (int(t[h[1]+1:h[2]])/60) + int(t[h[2]+1:])/3600 , 3)
###########
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f :
        return json.load(f)

###########
#################### Nom des animation ###################################
itineraire = load_lottiefile("itineraite.json")
stat = load_lottiefile("stat.json")
question = load_lottiefile("question.json")
traking = load_lottiefile("traking.json")
analys = load_lottiefile("analys.json")
car = load_lottiefile("car.json")
garage = load_lottiefile("garage.json")
analys =load_lottiefile("analys.json")
gps =load_lottiefile("gps.json")
#########################################################################


tab1, tab2, tab3 , tab4 = st.tabs(["Présentation 🎁", " Insérez un 📁", "Distances 🚘 📊" , "Temps ⌚ 📊"])
###################### tab1 = Présentation des différentes animations  #################################
with tab1:
    
    p=200
    n=400
    with st.container():
        col1, col2 , col3  = st.columns(3)
        with col1:
                
                st_lottie( gps,speed=1,reverse=False,loop=True,quality="low",height=p,width=n, key=None,)
                st.title("GPS")
            
        with col2:
                
                st_lottie(question,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("QUESTION")
        with col3:
                
                st_lottie(car,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("MOBILITE")
    with st.container():
        col4 , col5 , col6 = st.columns(3)
        with col4:
                
                st_lottie(itineraire,speed=1,reverse=False,loop=True,quality="low",height=p,width=n, key=None,)
                st.title("Itineraire")
            
        with col5:
                
                st_lottie(stat,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("Statistique")
        with col6:
                
                st_lottie(analys,speed=1,reverse=False,loop=True,quality="low",height=p,width=n,key=None,)
                st.title("ANALYSES")
################################################################♦########################################☺#####
#################################  traiement simple   ######################################
with tab2:
    st.title("Heure journalière")
    if 'data' not in st.session_state:
        st.session_state.data = []
    
    ###### Colonne pour le choix des heures ######
    col1_1 , col1_2 = st.columns(2)
    n_j = 1
    n_s = 1
    n_m = 1
    with col1_1:
         title = st.text_input('Heure de Début : hh:mm:ss',"00:00:00")
         debut = title
         st.write(debut)
    with col1_2:
        title_1 = st.text_input('Heure de Fin : hh:mm:ss',"23:59:59")
        fin = title_1
        st.write(fin)
    ######### Groupage ###############
    st.title("Traitement groupé")
    col2_1 , col2_2 , col2_3 = st.columns(3)
    with col2_1:
         j = st.text_input('Nombre de jour',1)
         try:    
             n_j = int(j)
             st.write(j)
         except:
            st.write("")
    with col2_2:
        s = st.text_input('Nombre de semaine',1)
        try:    
            n_s = int(s)
            st.write(s)
        except:
           st.write("")
    with col2_3:
        m = st.text_input('Nombre de mois',1)
        try:    
            n_m = int(m)
            st.write(m)
        except:
           st.write("")
    ########################
    ###### On charge le fichier ######
    r = Uplaodss().uploid()
    
    
    try:
        
        if 'distance_Jour' not in st.session_state:
            st.session_state.distance_Jour = []
            
        if 'temp_jour_mobile' not in st.session_state:
            st.session_state.temps_jour_mobile = []
            
        if 'temp_jour_immobile' not in st.session_state:
           st.session_state.temps_jour_immobile = []
        
        if 'periode' not in st.session_state:
            st.session_state.periode = []
            
        if 'nom' not in st.session_state:
            st.session_state.nom = []
        
        x = c_h(fin)-c_h(debut) # Calcul du temps d'une Jou
        st.write("Vous considérez qu'une journé fait : ",x , "Heures")
        r_1 = [] # Tableau qui contient les datasets filtré sur l'heure journalié
        for i in range(len(r[0])):
            var_1 = SeparationEnJour(DataSet(r[0][i]).DataFrame() ,debut ,fin ).Separe()
            r_1.append([ r[1][i]  , var_1[0]  , var_1[1]]) # [nom de la voiture , dataset]
        st.session_state.data = r_1 # enrégistre le tableau dans la session courante
        datas = st.session_state.data # Variable sur le Tableau des dataset : datas
        #st.write(datas)
        #st.write(st.session_state.data)
        #st.write("étape1")
        
        
        distance_jour = [] # nom_voiture,dataframe,jours de mobilité
        temps_jour_mobile = []
        temps_jour_immobile = []
        for i in range(len(datas)):
            distance_jour.append(Dist(datas[i],n_j).dist())
            temps_jour_mobile.append(Tem(datas[i],n_j,x).temps()[0])
            temps_jour_immobile.append(Tem(datas[i],n_j,x).temps()[1])
        #st.write("étape2")
        st.session_state.distance_Jour = distance_jour
        st.session_state.temps_jour_mobile = temps_jour_mobile
        st.session_state.temps_jour_immobile = temps_jour_immobile
        #st.title("temps mobile")
        #st.write(st.session_state.temps_jour_mobile)
        #st.title("temps immobile")
        #st.write(st.session_state.temps_jour_immobile)
        
        
        #st.write(st.session_state.distance_Jour)
        #st.write("étape3")
        
        
            
            #st.write(Dist(datas[0],n_j).dist())
            #### DATAFRAME PAR SEMAINE
            #d_1 = Groupes(jr,Z[1],1).G_J_S_M() # CETTE DONN2ES EST TR7S UTILES ? CE SONT LES SEMAINE D4ACTIVIT2
            #d_sem = Groupes(jr,d_1[1],3).G_J_S_M() #semaine CONDITIONE PAR LA TAILLE DE N
            #dat_sem = []
           # for j in range(len(d_sem[0])):
           ##     if len(d_sem[0][j]) == 1:
            #        d = Distance(dat.loc[ d_sem[0][j][0]]).distance()
            #        dat_sem.append([d , "Du " + d_sem[1][j][0] + " au " + d_sem[1][j][-1]  ])
            #    else:
            #        d = Distance(dat.loc[ d_sem[0][j][0]:d_sem[0][j][-1]]).distance()
            #        dat_sem.append([d , "Du ♌" + d_sem[1][j][0] + " au " + d_sem[1][j][-1] ])
            #
            #### DATAFRAME PAR MOIS
            #d_2 = Groupes(jr,Z[2],1).G_J_S_M()
            #d_mois = Groupes(jr,d_2[1],1).G_J_S_M() #mois
            #dat_mois = []
            #for j in range(len(d_mois[0])):
            #    if len(d_mois[0][j]) == 1:
            #        d = Distance(dat.loc[ d_mois[0][j][0]]).distance()
            #        dat_mois.append([d , "Du " + d_mois[1][j][0] + " au " + d_mois[1][j][-1]  ])
            #    else:
            #        d = Distance(dat.loc[ d_mois[0][j][0]:d_mois[0][j][-1]]).distance()
            #        dat_mois.append([d , "Du " + d_mois[1][j][0] + " au " + d_mois[1][j][-1] ])
            #DAT.append([dat_jour , dat_sem , dat_mois])
            #########################################################################################
            #d = Distance(dat).distance()
           # v = Vitesse(dat).vitesse()
           # di.append(d)
           # vi.append(v)
           # Pr.append([d_jour, d_sem ,d_mois])
        
        #st.session_state.vitesse = vi
        #st.session_state.periode = Pr
        #T = [] #temps mis et consort
       # for i in range(len(st.session_state.vitesse)):
       #     d = st.session_state.distance[i]
       #     v = st.session_state.vitesse[i]
       #     Q = Jrs[i]
       #     T.append(Temps(d,v,len(Q),x).temps())
       # st.session_state.temps = T
        
        
        #d=DataSet(datas[0][0]).DataFrame()
        #st.write(d)
        #st.success("-2")
        #Q=Coupure(d).DecoupeEnJour()
        #st.success("-1")
        #p = SeparationEnJour(d).Separe()[1]
        #st.success("0")
        #a=Distance(d).CalculDeDistanceParJour()
        #st.success("1")
        #v=Vitesse(d).Calcul_vitesse_moyenne()
        #st.success("2")
        #t=Temps(a,v,len(Q),p).Calcul_temps()
        #st.session_state.dq
        st.success("Bien chargé 😃")
    except : 
        st.title("Respecteer le format horaire ")
#############################################################################
with tab3:
    try:
        
        st.title(f"on considère qu'une journé à : {x} heures")
        
        nom_car = st.session_state.distance_Jour
        
        name_car = []
        for i in range(len(nom_car)):
            name_car.append([i,nom_car[i][0]])
        option = st.multiselect('Choisir une voiture',name_car,name_car)
        st.session_state.nom = option
        options = st.session_state.nom
        Données = []
        if len(options)==1:
            Graph([nom_car[options[0][0]]]).graph()[0]
            Données.append(Graph([nom_car[options[0][0]]]).graph()[1]) 
        else:
            
            options_1 = []
            for i in range(len(options)):
                options_1.append(nom_car[options[i][0]])
            Graph(options_1).graph()[0]
            Données.append(Graph(options_1).graph()[1])
        
        col1_11,col1_12 = st.columns(2)
        with col1_11:
             nom = st.text_input('Entrer le nom du fichier avnt de télécharger')
             submitted = st.button("Télécharger le fichier excel")
             if submitted:
                 
                 File(Données[0]).file().to_excel(nom+".xlsx")  
                 st.success("Votre fichier à été téléchargé avec succes 😃")
        with col1_21:
            st.write("")
            
        
        
    except:
        st.write("")

with tab4:
    
    try:
        st.title("Temps mobile")
        
        nom_car = st.session_state.temps_jour_mobile
        
        name_car = []
        for i in range(len(nom_car)):
            name_car.append([i,nom_car[i][0]])
        options = st.session_state.nom
        Données = []
        if len(options)==1:
            GraphTime([nom_car[options[0][0]]]).graph()[0]
            Données.append(GraphTime([nom_car[options[0][0]]]).graph()[1]) 
        else:
            
            options_1 = []
            for i in range(len(options)):
                options_1.append(nom_car[options[i][0]])
            GraphTime(options_1).graph()[0]
            Données.append(GraphTime(options_1).graph()[1])
        
        col1_111,col1_122 = st.columns(2)
        with col1_111:
             nom = st.text_input('Entrer le nom du fichier avnt de télécharger'+" ")
             submitted = st.button("Télécharger le fichier excel"+" ")
             if submitted:
                 
                 File(Données[0]).file().to_excel(nom+".xlsx")  
                 st.success("Votre fichier à été téléchargé avec succes 😃")
        with col1_122:
            st.write("")
        
        
        
        st.title("Temps immobile")
        
        nom_cars = st.session_state.temps_jour_immobile
        
        name_cars = []
        for i in range(len(nom_cars)):
            name_cars.append([i,nom_cars[i][0]])
        optionss = st.session_state.nom
        Données = []
        if len(optionss)==1:
            GraphTime([nom_cars[optionss[0][0]]]).graph()[0]
            Données.append(GraphTime([nom_cars[optionss[0][0]]]).graph()[1]) 
        else:
            
            options_1 = []
            for i in range(len(optionss)):
                options_1.append(nom_cars[optionss[i][0]])
            GraphTime(options_1).graph()[0]
            Données.append(GraphTime(options_1).graph()[1])
        
        col1_111,col1_122 = st.columns(2)
        with col1_111:
             nom = st.text_input('Entrer le nom du fichier avnt de télécharger'+"  ")
             submitted = st.button("Télécharger le fichier excel"+"  ")
             if submitted:
                 
                 File(Données[0]).file().to_excel(nom+".xlsx")  
                 st.success("Votre fichier à été téléchargé avec succes 😃")
        with col1_122:
            st.write("")
        
    except:
        pass
