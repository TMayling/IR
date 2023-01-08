# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:14:20 2022

@author: User
"""

import pandas as pd



def load_topics(topics_file):
    topics_words = pd.read_excel(topics_file)
    return topics_words





def topic_signature(data,topics_words):
    #Création de dictionnaires imbriqués
    nb_topics = {}
    distinct_auteurs = data["author"].unique()
    distinct_topics = data["toptopic"].unique()
    for auteur in distinct_auteurs:
        nb_topics[auteur]={}
        for topic in distinct_topics:
            nb_topics[auteur][topic] = 0
            
            
    dictionnaire={}
    
    #Récupération des toptopics par auteur
    for i in data.index:
        if data["author"][i] in dictionnaire:
            dictionnaire[data["author"][i]].append(data["toptopic"][i])
        else:
            dictionnaire[data["author"][i]] = []
            dictionnaire[data["author"][i]].append(data["toptopic"][i])
      
    
    for i in dictionnaire.keys():
        #Supression des valeurs nulles de la liste
        while '-' in dictionnaire[i]:
            dictionnaire[i].remove('-')
        while len(dictionnaire[i])>0:
            top_topic = dictionnaire[i][0]
            nb = dictionnaire[i].count(dictionnaire[i][0])
            nb_topics[i][top_topic] = nb
            while top_topic in dictionnaire[i]:
                dictionnaire[i].remove(top_topic)
            
    
    individu = "M. le président"
    #individu = "M. Éric Ciotti"
    print(nb_topics[individu])
    #Classement des récurrences des topics croissant et nb d'occurences associés
    topic_recur = sorted(nb_topics[individu], key=nb_topics[individu].get)
    nb_recur = sorted(list(nb_topics[individu].values()))
    
    #Topic le plus réccurent et nb d'occurences associés
    topic_max_individu = topic_recur[-1]
    print(topic_recur[-1])
    print(nb_recur[-1])
    #Mots correspondant au topic
    print(list(topics_words[topics_words["topic"]==topic_max_individu]['word']))
    
    #2ème topic le plus représenté
    topic_max_individu = topic_recur[-2]
    print(topic_recur[-2])
    print(nb_recur[-2])
    #Mots correspondant au topic
    print(list(topics_words[topics_words["topic"]==topic_max_individu]['word']))
    
    
    
    print(max(nb_topics[individu], key=nb_topics[individu].get))
    
