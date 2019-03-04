# -*- coding: utf-8 -*-

from lxml import etree
import os

tree = etree.parse("data_format.xml")

# GET LINE TEXT
#for element in tree.xpath("/body/p/r/t"):
#    print(element.text)

# GET LINE COLOR
#for element in tree.xpath("/body/p/r/rPr/color"):
#   print(element.attrib['val'])

# GET LINE SIZE
#for element in tree.xpath("/body/p/r/rPr/sz"):
#   print(element.attrib['val'])

# GET ALL
list_size = []
list_color = []
dict_size = {}
dict_color = {}

dict_coverage = {"89C495": "[90%-100%]",
"E7A19B": "[30%-40%]",
"D04437": "[0%-10%]",
"14892C": "[80%-90%]",
"FAE1A0": "[70%-80%]",
"E28E87": "[50%-60%]",
"F6C342": "[60%-70%]",
"DE7B72": "[40%-50%]",
"D5584C": "[10%-20%]",
"D9695F": "[20%-30%]"}

# multiplicateur complexity
x = 0.275

try:
    os.remove("Resultats_protocole_4.csv")
except OSError as e:
    print(e.errno)

res = open("Resultats_protocole_4.csv","a")
res.write("Class;Coverage;Estimate Complexity\n")

for element in tree.xpath("/body/p/r"):
    name = element.find('t').text
    color = element.find('rPr').find('color').attrib['val']

    if color not in list_color:
        list_color.append(color)
        dict_color[color] = 0
    dict_color[color] = dict_color[color] + 1

    size = 21
    try:
        size = element.find('rPr').find('sz').attrib['val']
    except AttributeError as e:
        continue

    if size not in list_size:
        list_size.append(size)
        dict_size[size] = 0
    dict_size[size] = dict_size[size] + 1
    estimate_complexity = 1
    if size != 21:
        estimate_complexity += (int(size) - 21) * x
    estimate_complexity = round(estimate_complexity, 2)
    #print(name + "," + color + "," + str(estimate_complexity))
    res.write(name + ";" + dict_coverage[color] + ";" + str(estimate_complexity) + "\n")

for color in list_color:
    print("color " + dict_coverage[color] + " : " + str(dict_color[color]))

#for size in list_size:
    #print("size " + size + " : " + str(dict_size[size]))