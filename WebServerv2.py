#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://jolthgs.wordpress.com/2012/02/12/desarrollo-web-con-python-y-web-py-parte-3/
import web
from web import form
print("Importado web.py. Version:",web.__version__)
import numpy as np
import pandas as pd
import os 

os.chdir("D:/WheWhe")
print('Directorio de trabajo fijado: D:/WheWhe') 

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
#  form.Dropdown('prioridad', ['baja', 'media', 'alta'])
  
  )


def Respuesta(ciudadSalida,firstPossibleDepartureDate,lasttPossibleDepartureDate,duration,currency):
    #return ("Gran exito! Nombre: %s, ID: %s" % (nombreIntroducido, (valor1+valor2)))

    #https://stackoverflow.com/questions/19622407/2d-numpy-array-to-html-table?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    
    (listadoDestinosNfila,listadoDestinosLargo,listadoDestinosCodigo,listadoDestinosFechaSalida,
     listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,listadoDestinosLats,listadoDestinosLons,
     listadoDestinosPais,listadoDestinosPrecioHoteles)=GenerateListsFromCity(ciudadSalida,firstPossibleDepartureDate,lasttPossibleDepartureDate,int(duration),currency)

    numberOfLines=len(listadoDestinosPrecioHoteles)
    
    listadoBigMacIndex=[]
    for i in range(numberOfLines):
        listadoBigMacIndex.append(BigMacIndex(listadoDestinosPais[i],currency))
        
    
    
    
    
    
    df=pd.DataFrame(list(map(list, zip (listadoDestinosNfila,listadoDestinosLargo,listadoDestinosCodigo,listadoDestinosFechaSalida,
     listadoDestinosFechaVuelta,listadoDestinosPrecioVuelo,listadoDestinosLats,listadoDestinosLons,
     listadoDestinosPais,listadoDestinosPrecioHoteles,listadoBigMacIndex))))

    df.columns=["Destination Code","Destination","Code","Departure","Return","Flight Price","Lat","Lon","Country","Hotel Price","BigMacIndex"]    

    indexesTexts=[]
    for i in range (numberOfLines):
        indexesTexts.append(i+1)
    df.index=indexesTexts

    html = df.to_html()
    
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
       return Respuesta(form['departureCity'].value,form['firstPossibleDepartureDate'].value,form['lasttPossibleDepartureDate'].value,form['duration'].value,form['currency'].value)

if __name__ == "__main__":
    app.run()
