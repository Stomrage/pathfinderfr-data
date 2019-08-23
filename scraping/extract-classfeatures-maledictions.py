#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

from main.libhtml import html2text, cleanSectionName, mergeYAML

## Configurations pour le lancement
MOCK_MALEDICTION = None
#MOCK_MALEDICTION = "mocks/maledictions.html"       # décommenter pour tester avec les maledictions pré-téléchargées

URL = "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.mal%c3%a9dictions%20doracle.ashx"
FIELDS = ['Nom', 'Classe', 'Archétype', 'Prérequis', 'Source', 'Niveau', 'Auto', 'Description', 'Référence' ]
MATCH = ['Nom', 'Classe', 'Archétype']

liste = []

print("Extraction des aptitude (malédictions)...")

if MOCK_MALEDICTION:
    content = BeautifulSoup(open(MOCK_MALEDICTION),features="lxml").body
else:
    content = BeautifulSoup(urllib.request.urlopen(URL).read(),features="lxml").body

section = content.find_all("div",{'class':['article_2col']})

malediction = {'Niveau':1}
newObj = False
descr = ""
source = 'MJRA'
for s in section:
    for el in s.children:
        if el.name == "h3":
            nom = cleanSectionName(el.text)
            reference = URL + el.find_next("a")['href']

            if newObj:
                malediction['Classe'] = 'Oracle'
                malediction['Description'] = descr.strip()
                liste.append(malediction)
                malediction = {'Niveau':1}
                descr = ""

            malediction['Nom'] = "Malédiction: " + nom
            malediction['Source'] = source
            malediction['Référence'] = reference
            newObj = True
        
        else:
            descr += html2text(el)
    
        
# last element        
malediction['Classe'] = 'Oracle'
malediction['Description'] = descr.strip()
liste.append(malediction)


print("Fusion avec fichier YAML existant...")

HEADER = ""

mergeYAML("../data/classfeatures.yml", MATCH, FIELDS, HEADER, liste)
