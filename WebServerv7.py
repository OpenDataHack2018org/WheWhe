#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://jolthgs.wordpress.com/2012/02/12/desarrollo-web-con-python-y-web-py-parte-3/
import web
from web import form
print("Importado web.py. Version:",web.__version__)
import numpy as np
import pandas as pd
import os 
from netCDF4 import Dataset

MainDirectory="D:/WheWhe/"
os.chdir("D:/WheWhe")
print('Directorio de trabajo fijado: D:/WheWhe/') 

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
    primerDiaPosibleVuelta_datetime = primerDiaPosibleSalida_datetime + datetime.timedelta(days=duracion)
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
        print(i)
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
        #print(respHoteles)
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

#########################################################
# Big Mac Index Function#################################
#########################################################   
highestPrice=6.8
euroAreaPrice=4.8
CountryList=["AR","AU","BR","GB","CA","CL","CN","CO","CR","CZ","DK","EG","HK","HU","IN","ID","IL","JP","LV","LT","MY","MX","NZ","NG","PK","PE","PH","PL","RU","SA","SG","ZA","KR","LK","SE","CH","TW","TH","TR","AE","UA","US","UY","VN","AT","BE","EE","FI","FR","DE","GR","IE","IT","NL","PT","ES","LU","IS","MT"]
dollar_price=[4.0,4.7,5.1,4.4,5.3,4.3,3.2,3.8,4.0,3.8,4.9,1.9,2.6,3.4,2.8,2.7,4.8,3.4,3.3,3.4,2.3,2.6,4.5,6.2,3.4,3.3,2.6,3.0,2.3,3.2,4.4,2.4,4.1,3.8,6.1,6.8,2.3,3.7,2.8,3.8,1.6,5.3,4.9,2.9,4.2,5.0,3.9,5.6,5.1,4.8,4.1,5.0,5.1,4.5,3.9,4.8,highestPrice,highestPrice,euroAreaPrice]
dictionary = dict(zip(CountryList, dollar_price))
def BigMacIndex(country,currency):
    bigMacIndex=0
    cheapestPrice=1.6
    fromdollartopound=0.745629863
    fromdollartoeuro=0.848789796
    if country in dictionary:
        bigMacIndex=dictionary[country]
    else:
        bigMacIndex=cheapestPrice
    if currency=="USD":
        bigMacIndex=bigMacIndex
    elif currency=="EUR":
        bigMacIndex=bigMacIndex*fromdollartoeuro
    elif currency=="GBP":
        bigMacIndex=bigMacIndex*fromdollartopound
    else:
        print("we are not ready to that currency...try GBP, EUR, USD")
    return bigMacIndex
#BigMacIndex("ES","EUR")

##################################################
## Clima1: extract lon/lat from .nc ##############
##################################################

def LonLatFromNC(FileName,VarName): 

    fh = Dataset(MainDirectory+FileName, mode='r')
    print('Probando a abrir archivo creado con estas caracteristicas')
    #print(fh.variables)
    lons = fh.variables['longitude'][:]
    lats = fh.variables['latitude'][:]
    #time = fh.variables['time'][:]
    #var = fh.variables[VarName][:]
    #var_units = fh.variables[VarName].units
    fh.close() #con esto cerramos el archivo para no dañarlo
    
    return {'lons':lons, 'lats':lats}

##############################################
## Clima2: extract var from .nc ##############
##############################################

def GetVarFromNC(FileName,VarName, lon_index, lat_index,arrival_index,departure_index): 

    fh = Dataset(MainDirectory+FileName, mode='r')
    print('Probando a abrir archivo creado con estas caracteristicas')
    #print(fh.variables)
    #lons = fh.variables['longitude'][:]
    #lats = fh.variables['latitude'][:]
    #time = fh.variables['time'][arrival_index:departure_index]
    var = fh.variables[VarName][arrival_index:departure_index,lat_index, lon_index]
    #var_units = fh.variables[VarName].units
    fh.close() #con esto cerramos el archivo para no dañarlo
    
    return var

#############################################################################################
## ClimaMAIN: function to extract indices given lon,lat,arrival date and departure date #####
#############################################################################################

