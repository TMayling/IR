# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 19:12:05 2023

@author: User
"""


def construc_dict(data):
    #Création du dictionnaire avec 3 valeurs pour chaque auteur : [nb_neg,sentence,nb_sent]
    distinct_auteurs = data["author"].unique()
    dictionnaire = {}
    for auteur in distinct_auteurs:
        dictionnaire[auteur] = [0,0,0] 
        
    #Alimentation du dictionnaire
    data["nb_neg"] = ""
    data["sentence"] = ""
    data["nb_sent"] = ""
    for raw in data.index:
        n_apostrophe = data["text"][149][6:8] #Création d'une variable qui prend la valeur: "n'"
        data["nb_neg"][raw] = data["text"][raw].lower().count(" ne ") + data["text"][raw].lower().count(n_apostrophe) #Comptage des négations
        data["sentence"][raw] = data["text"][raw].split(".") #Découpage des phrases
        for phrase in data["sentence"][raw]:
            if len(phrase) == 0:
                data["sentence"][raw].remove(phrase) #Suppression des phrases nulles (Le point à la fin du discours ajoutait une phrase '')
        data["nb_sent"][raw] = len(data["sentence"][raw])
        auteur = data["author"][raw]
        dictionnaire[auteur][0] += data["nb_neg"][raw]
        dictionnaire[auteur][1] += data["nb_sent"][raw]
        
    for auteur in dictionnaire.keys():
        dictionnaire[auteur][2] = dictionnaire[auteur][0] / dictionnaire[auteur][1]
        
    #Gestion des totaux
    nb_neg_glob = 0
    nb_sent_glob = 0
    for individu in dictionnaire.keys():
        nb_neg_glob += dictionnaire[individu][0]
        nb_sent_glob += dictionnaire[individu][1]
    dictionnaire["global"] = [nb_neg_glob,nb_sent_glob,nb_neg_glob/nb_sent_glob]
    
    return dictionnaire


        
def taux_negation(individu,dictionnaire):
    neg_per_sent = str(dictionnaire[individu][2])[0:5]
    nb_phrases = dictionnaire[individu][1]
    print("Sachant que les données contiennent "+str(nb_phrases)+" phrases de "+individu+",\n")
    print("Les discours de "+individu+" ont un rapport nombre de négations (\"ne\" ou \"n'\") / nombre de phrase qui vaut "+str(neg_per_sent))
  
def taux_negation_global(dictionnaire):
    neg_per_sent = str(dictionnaire["global"][2])[0:5]
    nb_phrases = dictionnaire["global"][1]
    print("Le document compte "+str(nb_phrases)+" phrases et a un rapport nombre de négations (\"ne\" ou \"n'\") / nombre de phrase qui vaut "+str(neg_per_sent))
    
    
    

    


  
    




