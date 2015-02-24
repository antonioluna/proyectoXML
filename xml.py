#-*- coding: utf-8 -*-

from lxml import etree

#def alcoholemia(valor):

#Abrimos los ficheros con los datos

with open("./DATA/controles-alcoholemia.xml", "r")as alcohol:
    alcoholr = etree.parse(alcohol)

with open("./DATA/curvas-peligrosas.xml", "r")as curvas:
    curvasr = etree.parse(curvas)

with open("./DATA/puntos-negros.xml", "r")as negros:
    negrosr = etree.parse(negros)

with open("./DATA/radares-camuflados.xml", "r")as camuflados:
    camufladosr = etree.parse(camuflados)

with open("./DATA/radares-fijos.xml", "r")as fijos:
    fijosr = etree.parse(fijos)





