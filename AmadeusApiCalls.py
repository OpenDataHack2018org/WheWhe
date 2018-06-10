
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:15:21 2018
@author: 108700
Prueba de la libreria Amadeus

## configurar el entorno #############################################

Todo instalado en envjorgePaz01 (Anaconda python 3 en Windows10)
activate envjorgepaz01
pip install amadeus
pip install datapackage 

##  documentacion de amadeus #######################################################

https://amadeus.readthedocs.io/en/latest/readme.html
Before anything else,  create an account and get your API key from Amadeus: https://sandbox.amadeus.com/


## leer los datos de aeropuertos con datapackage ##############################################################

Al final no hacemos uso de datapackage para recuperar el listado de aeropuertos.
Nos vamos a la fuente original y descargamos los csvs necesarios. 
http://ourairports.com/data/
Una fuente secundaria es: 
https://datahub.io/core/airport-codes#readme   ( que es de donde tira la libreria datapackage )

Por si hubiera que seguir explorarando por el camino de la librería de datapackage mirar esto: https://datahub.io/core/airport-codes#python
El problema me lo da con el encoding. 
Esto es lo que yo había avanzado

from datapackage import Package
package = Package('https://datahub.io/core/airport-codes/datapackage.json')

## print list of all resources:
print(package.resource_names)

## print processed tabular data (if exists any)
for resource in package.resources:
    if resource.descriptor['datahub']['type'] == 'derived/csv':
        print(resource.read())
print('Tenemos un listado de',len(resource.read()),'aeropuertos')    