def climate_indices(lon, lat, arrival_date, departure_date):
    
    init_date =  datetime.datetime.strptime('2018-05-01', '%Y-%m-%d')

    arrival_date =  datetime.datetime.strptime(arrival_date, '%Y-%m-%d')
    departure_date = datetime.datetime.strptime(departure_date, '%Y-%m-%d')
    
    index_arrival = (arrival_date - init_date).days
    index_departure = (departure_date - init_date).days
        
    # 1) find nearest neighbour
    # 1.1) extract lon/lat once (assume al .nc have the same grid)
    file_name = "ProbLluvia.nc"
    var_name = "pop"    
    lonlat = LonLatFromNC(file_name, var_name)
    # 1.2) compute abs value of differences between input lon lat and lonlat array
    # 1.3) take minimums
    lon_nn_index = np.argmin(abs(lonlat['lons'] - lon))
    lat_nn_index = np.argmin(abs(lonlat['lats'] - lat))
    
    ## Dictionary of all indices
    var_all = {'ProbLluvia.nc': 'pop',
               'PrecMaxMax.nc': 'tp',
               'PrecMaxMin.nc': 'tp',
               'PrecMaxPromedio.nc': 'tp',
               'TempMaxMax.nc': 'mx2t24',
               'TempMaxMin.nc': 'mx2t24',
               'TempMaxPromedio.nc': 'mx2t24',
               'TempMinMax.nc': 'mn2t24',
               'TempMinMin.nc': 'mn2t24',
               'TempMinPromedio.nc': 'mn2t24',
               'TCCAverage.nc': 'tcc',
               'TCCMax.nc': 'tcc',
               'TCCMin.nc': 'tcc',
               'TCCProbHigh.nc': 'tcc'
               }
    
    #file_name = "ProbLluvia.nc"
    #var_name = "pop"
    ## 
    
    # 2) Extract time series for the location of interest
    
    ind_ts = []
    
    for file_name in var_all:
        print()
        print(file_name, var_all[file_name], lon_nn_index, lat_nn_index,index_arrival,index_departure)
        indices = GetVarFromNC(file_name, var_all[file_name], lon_nn_index, lat_nn_index,index_arrival,index_departure)
        ind_ts.append(indices)
    
    out_index = np.zeros((14), dtype=float)
    out_index[0] = ind_ts[0].mean()
    out_index[1] = ind_ts[1].max()    
    out_index[2] = ind_ts[2].min()
    out_index[3] = ind_ts[3].mean()
    out_index[4] = ind_ts[4].max()    
    out_index[5] = ind_ts[5].min()
    out_index[6] = ind_ts[6].mean()
    out_index[7] = ind_ts[7].max()    
    out_index[8] = ind_ts[8].min()
    out_index[9] = ind_ts[9].mean()
    out_index[10] = ind_ts[10].mean()
    out_index[11] = ind_ts[11].max()    
    out_index[12] = ind_ts[12].min()
    out_index[13] = ind_ts[13].mean()
    
    if (out_index[2] < 0):
        out_index[2] = 0
    
    out_all = {'ProbRain': out_index[0],
           'PrecMax': out_index[1],
           'PrecMin': out_index[2],
           'PrecAverage': out_index[3],
           'TempMaxMax': out_index[4],
           'TempMaxMin': out_index[5],
           'TempMaxAverage' : out_index[6],
           'TempMinMax': out_index[7],
           'TempMinMin': out_index[8],
           'TempMinAverage': out_index[9],
           'TCCAverage': out_index[10],
           'TCCMax': out_index[11],
           'TCCMin': out_index[12],
           'TCCProbHigh': out_index[13]
           }
    return out_all


#########################################################
## Web server ###########################################
#########################################################

urls = (
  '/', 'index'
)

plantilla = web.template.render('./templates/')

app = web.application(urls, globals())

