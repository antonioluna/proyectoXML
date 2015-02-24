#-*- coding: utf-8 -*-

from lxml import etree

#def alcoholemia(valor):

##########################################################
#                                                        #
#         Abrimos los ficheros con los datos             #
#                                                        #
##########################################################

with open("./DATA/controles-alcoholemia.xml", "r")as alcohol:
    alcoholr = etree.parse(alcohol)
    alcoholrt = alcoholr.getroot()

with open("./DATA/curvas-peligrosas.xml", "r")as curvas:
    curvasr = etree.parse(curvas)

with open("./DATA/puntos-negros.xml", "r")as negros:
    negrosr = etree.parse(negros)

with open("./DATA/radares-camuflados.xml", "r")as camuflados:
    camufladosr = etree.parse(camuflados)

with open("./DATA/radares-fijos.xml", "r")as fijos:
    fijosr = etree.parse(fijos)


#prueba diccionario del xml "alcohol"

dicohol = {}

for x in alcoholrt[0]:
    dicohol[x[0].text] = x[1][0].text.split(",")

print dicohol