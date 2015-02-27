#-*- coding: utf-8 -*-

from lxml import etree
import webbrowser
import os
from commands import getoutput


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
        lat.append(float(y.text.replace(",", ".")))
    for z in peninsularoot.findall(ruta3):
        lon.append(float(z.text.replace(",", ".")))
    for w in range(len(pob)):
        valores[pob[w]] = [lat[w], lon[w]]
    return valores


#Función que calcula los límites de una provincia

def limites_provincia(nump, nump2):
    latp = []
    lonp = []
    for pueb in peninsularoot[nump][nump2]:
        if pueb.text in pueblos:
            latp.append(pueblos[pueb.text][0])
            lonp.append(pueblos[pueb.text][1])
    limites = [max(latp), min(latp), max(lonp), min(lonp)]
    return limites


#Esta función devuelve la cantidad de puntos en una provincia

def cantidad_pois(xml):
    pois = {}
    for poi in xml:
        if xml[poi][1] <= limit[0] and xml[poi][1] >= limit[1]\
         and xml[poi][0] <= limit[2] and xml[poi][0] >= limit[3]:
            pois[poi] = [xml[poi][1], xml[poi][0]]
    return pois


#Esta función añade al archivo de configuración de openlayers los pois

def openconf(dicpois, titulo, icono):
    anadir = ""
    #lt.ltltltl\tl.olololo\ttitle\tdescription\tname.png\t24,24\t0,0
    for pu in dicpois:
        anadir = anadir + str(dicpois[pu][0]) + "\t" + str(dicpois[pu][1])\
        + "\t" + titulo + "\t" + pu + "\t" + icono + "\t24,24\t0,0\n"
        anadir.replace(" ", "")
    return anadir


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

limit = limites_provincia(elec, elec2)

cant_control = cantidad_pois(dicohol)
cant_curvas = cantidad_pois(dicurvas)
cant_pnegros = cantidad_pois(dicnegro)
cant_camu = cantidad_pois(dicamu)
cant_rfijos = cantidad_pois(dicfijo)

##########################################################
#                                                        #
#                Concretar población                     #
#                                                        #
##########################################################


contador = -1
for pobl in peninsularoot[elec][elec2]:
    contador = contador + 1
    print str(contador) + " " + pobl.text

concretar = int(raw_input("\n¿Selecione una población: "))

##########################################################
#                                                        #
#          Impresion en pantalla de cantidades           #
#                                                        #
##########################################################

print 'En la provincia de %s hay:\n%i Puntos de controles de alcoholemia\n%i \
Curvas peligrosas\n%i Puntos negros\n%i Puntos de radar camuflados\n\
%i Radares fijos\n' % (peninsularoot[elec][elec2].text, len(cant_control),
    len(cant_curvas), len(cant_pnegros), len(cant_camu), len(cant_rfijos))


##########################################################
#                                                        #
#                Configuración Openlayers                #
#                                                        #
##########################################################


with open("./OPENLAYERS/sources/source", "r") as openbody:
    openbodyr = openbody.read().replace("l.olol", str(pueblos
    [peninsularoot[elec][elec2][concretar].text][1])).replace("lt.ltlt",
    str(pueblos[peninsularoot[elec][elec2][concretar].text][0]))
with open("./OPENLAYERS/sources/config", "r") as openconfig:
    openconfigr = openconfig.read()

open_ctrl = ["alco.png", "CONTROL DE ALCOHOLEMIA"]
open_negro = ["blkpnt.png", "PUNTO NEGRO"]
open_camu = ["camu.png", "RADAR CAMUFLADO"]
open_curvas = ["curv.png", "CURVA PELIGROSA"]
open_fijo = ["fijo.png", "RADAR FIJO"]

ct = openconf(cant_control, open_ctrl[1], open_ctrl[0])
cv = openconf(cant_curvas, open_curvas[1], open_curvas[0])
ne = openconf(cant_pnegros, open_negro[1], open_negro[0])
camu = openconf(cant_camu, open_camu[1], open_camu[0])
fijo = openconf(cant_rfijos, open_fijo[1], open_fijo[0])


##########################################################
#                                                        #
#                Exportación al navegador                #
#                                                        #
##########################################################

with open("./OPENLAYERS/ficheros/index.html", "w") as index:
    index.writelines(openbodyr)

with open("./OPENLAYERS/ficheros/textfile.txt", "w") as textfile:
    textfile.write((openconfigr + ct + cv + ne + camu + fijo).encode("utf-8"))

navegador = raw_input('\nPulse "n" para abrir los POIs en el navegador.Esta\
función sólo es compatible con navegadores Mozilla: ')

if navegador == "n" or navegador == "N":
    webbrowser.open(getoutput("pwd") +
    "/OPENLAYERS/ficheros/index.html")
else:
    print "\n\nAdios\n\n"