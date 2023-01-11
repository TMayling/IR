# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 11:37:11 2023

@author: User
"""
import pandas as pd
from textblob import Blobber #pip install textblob
from textblob_fr import PatternTagger, PatternAnalyzer #pip install textblob-fr
tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())



def note(nb):
    if nb > 0 : 
        return "Positif"
    elif nb < 0 : 
        return "Négatif"
    else:
        return "Neutre"



def analyse_sentiment(data):
    dictionnaire = {}
    for auteur in data["author"].unique():
        dictionnaire[auteur] = []
        
    data.loc[max(data.index)+1] = [0,0,"",0,0,"","",""]
    parole = data["author"][0]
    text = ""
    for i in data.index:
        if parole == data["author"][i]:
            text += " "+data["text"][i]
        else: 
            analysis = note(tb(text).sentiment[0])
            dictionnaire[data["author"][i-1]].append(analysis)
            parole = data["author"][i]
            text = data["text"][i]
      
        
    
    sentiment = {}
    sentiment["global"] = [0,0,0]
    for auteur in dictionnaire.keys():
        sentiment[auteur] = [dictionnaire[auteur].count('Positif'),dictionnaire[auteur].count('Neutre'),dictionnaire[auteur].count('Négatif')]
    
        sentiment["global"][0] += dictionnaire[auteur].count('Positif')
        sentiment["global"][1] += dictionnaire[auteur].count('Neutre')
        sentiment["global"][2] += dictionnaire[auteur].count('Négatif')
        
    return sentiment


        