with open('aeropuertos2.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(resource.read())
....y tarda un monton y me da error por los caracteres raros. 

"""
################################################################################################
# 1 Determinar el directorio de trabajo ########################################################
################################################################################################
import os 
os.chdir("D:/WheWhe")
print('Directorio de trabajo fijado: D:/WheWhe') 


################################################################################################
# 2 Importar librerias #########################################################################
################################################################################################

import datetime
import csv

#########################################################
## Generar listas desde csv #############################
#########################################################
longListaAeropuertos=0
listaNamesAirports=[]
listaLatsAirports=[]
listaLongsAirports=[]
listaCountryAirports=[]
listaMunicipalityAirports=[]
listaIataCode=[]
with open('airports_clean.csv', newline='',encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        print(longListaAeropuertos)
        print(row[13])
        if row[2]=="closed":
            continue
        listaNamesAirports.append(row[3])
        listaLatsAirports.append(row[4])
        listaLongsAirports.append(row[5])
        listaCountryAirports.append(row[8])
        listaMunicipalityAirports.append(row[10])
        listaIataCode.append(row[13])
        
        longListaAeropuertos=longListaAeropuertos+1
#Pruebas borrables
#print("------------")
#print(listaMunicipalityAirports)
#print("------------")
#print(longListaAeropuertos)
#print("------------")

#########################################################
## Funcion recuperar numero aeropuerto ##################
#########################################################

def RecuperarNumeroFromIataCode(iataCode):
    #corregir codigos
    
    #https://en.wikipedia.org/wiki/IATA_airport_code
    if iataCode=="BER":
        iataCode="TXL" # Berlin (BER) – Berlin Tegel Airport (TXL) and Berlin Schönefeld Airport (SXF), both of which may be replaced by Berlin Brandenburg Airport (BER) in the future
    if iataCode=="BUH":
        iataCode="OTP" # Bucharest (BUH) – Otopeni (OTP) is named after the town of Otopeni which the airport is located, while the city also has another airport inside the city limits, Băneasa (BBU).
    if iataCode=="BUE":
        iataCode="EZE" #Buenos Aires (BUE) – Ezeiza (EZE) is named after the suburb in Ezeiza Partido which the airport is located, while the city also has another airport in city proper, Aeroparque Jorge Newbery (AEP).
    if iataCode=="CHI":
        iataCode="ORD" #Chicago (CHI) – O'Hare (ORD), named after Orchard Field, the airport's former name which took it, and Midway (MDW)
    if iataCode=="JKT":
        iataCode="CGK" #Jakarta (JKT) – Soekarno–Hatta (CGK) is named after Cengkareng, the district in which the airport is located, while the city also has another airport, Halim Perdanakusuma (HLP). JKT had referred to the city's former airport, Kemayoran Airport which is now closed.
    if iataCode=="LON":
        iataCode="LHR" #London (LON) – Heathrow (LHR), Gatwick (LGW), London City (LCY),[3] Stansted (STN), Luton (LTN) and Southend (SEN)
    if iataCode=="MIL":
        iataCode="MXP" #Milan (MIL) – Malpensa (MXP), Linate (LIN) and Orio al Serio (BGY)
    if iataCode=="YMQ":
        iataCode="YUL" #Montreal (YMQ) – Trudeau (YUL), Mirabel (YMX), and Saint-Hubert (YHU)
    if iataCode=="MOW":
        iataCode="DME" #Moscow (MOW) – Sheremetyevo (SVO), Domodedovo (DME), Vnukovo (VKO)
    if iataCode=="NYC":
        iataCode="JFK" #New York City (NYC) – John F. Kennedy (JFK, formerly Idlewild (IDL)), La Guardia (LGA), and Newark Liberty (EWR)
    if iataCode=="OSA":
        iataCode="KIX" #Osaka (OSA) – Kansai (KIX) and Itami (ITM, formerly OSA)
    if iataCode=="PAR":
        iataCode="CDG" #Paris (PAR) – Orly (ORY), Charles de Gaulle (CDG), Paris–Le Bourget Airport (LBG) and Beauvais–Tillé Airport (BVA)
    if iataCode=="RIO":
        iataCode="GIG" #Rio de Janeiro (RIO) – Galeão (GIG) and Santos Dumont (SDU)
    if iataCode=="ROM":
        iataCode="FCO" #Rome (ROM) – Fiumicino (FCO) and Ciampino (CIA)
    if iataCode=="SAO":
        iataCode="CGH" #São Paulo (SAO) – Congonhas (CGH), Guarulhos (GRU) and Campinas (VCP)
    if iataCode=="SPK":
        iataCode="CTS" #Sapporo (SPK) – Chitose (CTS) and Okadama (OKD)
    if iataCode=="SEL":
        iataCode="ICN" #Seoul (SEL) – Incheon (ICN) and Gimpo (GMP, formerly SEL)
    if iataCode=="STO":
        iataCode="ARN" #Stockholm (STO) – Arlanda (ARN), Bromma (BMA), Nyköping–Skavsta (NYO) and Västerås (VST)
    if iataCode=="TYO":
        iataCode="HND" #Tokyo (TYO) – Haneda (HND) and Narita (NRT)
    if iataCode=="YTO":
        iataCode="YYZ" #Toronto (YTO) – Pearson (YYZ), Bishop (YTZ), Hamilton (YHM), and Waterloo (YKF)
    if iataCode=="WAS":
        iataCode="IAD" #Washington, D.C. (WAS) – Dulles (IAD), Reagan (DCA), and Baltimore–Washington (BWI)
    if iataCode=="BJS":
        iataCode="PEK" #Or using a code for the city in one of the major airport and then assign another code to another airport: Beijing (BJS) – Capital (PEK) and Nanyuan (NAY)
    #Bangkok (BKK) – Suvarnabhumi (BKK) and Don Mueang (DMK)
    #Dubai (DXB) – International (DXB) and Al Maktoum (DWC)
    #Johannesburg (JNB) – O. R. Tambo (formerly Jan Smuts) (JNB) and Lanseria (HLA)
    #Kuala Lumpur (KUL) – Sepang (KUL) and Subang (SZB)
    #Medellín (MDE) – José María Córdova (MDE) and Olaya Herrera (EOH)
    #Nagoya (NGO) – Centrair (NGO) and Komaki (NKM)
    #Shanghai (SHA) – Pudong (PVG) and Hongqiao (SHA)
    #Taipei (TPE) – Taoyuan (TPE) and Songshan (TSA)
    #Tehran (THR) – Imam Khomeini (IKA) and Mehrabad (THR)

    #https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_A
    # hasta
    #https://en.wikipedia.org/wiki/List_of_airports_by_IATA_code:_Z
    if iataCode=="BAK":
        iataCode="GYD" #BAK is common IATA code for Heydar Aliyev International Airport (IATA: GYD) and Zabrat Airport (IATA: ZXT).
    if iataCode=="BHZ":
        iataCode="CNF" #BHZ is common IATA code for Tancredo Neves International Airport (IATA: CNF) and Belo Horizonte/Pampulha – Carlos Drummond de Andrade Airport (IATA: PLU).
    if iataCode=="CHI":
        iataCode="ORD" #CHI is common IATA code for O'Hare International Airport (IATA: ORD), Midway International Airport (IATA: MDW), DuPage Airport (IATA: DPA), Gary/Chicago International Airport (IATA: GYY), Chicago Executive Airport (IATA: PWK) and Chicago Rockford International Airport (IATA: RFD).
    if iataCode=="DTT":
        iataCode="DTW" #DTT is common IATA code for Detroit Metropolitan Airport (IATA: DTW), Coleman A. Young International Airport (IATA: DET) and Willow Run Airport (IATA: YIP).
    if iataCode=="EAP":
        iataCode="BSL" #EAP is IATA code used for EuroAirport Basel Mulhouse Freiburg (IATA: BSL / MLH).
    if iataCode=="IZM":
        iataCode="ADB" #IZM is common IATA code for Adnan Menderes Airport (IATA: ADB) and Çiğli Air Base (IATA: IGL).
    if iataCode=="JKT":
        iataCode="CGK" #JKT is common IATA code for Soekarno–Hatta International Airport (IATA: CGK) and Halim Perdanakusuma Airport (IATA: HLP).
    if iataCode=="MMA":
        iataCode="MMX" #MMA covers Malmö Airport (IATA: MMX) only.    
    if iataCode=="OSA":
        iataCode="KIX" #OSA is common IATA code for Kansai International Airport (IATA: KIX), Osaka International Airport (IATA: ITM) and Kobe Airport (IATA: UKB).    
    if iataCode=="REK":
        iataCode="KEF" #REK is common IATA code for Keflavík International Airport (IATA: KEF) and Reykjavík Airport (IATA: RKV).
    if iataCode=="RIO":
        iataCode="GIG" #RIO is common IATA code for Rio de Janeiro–Galeão International Airport (IATA: GIG), Santos Dumont Airport (IATA: SDU) and Santa Cruz Air Force Base (IATA: SNZ).
    if iataCode=="SDZ":
        iataCode="LSI" #SDZ is common IATA code for Sumburgh Airport (IATA: LSI), Tingwall Airport (IATA: LWK) and Scatsta Airport (IATA: SCS).
    if iataCode=="SFY":
        iataCode="BDL" #SFY is common IATA code for Bradley International Airport (IATA: BDL) and Westover Metropolitan Airport (IATA: CEF).
    if iataCode=="TCI":
        iataCode="TFS" # TCI is common IATA code for Tenerife–South Airport (IATA: TFS) and Tenerife–North Airport (IATA: TFN).
    if iataCode=="TYO":
        iataCode="NRT" #TYO is common IATA code for Narita International Airport (IATA: NRT), Haneda Airport (IATA: HND) and Yokota Air Base (IATA: OK
    if iataCode=="YEA":
        iataCode="YEG" #YEA is common IATA code for Edmonton International Airport (IATA: YEG) and former Edmonton City Centre Airport (IATA: YXD).

    # descubierto durante pruebas
    if iataCode=="ORL":
        iataCode="MCO" 
    if iataCode=="CAS":
        iataCode="CMN"

    for ae in range (longListaAeropuertos):
        if iataCode==listaIataCode[ae]:
            return ae
    return("unknown Airport")

#########################################################
## funcion convertir numeros texto a float ##############
#########################################################

#borrable

def FromNumText2Num(numeroComoTexto):
    posicionPunto=numeroComoTexto.find(".")
    enteros=numeroComoTexto[0: posicionPunto]
    decimales=numeroComoTexto[posicionPunto+1:len(numeroComoTexto)]
    numero=int(enteros)+(int(decimales)/100)
    return (numero)
#print(FromNumText2Num("192.00"))
#print(FromNumText2Num("192.01"))
#print(FromNumText2Num("12345.67"))

    
#########################################################
## llamada a API Amadeus recuperar numero aeropuerto ####
#########################################################
#https://github.com/ardydedase/amadeus-python
#https://sandbox.amadeus.com/getting-started

#(ciudadElegidaUsuario,primerDiaPosibleSalida,ultimoDiaPosibleSalida,duracion,currencyByUser)=('London',"2018-06-25","2018-06-30",6,'GBP')

def GenerateListsFromCity(ciudadElegidaUsuario,primerDiaPosibleSalida,ultimoDiaPosibleSalida,duracion,currencyByUser):
    # importamos los modulos necesarios de amadeus y le pasamos la pw
    from amadeus import Flights
    flights = Flights('fdNSGaHphktgPWytHqHqBVhcQVVs4uVr')
    from amadeus import Hotels
    hotels = Hotels('fdNSGaHphktgPWytHqHqBVhcQVVs4uVr')
    
    #aseguramos que las fechas van con guiones
    primerDiaPosibleSalida_Corregido=primerDiaPosibleSalida.replace("/","-")
    ultimoDiaPosibleSalida_Corregido=ultimoDiaPosibleSalida.replace("/","-")
        
    #calculo fecha regreso  <- de momento no se emplea
    primerDiaPosibleSalida_datetime = datetime.datetime.strptime(primerDiaPosibleSalida, '%Y-%m-%d')
    primerDiaPosibleVuelta_datetime = primerDiaPosibleSalida_datetime + datetime.timedelta(days=7)
    primerDiaPosibleVuelta=(str(primerDiaPosibleVuelta_datetime)[:10])
    
    ultimoDiaPosibleSalida_datetime = datetime.datetime.strptime(ultimoDiaPosibleSalida, '%Y-%m-%d')
    ultimoDiaPosibleVuelta_datetime = ultimoDiaPosibleSalida_datetime + datetime.timedelta(days=duracion)
    ultimoDiaPosibleVuelta=(str(ultimoDiaPosibleVuelta_datetime)[:10])

    #Obtener codigo ciudad salida
    respCity = flights.auto_complete(term=ciudadElegidaUsuario)
    print(respCity)
    codigoCiudadSalida=respCity[0]['value']
    print("Buscando vuelos desde",codigoCiudadSalida)

    # Buscar vuelos
    flights = Flights('fdNSGaHphktgPWytHqHqBVhcQVVs4uVr')
    respVuelos = flights.inspiration_search(
        origin=codigoCiudadSalida,
        departure_date=primerDiaPosibleSalida_Corregido+"--"+ultimoDiaPosibleSalida_Corregido,
        duration=6,
        max_price=200)
    print(respVuelos)

    # Generar listas con resultados
    listadoDestinosNfila=[]
    listadoDestinosLargo=[]
    listadoDestinosCodigo=[]
    listadoDestinosFechaSalida=[]
    listadoDestinosFechaVuelta=[]
    listadoDestinosPrecioVuelo=[]
    listadoDestinosLats=[]
    listadoDestinosLons=[]
    listadoDestinosPais=[]
    listadoDestinosPrecioHoteles=[]

    #for i in range (len(respVuelos['results'])):    
    #    print(RecuperarNumeroFromIataCode(respVuelos['results'][i]['destination']),respVuelos['results'][i]['destination'],respVuelos['results'][i]['price'])
     
    for i in range (len(respVuelos['results'])):    
        posicionEnListas=RecuperarNumeroFromIataCode(respVuelos['results'][i]['destination'])
        listadoDestinosNfila.append(posicionEnListas)
        listadoDestinosLargo.append(listaMunicipalityAirports[posicionEnListas])
        listadoDestinosCodigo.append(respVuelos['results'][i]['destination'])      
        listadoDestinosFechaSalida.append(respVuelos['results'][i]['departure_date'])
        listadoDestinosFechaVuelta.append(respVuelos['results'][i]['return_date'])
        listadoDestinosPrecioVuelo.append(respVuelos['results'][i]['price'])
        listadoDestinosLats.append(listaLatsAirports[posicionEnListas])
        listadoDestinosLons.append(listaLongsAirports[posicionEnListas])
        listadoDestinosPais.append(listaCountryAirports[posicionEnListas])
        
        #print("inciando busqueda hotel cerca de",listaLatsAirports[posicionEnListas],",",listaLongsAirports[posicionEnListas] )
        respHoteles=hotels.search_circle(
                    check_in=respVuelos['results'][i]['departure_date'],
                    check_out=respVuelos['results'][i]['return_date'],
                    latitude=float(listaLatsAirports[posicionEnListas]),
                    longitude=float(listaLongsAirports[posicionEnListas]),
                    currency=currencyByUser,
                    radius=30)#km from coordenates=km from airport
        print(respHoteles)
        precioMedioHoteles=0
        numeroHotelesConsiderar=min(len(respHoteles['results']),5) #max number of hotels to consider in mean price
        if numeroHotelesConsiderar==0:
            precioMedioHoteles=1000*duracion
        else:
            for h in range (numeroHotelesConsiderar):
                precioDeCadaHotel=respHoteles['results'][h]['total_price']['amount']
        #        print(precioDeCadaHotel)
        #        print(respHoteles['results'][h]['location']['latitude'])
        #        print(respHoteles['results'][h]['location']['longitude'])
                precioMedioHoteles=precioMedioHoteles+float(precioDeCadaHotel)
            precioMedioHoteles=round(precioMedioHoteles/numeroHotelesConsiderar,2)
        listadoDestinosPrecioHoteles.append(precioMedioHoteles)  

    return(listadoDestinosNfila,listadoDestinosLargo,
           listadoDestinosCodigo,listadoDestinosFechaSalida,
           listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,
           listadoDestinosLats,listadoDestinosLons,
           listadoDestinosPais,listadoDestinosPrecioHoteles)

#Probamos que la funciíon funciona
#Madrid en euros
(listadoDestinosNfila,listadoDestinosLargo,listadoDestinosCodigo,listadoDestinosFechaSalida,
 listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,listadoDestinosLats,listadoDestinosLons,
 listadoDestinosPais,listadoDestinosPrecioHoteles)=GenerateListsFromCity('mAdrid',"2018-06-25","2018-06-30",6,'EUR')
for i in range (len(listadoDestinosNfila)):
    print()
    print(listadoDestinosNfila[i],listadoDestinosLargo[i],
          listadoDestinosCodigo[i],listadoDestinosFechaSalida[i],
          listadoDestinosFechaVuelta[i],listadoDestinosPrecioVuelo[i],
          listadoDestinosLats[i],listadoDestinosLons[i],
          listadoDestinosPais[i],listadoDestinosPrecioHoteles[i])
#Londres en euros
(listadoDestinosNfila,listadoDestinosLargo,listadoDestinosCodigo,listadoDestinosFechaSalida,
 listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,listadoDestinosLats,listadoDestinosLons,
 listadoDestinosPais,listadoDestinosPrecioHoteles)=GenerateListsFromCity('London',"2018-06-25","2018-06-30",6,'GBP')
for i in range (len(listadoDestinosNfila)):
    print()
    print(listadoDestinosNfila[i],listadoDestinosLargo[i],
          listadoDestinosCodigo[i],listadoDestinosFechaSalida[i],
          listadoDestinosFechaVuelta[i],listadoDestinosPrecioVuelo[i],
          listadoDestinosLats[i],listadoDestinosLons[i],
          listadoDestinosPais[i],listadoDestinosPrecioHoteles[i])



