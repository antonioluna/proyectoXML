#-*- coding: utf-8 -*-

from lxml import etree


##########################################################
#                                                        #
#                Creamos las funciones                   #
#                                                        #
##########################################################


#Funcion para los xml con nombres distintos

def distintos(valor):
    diccionario = {}
    for x in valor[0]:
        diccionario[x[0].text] = map(float, x[1][0].text.replace(",0", '')
.split(","))
    return diccionario


#Función para los xml con nombres iguales

def iguales(valor):
    contador = 0
    diccionario = {}
    for x in valor[0]:
        contador = contador + 1
        diccionario[x[0].text + " " + str(contador)] = map(float, x[1][0].text
        .replace(",0", '').split(","))
    return diccionario


#Función que extrae las coordenadas de las poblaciones
def gtroot(ruta, ruta2, ruta3):
    pob = []
    lat = []
    lon = []
    valores = {}
    for x in peninsularoot.findall(ruta):
        pob.append(x.text)
    for y in peninsularoot.findall(ruta2):
        lat.append(y.text)
    for z in peninsularoot.findall(ruta3):
        lon.append(z.text)
    for w in range(len(pob)):
        valores[pob[w]] = [lat[w], lon[w]]
    return valores


#Función que calcula los límites de una provincia
def limites_provincia(nump):
    latp = []
    lonp = []
    for pueb in peninsularoot[nump][0]:
        if pueb.text in pueblos:
            latp.append(pueblos[pueb.text][0])
            lonp.append(pueblos[pueb.text][1])
    limites = [max(latp), min(latp), max(lonp), min(lonp)]
    return limites


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

with open("./DATA/PENINSULA.xml", "r") as peninsula:
    peninsular = etree.parse(peninsula)
    peninsularoot = peninsular.getroot()

##########################################################
#                                                        #
#         Obtención de datos de la península             #
#                                                        #
##########################################################


pueblos = gtroot("CCAA/PROVINCIA/POBLACION", "CCAA/PROVINCIA/POBLACION/LATITUD",
     "CCAA/PROVINCIA/POBLACION/LONGITUD")


##########################################################
#                                                        #
#                Variables de los xml                    #
#                                                        #
##########################################################

dicohol = distintos(alcoholrt)
dicurvas = iguales(curvasroot)
dicnegro = iguales(negrosroot)
dicamu = distintos(camufladosroot)
dicfijo = distintos(fijosroot)
comun = peninsularoot.findall("CCAA")

##########################################################
#                                                        #
#                   Menú principal                       #
#                                                        #
##########################################################


print "Bienvenido a mi proyecto de XML\n"

contador = -1
for com in comun:
    contador = contador + 1
    print str(contador) + " " + com.text

elec = int(raw_input("\nPor favor, elija el número de comunidad Atónoma: "))

contador = -1
for prov in peninsularoot[elec]:
    contador = contador + 1
    print str(contador) + " " + prov.text

elec2 = int(raw_input("\nAhora, seleccione el número de provincia: "))

limit = limites_provincia(elec)

print 'En la provincia de %s hay:\ni Puntos de controles de alcoholemia\ni \
Puntos negros\ni Puntos de radar camuflados\ni Radares fijos\n'\
 % (peninsularoot[elec].text)

contador = -1
for pobl in peninsularoot[elec][elec2]:
    contador = contador + 1
    print str(contador) + " " + pobl.text

#for z in dicohol:
    #print max(dicohol[z])
    #print min(dicohol[z])