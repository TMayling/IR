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
    
#Lancement des fonctions de la partie : 1.Topics_Signature
def signature_topic(individu):
    topics_words = topic.load_topics('topic_legit.xls')
    print("-----------Signature de topic \n")
    nb_topics_par_individu, nb_topics_global = topic.topic_signature(data, topics_words)
    topic.n_major_topics(individu, 2, topics_words, nb_topics_par_individu)
    topic.n_major_topics_global(topics_words, nb_topics_global)
    topic.compare(individu, 2, topics_words, nb_topics_par_individu,nb_topics_global)
    
#Chargement des données communes à toutes les analyses
preprocessing('docs_legit_5k.xls', 'speechs.csv')
data = load_speechs('speechs.csv')
individu = 'M. Éric Ciotti' #'M. Éric Ciotti''M. le président'

#1.Topics_Signature
signature_topic(individu)
#2.



     

