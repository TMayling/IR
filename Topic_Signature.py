# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:14:20 2022

@author: User
"""

import pandas as pd



def load_topics(topics_file):
    topics_words = pd.read_excel(topics_file)
    return topics_words





def topic_signature(data,topics_words, individu, n):
                   
    dictionnaire={}
    
    #Récupération des toptopics par auteur (1 topic ne peut être compté qu'une fois par prise de parole)
    passage = 0
    for i in data.index:
        auteur = data["author"][i]
        top_topic = data["toptopic"][i]
        
        if auteur not in dictionnaire:
            dictionnaire[auteur] = [] #Création de la clé de l'auteur n'étant pas encore été créée
            
        if passage != data["id_passage"][i]: #Si on change d'orateur
            passage_topics = [top_topic] #La liste des topics est initialisé avec le top_topic actuel 
            passage = data["id_passage"][i] #On actualise le passage
            dictionnaire[auteur].append(top_topic) #Ajout du toptopic dans la liste des topics de l'auteur
        elif top_topic not in passage_topics:
            passage_topics.append(top_topic)
            dictionnaire[auteur].append(top_topic) #Ajout du toptopic dans la liste des topics de l'auteur  
        
    
    #Création de dictionnaires imbriqués
    nb_topics = {}
    distinct_auteurs = data["author"].unique()
    distinct_topics = data["toptopic"].unique()
    for auteur in distinct_auteurs:
        nb_topics[auteur]={}
        for topic in distinct_topics:
            nb_topics[auteur][topic] = 0
            
            
    for i in dictionnaire.keys():
        #Supression des valeurs nulles de la liste
        while '-' in dictionnaire[i]:
            dictionnaire[i].remove('-')
        #Alimentation du dictionnaires nb_topics
        while len(dictionnaire[i])>0:
            top_topic = dictionnaire[i][0]
            nb = dictionnaire[i].count(dictionnaire[i][0])
            nb_topics[i][top_topic] = nb
            while top_topic in dictionnaire[i]:
                dictionnaire[i].remove(top_topic)
            
    

    
    #print(nb_topics[individu]) #Liste des topics de l'individu
    #Classement des récurrences des topics croissant et nb d'occurences associés
    topic_recur = sorted(nb_topics[individu], key=nb_topics[individu].get)
    nb_recur = sorted(list(nb_topics[individu].values()))
    
    nb_topics_detectes = sum(nb_topics[individu].values())
    print(str(nb_topics_detectes)+" topics ont été détectés dans les discours de "+individu+"\n")
    for i in range(1,n+1):
        lib_topic = topic_recur[-i]
        nb_recur_topic = nb_recur[-i]
        words_topic = list(topics_words[topics_words["topic"]==lib_topic]['word'])
        print("Topic "+str(i)+": "+lib_topic+", "+str(nb_recur_topic)+" fois reconnu. \n Champx lexical: "+str(words_topic)+"\n")