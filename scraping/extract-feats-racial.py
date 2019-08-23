#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

from main.libhtml import mergeYAML

## Configurations pour le lancement
MOCK_LIST = None
MOCK_DON = None
#MOCK_LIST = "mocks/don-aasimar.html" # décommenter pour tester avec une liste pré-téléchargée
#MOCK_DON  = "mocks/don3.html"        # décommenter pour tester avec un sort pré-téléchargé

URLs = ["http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.aasimar%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.dhampir%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.drow%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.fetchelin%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Gobelin%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.hobgobelin%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.homme-f%c3%a9lin%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.homme-rat%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.ifrit%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.kobold%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.ondin%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.orque%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.or%c3%a9ade%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.sylphe%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.tengu%20(race).ashx",
        "http://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.tieffelin%20(race).ashx"
        ]

PROPERTIES = [  "Catégorie", "Catégories", "Conditions", "Condition", "Conditions requises", "Normal", "Avantage", "Avantages", "Spécial", "À noter"]

FIELDS = ['Nom', 'Résumé', 'Catégorie', 'Conditions', 'Avantage', 'Normal', 'Spécial', 'Source', 'Référence' ]
MATCH = ['Nom']

liste = []


for u in URLs:

    if MOCK_LIST:
        html = BeautifulSoup(open(MOCK_LIST),features="lxml")
    else:
        html = BeautifulSoup(urllib.request.urlopen(u).read(),features="lxml")

    feats = html.find('table',{'class':'tablo autoalt toutgauche'})
    if not feats:
        print("No section feats found for %s" % u)

    # itération sur chaque page
    for r in feats.find_all('tr'):
        # ignore some rows
        if 'class' in r.attrs and 'titre' in r.attrs['class']:
            continue

        don = {}

        element = r.find_next('a')
        title = element.text
        link  = element.get('href')
        source  = r.find_next('sup').text
        if source == "MJ-UC":
            source = "MJ"
        elif source == "MA": # doit être une erreur
            source = "AO"

        print("Processing %s" % title)
        pageURL = "http://www.pathfinder-fr.org/Wiki/" + link

        don[u'Nom']=title
        don[u'Référence']=pageURL
        don[u'Source']=source

        if MOCK_DON:
            content = BeautifulSoup(open(MOCK_DON),features="lxml").body.find(id='PageContentDiv')
        else:
            content = BeautifulSoup(urllib.request.urlopen(pageURL).read(),features="lxml").body.find(id='PageContentDiv')

        if(content == None):
            print("Page %s n'a pas pu être récupérée!" % pageURL)
            continue

        # lire les attributs
        text = ""
        for attr in content.find_all('b'):
            key = attr.text.strip()
            if key[-1]=='.':
                key = key[:-1]
            if key.endswith(' :'):
                key = key[:-2]

            for s in attr.next_siblings:
                #print "%s %s" % (key,s.name)
                if s.name == 'b':
                    break
                elif s.string:
                    text += s.string
                elif s.name == 'ul':
                    text += "\n"
                    for li in s.find_all('li'):
                        text +=  li.text + "\n"
                    text += "\n"

            value = text.strip()
            if value.startswith(":"):
                value = value[1:]

            if key in PROPERTIES:
                if key == "Condition" or key == "Conditions requises":
                    key = "Conditions"
                elif key == "Avantages":
                    key = "Avantage"
                elif key == "Catégories":
                    key = "Catégorie"
                elif key == "À noter":
                    key = "Spécial"

                don[key]=value.strip()
                text = ""
            elif "Avantage" in don and len(key) < 15:
                don["Avantage"] += "\n" + key.upper() + " " + value.strip()
                text = ""
            else:
                print("- Skipping unknown property %s" % key)

        # ajouter don
        liste.append(don)

print("Fusion avec fichier YAML existant...")

HEADER = ""

mergeYAML("../data/dons.yml", MATCH, FIELDS, HEADER, liste)
