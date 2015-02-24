#-*- coding: utf-8 -*-

from lxml import etree

#def alcoholemia(valor):

#Abrimos los ficheros con los datos

with open("./DATA/controles-alcoholemia.xml", "r")as alcohol:
    alcoholr = etree.parse(alcohol)

