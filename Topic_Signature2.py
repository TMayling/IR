# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:39:03 2022

@author: User
"""
import pandas as pd
from os import path
import Topic_Signature as topic

def preprocessing(data_init,data_fin):
    if not path.exists(data_fin):
        #Chargement des données
        data = pd.read_excel(data_init)
        #Suppression des lignes qui sont des descriptions (ex: Applaudissements sur les bancs du groupe A)
        for phrase in range(len(data)):
            if data["text"][phrase][0] == "(" or data["text"][phrase][-1] == ")":
                data = data.drop(phrase)
        #Suppression des lignes avec auteur inconnu       
        data = data[data["author"]!="unk"]   
        
        data.to_csv(data_fin,index=False,sep=';', encoding="utf-8-sig")

        
def load_speechs(data_fin):
    data = pd.read_csv(data_fin, sep=";")
    return data
    



preprocessing('docs_legit_5k.xls', 'speechs.csv')
data = load_speechs('speechs.csv')
topics_words = topic.load_topics('topic_legit.xls')
topic.topic_signature(data, topics_words)

     

