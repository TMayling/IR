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
    
    
    
    data = data[data["toptopic"]!="-"] #Suppression des lignes sans toptopic détecté
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
        
    


    distinct_auteurs = data["author"].unique()
    distinct_topics = data["toptopic"].unique()
    
    #Initialisation de nb_topics (dictionnaires imbriqués)
    nb_topics = {}
    for auteur in distinct_auteurs:
        nb_topics[auteur]={}
        for topic in distinct_topics:
            nb_topics[auteur][topic] = 0
            
    #Initialisation de nb_topics_global
    nb_topics_global = {}
    for topic in distinct_topics:
        nb_topics_global[topic] = 0
        
            
    #Remplissage des dictionnaires
    for i in dictionnaire.keys():
        #Alimentation du dictionnaires nb_topics
        while len(dictionnaire[i])>0:
            top_topic = dictionnaire[i][0]
            nb = dictionnaire[i].count(dictionnaire[i][0])
            nb_topics[i][top_topic] = nb #remplissage de nb_topics
            nb_topics_global[top_topic] += nb #remplissage de nb_topics_global
            while top_topic in dictionnaire[i]:
                dictionnaire[i].remove(top_topic)
    
            
    return nb_topics, nb_topics_global

    
    
def n_major_topics(individu,n,topics_words,nb_topics_par_individu):
    topic_recur = sorted(nb_topics_par_individu[individu], key=nb_topics_par_individu[individu].get) #Classement de récurrence des topics croissant (topics)
    nb_recur = sorted(list(nb_topics_par_individu[individu].values())) #Classement de récurrence des topics croissant (nb_occurences)
    
    nb_topics_detectes = sum(nb_topics_par_individu[individu].values())
    print(str(nb_topics_detectes)+" topics ont été détectés dans les discours de "+individu+"\n")
    for i in range(1,n+1):
        lib_topic = topic_recur[-i]
        nb_recur_topic = nb_recur[-i]
        pct_recur_topic = nb_recur_topic/nb_topics_detectes*100
        pct_to_print = str(pct_recur_topic)[0:5]
        words_topic = list(topics_words[topics_words["topic"]==lib_topic]['word'])
        print("Topic n°"+str(i)+": "+lib_topic+", "+str(nb_recur_topic)+" fois reconnu (équivaut à "+str(pct_to_print)+"% des topics détectés). \n Champ lexical: "+str(words_topic)+"\n")
    
        
def n_major_topics_global(topics_words,nb_topics_global):
    topic_recur = sorted(nb_topics_global, key=nb_topics_global.get) #Classement de récurrence des topics croissant (topics)
    nb_recur = sorted(list(nb_topics_global.values())) #Classement de récurrence des topics croissant (nb_occurences)
    
    nb_topics_detectes = sum(nb_topics_global.values())
    print(str(nb_topics_detectes)+" topics ont été détectés\n")
    """
    for i in range(1,n+1):
        lib_topic = topic_recur[-i]
        nb_recur_topic = nb_recur[-i]
        pct_recur_topic = nb_recur_topic/nb_topics_detectes*100
        pct_to_print = str(pct_recur_topic)[0:5]
        words_topic = list(topics_words[topics_words["topic"]==lib_topic]['word'])
        print("Topic "+str(i)+": "+lib_topic+", "+str(nb_recur_topic)[0:1]+" fois reconnu (équivaut à "+str(pct_to_print)+"% des topics détectés). \n Champ lexical: "+str(words_topic)+"\n")
    """
    
def compare(individu,n,topics_words,nb_topics_par_individu,nb_topics_global):
    #Différence entre le pct de réccurence du topic par l'individu et au global
    pct_indiv_moins_pct_global = nb_topics_global.copy()
    for topic in nb_topics_global.keys():
        pct_indiv_moins_pct_global[topic] = (nb_topics_par_individu[individu][topic]/sum(nb_topics_par_individu[individu].values()) - nb_topics_global[topic]/sum(nb_topics_global.values()))*100
        
        
    topic_recur = sorted(pct_indiv_moins_pct_global, key=pct_indiv_moins_pct_global.get) #Classement de récurrence des topics croissant (topics)
    diff_recur = sorted(list(pct_indiv_moins_pct_global.values())) #Classement de récurrence des topics croissant (nb_occurences)
    
    for i in range(1,n+1):
        lib_topic = topic_recur[-i]
        diff_topic = diff_recur[-i]
        diff_to_print = str(diff_topic)[0:5]
        #pct_to_print = str(pct_recur_topic)[0:5]
        words_topic = list(topics_words[topics_words["topic"]==lib_topic]['word'])
        print("Topic privilégié n°"+str(i)+": "+lib_topic+".\n "+individu+" évoque plus ce thème que la moyenne, la différence en points de pourcentage est de "+str(diff_to_print)+ ".\n Champ lexical: "+str(words_topic)+"\n")
    