myform = form.Form(
  form.Textbox('departureCity', form.notnull, description="Departure city", class_="textEntry",\
  value="3 letters ICAO code", id="cajatext", post="  City where you want to start your travel. It should has an airport.", size="15"),
  
  form.Textbox('firstPossibleDepartureDate', form.notnull, description="First possible departure date", class_="textEntry",\
  value="YYYY-MM-DD", id="cajatext", post="  First  day on which you can start your trip.", size="15"),
  
  form.Textbox('lasttPossibleDepartureDate', form.notnull, description="Last possible departure date", class_="textEntry",\
  value="YYYY-MM-DD", id="cajatext", post="  Last day on which you can start your trip: The more flexible you are, the better suggestions we can give you!!", size="15"),

  form.Textbox('duration', form.notnull, description="Trip duration", class_="textEntry",\
  value="number of days", id="cajatext", post="  How many days will your trip last?", size="15"),

  form.Textbox('currency', form.notnull, description="Your local currency", class_="textEntry",\
  value="EUR", id="cajatext", post="  EUR/GBP/USD...Which is the currency in the departure airport?", size="15"),
  
#  form.Textbox("nombre"),
#  form.Textbox("id1",
#    form.notnull,
#    form.regexp('\d+', 'Debe ser un dígito'),
#    form.Validator('Debe ser más de 5', lambda x:int(x)>5)),
#  form.Textbox("id2",
#    form.notnull,
#    form.regexp('\d+', 'Debe ser un dígito'),
#    form.Validator('Debe ser más de 5', lambda x:int(x)>5)),
#  form.Textarea('observacion'),
#  form.Checkbox('reenviar'),
  form.Dropdown('yourProfile', ['Equilibrated tourist','Tan-aholic','Student','Only one live','Keep me warm'],description="Your tourist profile",\
  post="how would you describe your self?", size="5"),

  form.Textbox('budget', form.notnull, description="What is your budget?", class_="textEntry",\
  value="500", id="cajatext", post=" How much money you want to spent? (EUR/GBP/USD...)", size="15"),

  )


