# -*- coding: utf-8 -*-

import os

list_class = []
dict_composant = {}
dict_class = {}

with open('./sources/Resultats_protocole_3.csv') as lines:
    for line in lines:
        tab_line = line.split(";")
        tab = tab_line[2]
        files = tab.split(',')
        for i in range(len(files)):
            print(files[i])
            classe =files[i].split("/")
            nom_classe = classe[len(classe) - 1]
            tab_classe = nom_classe.split(".")
            if len(tab_classe) > 1:
                if "java" in tab_classe[1]:

                    if (tab_classe[0] not in list_class):
                        list_class.append(tab_classe[0])
                        dict_class[tab_classe[0]] = 0
                        i = len(classe) - 2
                        check = False
                        composant = ""
                        while (not check and i >=0):
                            if "xwiki-platform" in classe[i]:
                                composant = classe[i][15:]
                                check = True
                            i = i - 1
                        dict_composant[tab_classe[0]] = composant

                    dict_class[tab_classe[0]] = dict_class[tab_classe[0]] + 1
    for i in range(len(list_class)):
        print(list_class[i] + " : " + str(dict_class[list_class[i]]) + " | In component : " + dict_composant[list_class[i]])

list_classe = []
list_couverture = []
list_complexite = []

with open('./sources/Resultats_protocole_4.csv') as lines:
    for line in lines:
        tab_line = line.split(";")
        list_classe.append(tab_line[0])
        list_couverture.append(tab_line[1])
        list_complexite.append(tab_line[2].rstrip("\n\r"))

try:
    os.remove("./Resultats_protocole_5.csv")
except OSError as e:
    print(e.errno)

res = open("./Resultats_protocole_5.csv","a")
res.write("Class;Component;Coverage;Estimate Complexity;Bugs Number\n")
for i in range (0, len(list_classe)):
    if i != 0:
        nombre = 0
        composant = ""
        if list_classe[i] in list_class:
            classe = list_classe[i]
            nombre = dict_class[classe]
            composant = dict_composant[classe]
        if nombre != 0:
            res.write(list_classe[i] + ";" + composant + ";" + list_couverture[i] + ";" +str(list_complexite[i]) + ";" + str(nombre) + "\n")