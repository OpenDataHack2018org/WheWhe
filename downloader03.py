 #!/usr/bin/env python
# -*- coding: utf-8 -*-


############BLOQUE 1: configurar el entorno

# empezar el tutorial en https://software.ecmwf.int/wiki/display/WEBAPI/Access+ECMWF+Public+Datasets

###PASO 1
# el primer paso d pasos de este tutorial es intalar la libreria ecmwfapi. En Ubuntu se hace asi: 
# installar pip : sudo apt-get update && sudo apt-get -y upgrade
# actualizarlo : sudo apt-get install python-pip
# instalar la librería añadiendo  un flog "-H" a lo que indcia la web: sudo pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz
# así a mí no me funciona no funciona
# pip search ecmwf te da los nombres del as librerías que llevan "ecmwf". veo que hay una que se llama ecmwf-api-client 
# la instalo con pip install ecmwf-api-client  y  parece que al fin funciona

###PASO2
# luego hay que crear un archivo con el nombre ".ecmwfapirc" en $Home
# para ver estos arcihvos en el explorador de archivos hay que pulsar Ctrl+h
# este es el contenido del archivo (sin las #)
#{
#    "url"   : "https://api.ecmwf.int/v1",
#    "key"   : "XXXXX",
#    "email" : "YYYY"
#}

###PASO 3
# hay que logarse en la web de ECMWF y aceptar los terminos de uso de C3S
# http://apps.ecmwf.int/datasets/licences/copernicus/

#########BLOQUE 2 descargar datos de 

###PASO1
# descripción de los seasonal forecast de c3s: https://climate.copernicus.eu/seasonal-forecasts
# catalogo de datos http://apps.ecmwf.int/data-catalogues/c3s-seasonal/?class=c3
# known issues of the C3S seasonal forecast  https://software.ecmwf.int/wiki/display/CKB/C3S+seasonal+forecasts+known+issues
# ejemplo tomado de
#https://software.ecmwf.int/wiki/display/CKB/How+to+download+the+C3S+Seasonal+forecast+data+via+the+ECMWF+Web+API

from ecmwfapi import ECMWFDataServer
  
server = ECMWFDataServer()          

def download(Origin="ecmf",Parameter="228",Date="2018-05-01",Step="24"):
    server.retrieve({
        "dataset":   "c3s_seasonal",          
        "date":      Date,
        "levtype":   "sfc",
        "number":    "0/to/50",
        "origin":    Origin,
        "param":     Parameter+".128",
        "step":      Step,
        "stream":    "mmsf",
        "time":      "00:00:00",
        "type":      "fc",
        "area":      "90/-180/-90/180",
        "grid":      "0.25/0.25",
        "format":    "netcdf",
        "target":    Origin+Parameter+Date+"step_"+Step+".nc"
     })

print ("///Inicio Bucle Descarga///")
for i in range(215):
    print ("--Descargando Step "+str(i*24+24))
    download(Origin="ecmf",Parameter="228",Date="2018-05-01",Step=str(i*24+24))
    print("--Finalizado. Chequea que transfer Rate sea mayor de cero para saber si ha ido bien")
print ("---Fin Bucle Descarga---")
print ()

print ("///Inicio Bucle Descarga///")
for i in range(215):
    print ("--Descargando Step "+str(i*24+24))
    download(Origin="ecmf",Parameter="51",Date="2018-05-01",Step=str(i*24+24))
    print("--Finalizado. Chequea que transfer Rate sea mayor de cero para saber si ha ido bien")
print ("---Fin Bucle Descarga---")
print ()

print ("///Inicio Bucle Descarga///")
for i in range(215):
    print ("--Descargando Step "+str(i*24+24))
    download(Origin="ecmf",Parameter="52",Date="2018-05-01",Step=str(i*24+24))
    print("--Finalizado. Chequea que transfer Rate sea mayor de cero para saber si ha ido bien")
print ("---Fin Bucle Descarga---")
print ()

print ("///Inicio Bucle Descarga///")
for i in range(215*4):
    print ("--Descargando Step "+str(i*6+6)) #
    download(Origin="ecmf",Parameter="164",Date="2018-05-01",Step=str(i*6+6))
    print("--Finalizado. Chequea que transfer Rate sea mayor de cero para saber si ha ido bien")
    print()
print ("---Fin Bucle Descarga---")
print ()

#stream: 
##mmsa ,     Multi-model seasonal forecast
##mmsf ,     Multi-model seasonal forecast atmospheric monthly means
##msmm ,     Multi-model seasonal forecast monthly anomalies

#param: see http://apps.ecmwf.int/codes/grib/param-db
## Wind speed	ws	m s-1	10       <- no para surface
## Temperature	t	K	130          <- no para surface
## Total precipitation	tp	m	228 
## 2 m temperature: 167.128
## total precipitation 228.128 -> ojo, es acumulativa desde el principio de la proyecccion
## Minimum temperature at 2 metres in the last 24 hours: 52.128
## Maximun temperature at 2 metres in the last 24 hours: 51.128
## Maximun temperature at 2 metres in the last 24 hours: 51.128
## Fraction of cloud cover: 248.128
## Total cloud cover:164.128 
## el ".128 creo que es para indicar la versión de tabla, que se va actualizando.

"""Estas son las unicas variables que dan datos cada 6 horas, el resto cada 24
10 metre U wind component, 
10 metre V wind component, 
2 metre dewpoint temperature, 
2 metre temperature, 
Mean sea level pressure, 
Sea surface temperature, 
Soil temperature level 1, 
Total cloud cover
"""

#origin
## 	ecmf , egrr , lfpw

#levtype
##sfc=surface -> no me va
##pl= pressure level
## con pl es necesario añadir el nivel como levellist
## leer https://www.ecmwf.int/en/forecasts/documentation-and-support/137-model-levels