def Respuesta(ciudadSalida,firstPossibleDepartureDate,lasttPossibleDepartureDate,duration,currency,profile,budget):
    #return ("Gran exito! Nombre: %s, ID: %s" % (nombreIntroducido, (valor1+valor2)))

    #https://stackoverflow.com/questions/19622407/2d-numpy-array-to-html-table?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    
    budgetFloat=float(budget)
    
    (listadoDestinosNfila,listadoDestinosLargo,listadoDestinosCodigo,listadoDestinosFechaSalida,
     listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,listadoDestinosLats,listadoDestinosLons,
     listadoDestinosPais,listadoDestinosPrecioHoteles)=GenerateListsFromCity(ciudadSalida,firstPossibleDepartureDate,lasttPossibleDepartureDate,int(duration),currency)

    numberOfLines=len(listadoDestinosPrecioHoteles)
    
    listadoBigMacIndex=[]
    for i in range(numberOfLines):
        listadoBigMacIndex.append(BigMacIndex(listadoDestinosPais[i],currency))
        
    listadoPrecAverage=[]
    listadoPrecRange=[]
    listadoPrecProb=[]
    listadoCloudCovAverage=[] 
    listadoCloudCovRange=[] 
    listadoCloudCovProb=[] 
    ListadoTempMaxAverage=[]
    ListadoTempMaxRange=[]
    ListadoTempMinAverage=[]
    ListadoTempMinRange=[]
    for i in range(numberOfLines):
        longitude=float(listadoDestinosLons[i])
        latitude=float(listadoDestinosLats[i])
        fechaSalida=listadoDestinosFechaSalida[i]
        fechaVuelta=listadoDestinosFechaVuelta[i]
        
        dictOfResults=climate_indices(longitude, latitude, fechaSalida, fechaVuelta)
        listadoPrecAverage.append(dictOfResults['PrecAverage'])
        listadoPrecRange.append(dictOfResults['PrecMax']-(dictOfResults['PrecMin']))
        listadoPrecProb.append(dictOfResults['ProbRain'])
        listadoCloudCovAverage.append(dictOfResults['TCCAverage'])
        listadoCloudCovRange.append(dictOfResults['TCCMax']-(dictOfResults['TCCMin'])) 
        listadoCloudCovProb.append(dictOfResults['TCCProbHigh']) 
        ListadoTempMaxAverage.append(dictOfResults['TempMaxAverage'])
        ListadoTempMaxRange.append(dictOfResults['TempMaxMax']-(dictOfResults['TempMaxMin'])) 
        ListadoTempMinAverage.append(dictOfResults['TempMinAverage'])
        ListadoTempMinRange.append(dictOfResults['TempMinMax']-(dictOfResults['TempMinMin'])) 

    listadoIndex=[]
    wwindex=0    
    for i in range(numberOfLines):
        if profile=='Equilibrated tourist': #WheWhe index
            
            moneyYouWillSpent=(float(listadoDestinosPrecioVuelo[i])+float(listadoDestinosPrecioHoteles[i])+float(listadoBigMacIndex[i])*20*int(duration))
            moneyInYourPocket=(budgetFloat-moneyYouWillSpent)
            priceIndex=moneyInYourPocket/budgetFloat
            if moneyInYourPocket<0:
                priceIndex=0
            
            precipatationIndex=0.5*(1-float(listadoPrecProb[i]))+0.5*((1-listadoPrecAverage[i])/50)
            temperatureIndex=1-(abs((float(ListadoTempMaxAverage[i])-(37+22)/2))/((37+22)/2))
            cloudIndex=1-listadoCloudCovProb[i]
            
            weatherIndex=0.4*precipatationIndex+0.4*temperatureIndex+0.2*cloudIndex
                
            wwindex=priceIndex*0.5+weatherIndex*0.5

        elif profile=='Tan-aholic':
            wwindex=(1-listadoCloudCovAverage[i])
        elif profile=='Student':
            moneyYouWillSpent=(float(listadoDestinosPrecioVuelo[i])+float(listadoDestinosPrecioHoteles[i])+float(listadoBigMacIndex[i])*20*int(duration))
            moneyInYourPocket=(budgetFloat-moneyYouWillSpent)
            wwindex=moneyInYourPocket/budgetFloat
            if moneyInYourPocket<0:
                wwindex=0
        elif profile=='Only one live':
            precipatationIndex=0.5*(1-float(listadoPrecProb[i]))+0.5*((1-listadoPrecAverage[i])/50)
            temperatureIndex=1-(abs((float(ListadoTempMaxAverage[i])-(37+22)/2))/((37+22)/2))
            cloudIndex=1-listadoCloudCovProb[i]
            
            weatherIndex=0.4*precipatationIndex+0.4*temperatureIndex+0.2*cloudIndex
                
            wwindex=weatherIndex
        elif profile=='Keep me warm':   #Rutty and Scott 2010 , see https://earth-perspectives.springeropen.com/articles/10.1186/s40322-016-0034-y
            wwindex=1-(abs((float(ListadoTempMaxAverage[i])-(37+22)/2))/((37+22)/2))
        else:
            print("we have a proplem")
        listadoIndex.append(wwindex)

    
    df=pd.DataFrame(list(map(list, zip (listadoDestinosLargo,listadoDestinosFechaSalida,
     listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,
     listadoDestinosPrecioHoteles,listadoBigMacIndex,
     listadoPrecAverage,listadoPrecRange,listadoPrecProb,listadoCloudCovAverage,listadoCloudCovRange,
     listadoCloudCovProb,ListadoTempMaxAverage,ListadoTempMaxRange,ListadoTempMinAverage,ListadoTempMinRange,listadoIndex))))

    df.columns=["Destination","Departure","Return","Flight Price","Hotel Price","BigMacIndex",
                "Total Precipitation","Range","Rain Probability","Cloud Coverage","range","% of cloudy days",
                "Max Temp","Range","Min Temp","Range","WheWhe Score"]    

    df2=df.copy(deep=True)
    
    df2=df2.sort_values(by="WheWhe Score",ascending=False)

    indexesTexts=[]
    for i in range (numberOfLines):
        indexesTexts.append(i+1)
    df2.index=indexesTexts
    
    html = df2.to_html()
    
    return html

class index:
  #Metodo de llegada
  def GET(self):
    form = myform()
    return plantilla.formulario_2(form)

# Método POST
  def POST(self):
     form = myform()
     if not form.validates():
       return plantilla.formulario_2(form)
     else:
       return Respuesta(form['departureCity'].value,form['firstPossibleDepartureDate'].value,form['lasttPossibleDepartureDate'].value,form['duration'].value,form['currency'].value,form['yourProfile'].value,form['budget'].value)

if __name__ == "__main__":
    app.run()
