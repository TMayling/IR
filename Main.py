# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 11:39:03 2022

@author: User
"""
import pandas as pd
from os import path
import Topic_Signature as topic
import Negation_Signature as negation
import Sentiment_Analysis_Signature as sentiment

pd.options.mode.chained_assignment = None  # default='warn' --> Supprime les messages d'avertissements (Negation_Signature)


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
def signature_topic():
    print("---------------------Signature de topic \n")
    topics_words = topic.load_topics('topic_legit.xls')
    nb_topics_par_individu, nb_topics_global = topic.topic_signature(data, topics_words)
    topic.n_major_topics(individu, 2, topics_words, nb_topics_par_individu)
    topic.n_major_topics_global(topics_words, nb_topics_global)
    topic.compare(individu, 2, topics_words, nb_topics_par_individu,nb_topics_global)
    
#Lancement des fonctions de la partie : 2.Negation_Signature
def signature_negation():
    print("---------------------Signature de négation \n")
    dictionnaire_negation = negation.construc_dict(data)
    negation.taux_negation_global(dictionnaire_negation)
    negation.taux_negation(individu, dictionnaire_negation)
    
#Lancement des fonctions de la partie : 3.Sentiment_Analysis_Signature
def analyse_sentiment():
    dictionnaire_sentiment = sentiment.analyse_sentiment(data.iloc[:,:8])
    sentiments_individu = dictionnaire_sentiment[individu]
    sentiments_global = dictionnaire_sentiment["global"]
    

    
#Chargement des données communes à toutes les analyses
preprocessing('docs_legit_5k.xls', 'speechs.csv')
data = load_speechs('speechs.csv')
individu = 'M. Éric Ciotti' #'M. Éric Ciotti''M. le président'

#1.Topics_Signature
signature_topic()
#2.Negation_Signature
signature_negation()
#3.Sentiment_Analysis_Signature
analyse_sentiment()


     

