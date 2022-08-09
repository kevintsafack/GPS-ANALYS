import pandas as pd
import altair as alt
import streamlit as st
class Graph :
    def __init__(self, data):
        self.data = data
    def graph(self):
        Distance = self.data
        Dist = Distance[0][1]
        name = []
        Jrs =  Distance[0][-1]
        for i in range(len(Distance)):
            
            for j in range(len(Distance[i][1])) :
                name.append(Distance[i][0])
            try : 
                Dist = Dist+ Distance[i+1][1]
                Jrs = Jrs +  Distance[i+1][-1]
            except :
                continue

        d_text = []
        for i in range(len(Dist)):
            d_text.append(str(Dist[i])+" Km")
        d_text
        source_1 =  pd.DataFrame({ 'Valeurs': Dist ,
                                    'Voitures' :name ,
                                       'Dates': Jrs,
                                  'Text' : d_text
                                      })
        bars = alt.Chart().mark_bar().encode(
            x='Voitures:O',
            y=alt.Y('Valeurs:Q', title='Distance'),
            color='Voitures:N',
        )
        text = bars.mark_text(
                    align='center',
                    baseline='middle', dy=-10, color='#38761d',
                    dx=0).encode(text='Text')
        Graph = alt.layer(bars,text, data=source_1,width=250,height=300).facet(
            column='Dates:N'
        )
        return Graph , source_1

class GraphTime :
    def __init__(self, data):
        self.data = data
    def graph(self):
        Distance = self.data
        Dist = Distance[0][1]
        name = []
        Jrs =  Distance[0][-2]
        d_text = Distance[0][-1]
        for i in range(len(Distance)):
            for j in range(len(Distance[i][1])) :
                name.append(Distance[i][0])
            try : 
                Dist = Dist+ Distance[i+1][1]
                Jrs = Jrs +  Distance[i+1][-2]
                d_text = d_text + Distance[i+1][-1]
            except :
                continue

        
        print(d_text)
        source_1 =  pd.DataFrame({ 'Valeurs': Dist ,
                                    'Voitures' :name ,
                                       'Dates': Jrs,
                                  'Text' : d_text
                                      })
        bars = alt.Chart().mark_bar().encode(
            x='Voitures:O',
            y=alt.Y('Valeurs:Q', title='Time'),
            color='Voitures:N',
        )
        text = bars.mark_text(
                    align='center',
                    baseline='middle', dy=-10, color='#38761d',
                    dx=0).encode(text='Text')
        Graph = alt.layer(bars,text, data=source_1,width=250,height=300).facet(
            column='Dates:N'
        )
        return Graph , source_1
    

class File :
    def __init__(self, dataframe):
        self.dataframe = dataframe
    def file(self):
        S = self.dataframe
        AQ = []
        for i in  range(len(S.Dates)) :
            AQ.append(S.Dates[i])
        A_1 = [[AQ[0],AQ.count(AQ[0])]]
        for i in range(len(AQ)) :
            if A_1.count([AQ[i],AQ.count(AQ[i])]) == 0 :
                A_1.append([AQ[i],AQ.count(AQ[i])])
        S = S.set_index('Dates')
        DF = []
        for i in range(len(A_1)):
            if A_1[i][1] == 1:
                S_33 =S.loc[A_1[i][0]]
                S_3 = pd.DataFrame({ 'Valeurs': [S_33[0]] ,
                                                    'Voitures' :[S_33[1]] ,
                                                       'Dates':A_1[i][0] ,
                                                  'Text' : [S_33[2]]
                                                      })
                S_3 = S_3.set_index('Dates')
                DF.append(S_3)
            else:
                DF.append(S.loc[A_1[i][0]])

        space = pd.DataFrame({ 'Valeurs': [' '] ,
                               'Voitures' :[' '] ,
                              'Dates':[ ' '],
                               'Text' :[' ']
                                              })
        space = space.set_index('Dates')
        
        DF_1 = DF[0]
        for i in range(len(DF)-1):
            DF_1 = pd.concat([DF_1,space,space,DF[i+1]])
        DF_1
        return DF_1
    
