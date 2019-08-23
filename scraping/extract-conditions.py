#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

from main.libhtml import jumpTo, html2text, mergeYAML


## Configurations pour le lancement
URL = "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.%c3%89tats%20pr%c3%a9judiciables.ashx"
MOCK_CF = None
#MOCK_CF = "mocks/conditions.html"       # décommenter pour tester avec les conditions pré-téléchargées

FIELDS = ['Nom', 'Source', 'Description', 'Référence' ]
MATCH = ['Nom']

liste = []

if MOCK_CF:
    content = BeautifulSoup(open(MOCK_CF),features="lxml").body
else:
    content = BeautifulSoup(urllib.request.urlopen(URL).read(),features="lxml").body

section = jumpTo(content, 'h2',{'class':'separator'}, "Liste des états préjudiciables")

SOURCE = "MJ"

condition = {'Source':SOURCE}
newObj = False
advantage = False
descr = ""

for s in section:
    if s.name == 'h2':
        condition['Description'] = descr.replace('\n','').strip()
        liste.append(condition)
        
        # avantages
        SOURCE = "AM"
        condition = {'Source':SOURCE}
        newObj = False
        advantage = True
        descr = ""
        
    elif s.name == 'h3':
        if newObj:
            condition['Description'] = descr.strip()
            liste.append(condition)
            condition = {'Source':SOURCE}
        descr = ""
        condition['Nom'] = s.text.replace('¶','').strip()
        if advantage:
            condition['Nom'] += " (avantage)"
        newObj = True
        
        condition['Référence']= URL + s.find('a')['href']
                
    else:
        descr += html2text(s)

## last element
condition['Description'] = descr.replace('\n','').strip()
liste.append(condition)
            
print("Fusion avec fichier YAML existant...")

HEADER = ""

mergeYAML("../data/conditions.yml", MATCH, FIELDS, HEADER, liste)
