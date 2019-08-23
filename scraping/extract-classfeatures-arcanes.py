#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

from main.libhtml import html2text, cleanSectionName, cleanInlineDescription, mergeYAML

## Configurations pour le lancement
MOCK_ARCANE = None
#MOCK_ARCANE = "mocks/arcanes.html"       # décommenter pour tester avec les arcanes pré-téléchargées

URL = "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.arcanes.ashx"
FIELDS = ['Nom', 'Classe', 'Archétype', 'Prérequis', 'Source', 'Niveau', 'Auto', 'Description', 'Référence' ]
MATCH = ['Nom', 'Classe', 'Archétype']

liste = []

print("Extraction des aptitude (arcanes)...")

if MOCK_ARCANE:
    content = BeautifulSoup(open(MOCK_ARCANE),features="lxml").body
else:
    content = BeautifulSoup(urllib.request.urlopen(URL).read(),features="lxml").body

section = content.find_all("div",{'class':['article_2col']})

LVL = 3
arcane = {'Niveau':LVL}
newObj = False
descr = ""
source = 'AM'

for s in section:
    for el in s.children:
        if el.name == "h3":
            nom = cleanSectionName(el.text)
            reference = URL + el.find_next("a")['href']

            if newObj:
                arcane['Classe'] = 'Magus'
                arcane['Description'] = cleanInlineDescription(descr)
                liste.append(arcane)
                arcane = {'Niveau':LVL}
                
            descr = ""
            arcane['Nom'] = "Arcane: " + nom
            arcane['Source'] = source
            arcane['Référence'] = reference
            source = "AM"
            newObj = True
        
        else:
            descr += html2text(el)
    

# last element        
arcane['Classe'] = 'Magus'
arcane['Description'] = cleanInlineDescription(descr)
liste.append(arcane)


print("Fusion avec fichier YAML existant...")

HEADER = ""

mergeYAML("../data/classfeatures.yml", MATCH, FIELDS, HEADER, liste)
