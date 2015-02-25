#-*- coding: utf-8 -*-

from lxml import etree


##########################################################
#                                                        #
#                Creamos las funciones                   #
#                                                        #
##########################################################


def iguales(valor):
    diccionario = {}
    for x in valor[0]:
        diccionario[x[0].text] = map(float, x[1][0].text.replace(",0", '')\
        .split(","))
        return diccionario


#def distintos(valor):
    #diccionario2 = {}
    #for x in valor[0]:
        #diccionario2[x[0].text] = map(float, x[1][0].text.replace(",0", '')\
        #.split(","))
        #print diccionario2

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
    curvasroot = curvasr.getroot()

with open("./DATA/puntos-negros.xml", "r")as negros:
    negrosr = etree.parse(negros)
    negrosroot = negrosr.getroot()

with open("./DATA/radares-camuflados.xml", "r")as camuflados:
    camufladosr = etree.parse(camuflados)
    camufladosroot = camufladosr.getroot()

with open("./DATA/radares-fijos.xml", "r")as fijos:
    fijosr = etree.parse(fijos)
    fijosroot = fijosr.getroot()

##########################################################
#                                                        #
#         Coordenadas Peninsula Ibérica                  #
#                                                        #
##########################################################

with open("./DATA/PENINSULA.xml", "r")as peninsula:
    peninsular = etree.parse(peninsula)
    peninsularoot = peninsular.getroot()

#prueba diccionario del xml "alcohol"

dicohol = {}
dicurvas = iguales(alcoholrt)
dicnegro = {}
dicamu = {}
dicfijo = {}

#for x in alcoholrt[0]:
    #dicohol[x[0].text] = map(float, x[1][0].text.replace(",0", '').split(","))

#for x in curvasroot[0]:
    #dicurvas[x[0].text] = map(float, x[1][0].text.replace(",0", '').split(","))


print dicurvas

#for z in dicohol:
    #print max(dicohol[z])
    #print min(dicohol[z])