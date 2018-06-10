#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 21:43:00 2018

@author: mcucchi
"""

##########################################################
## 1: importar todas las librerías #######################
##########################################################
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.basemap import Basemap
import netCDF4
#from datetime import datetime, timedelta #for writing dates in nc
#import time #for current time record in .nc
import os
rutaGralCarpeta="/mnt/DATA/PROGETTI/11_WHEWHE/" #en esta carpeta se almacena este script y los archivos generados
os.chdir(rutaGralCarpeta)

rutaTempMax="D:/51 temp max"
rutaTempMin="D:/52 temp min"  
rutaPrecipt="D:/228 precipt"
# to be changed
rutaTCC='/mnt/DATA/PROGETTI/11_WHEWHE/tcc/'

###################################################################
## 4: funcion volcado a archivo .nc ###############################
###################################################################
# basado en http://www.ceda.ac.uk/static/media/uploads/ncas-reading-2015/11_create_netcdf_python.pdf

def GuardarEnNC(arrayAGuardar,nombreFichero,descripcion,nombreVariable,unidades,lats,lons,timeserie):      

    #creating a NetCDF file
    print ('Inicio creacion archico nc '+nombreFichero+'.nc')
    dataset = Dataset (nombreFichero, 'w',
                       format='NETCDF4_CLASSIC')
    #print ('Generado fichero'+nombreFichero+' con formato '+dataset.file_format)
    #print ('Caracteristicas iniciales:')
    #print (dataset.dimensions)
    #print ('Debe ser un diccionario vacio')
    
    #Create dimensions
    lat = dataset.createDimension('lat', len(lats))
    #print('creada dimension lat : '+str(dataset.dimensions ['lat']))
    lon = dataset.createDimension('lon', len(lons)) 
    #print('creada dimension len : '+str(dataset.dimensions ['lon']))
    time = dataset.createDimension('time', None)
    #print('creada dimension time: '+str(dataset.dimensions ['time'])+'¿Es ilimitada?:'+str(time.isunlimited())) 
    #print('Resumen dimensiones creadas:')
    #print('Nombre Tamaño Ilimitada')
    #for dimname in dataset.dimensions.keys():
    #    dim = dataset.dimensions[dimname]
    #    print (dimname, len(dim), dim.isunlimited())
        
    #Create coordinate variables for N-dimensions
    times = dataset.createVariable('time', np.float64, ('time',))
    latitudes = dataset.createVariable('latitude', np.float32, ('lat',))
    longitudes = dataset.createVariable('longitude', np.float32, ('lon',))
    
    #create the actual N-d variable
    datos = dataset.createVariable(nombreVariable, np.float32, ('time','lat','lon'))
    #print ('creada variable para almacenar datos vacia:', dataset.variables[nombreVariable])
    
    #print('Resumen variables creadas:')
    #print('Nombre Tipo Dimensiones Tamaño')
    #for varname in dataset.variables.keys():
    #    var = dataset.variables[varname]
    #    print (varname, var.dtype, var.dimensions, var.shape)
        
    #Creation of global Attributes
    dataset.description = descripcion
    import time #importar aqui porque si no se lia con variable time en siguiente linea
    dataset.history = 'Created on' + time.ctime(time.time())
    dataset.source = 'Calculated from C3S CDS Seasonal Forecast'
    
    #Variable Attributes
    latitudes.units = 'degree_north'
    longitudes.units = 'degree_east'
    datos.units = unidades
    times.units = 'hours since 0001-01-01 00:00:00'
    times.calendar = 'gregorian'

    #Repaso del archivo
    #print('Características del archivo creado a falta de escribir datos:')    
    #print('Descripcion: '+dataset.description)
    #print('Historia: '+dataset.history)
    #print('Dimensiones: '+str(dataset.dimensions))
    
    #writing data
    latitudes[:] = lats
    longitudes[:] = lons
    #print ('latitudes =\n', latitudes[:])
    #print ('latitudes =\n', latitudes[:])
    
    #growing data along unlimited dimension
    nPasosTiempo=arrayAGuardar.shape[0]
    #print ('data shape before adding data = ', datos.shape)
    datos[0:int(nPasosTiempo),:,:] = arrayAGuardar
    #print ('data shape before adding data =', datos.shape)
    
    # Fill in times.    <-----------------esta pensado para generar una lista de meses. Innecesario
#    dates = []
#  
#    def add_several_month(dt0,nMeses):# Basado en http://code.activestate.com/recipes/577274-subtract-or-add-a-month-to-a-datetimedate-or-datet/
#        dt3=dt0
#        diaDelMes=dt0.day
#        for i in range (nMeses):
#            dt1 = dt0.replace(day=1)
#            dt2 = dt1 + timedelta(days=32)
#            dt3 = dt2.replace(day=diaDelMes)
#            dt0 = dt3
#        return dt3
#    
#    for n in range(datos.shape[0]):
#        dates.append(add_several_month(datetime(2011, 1, 1),n))
#    times[:] = date2num(dates, units = times.units, calendar = times.calendar)
#    #print ('time values (in units %s): ' % times.units + '\n', times[:])

    times[:] = timeserie


    # Close, and it saved.
    dataset.close()
    
###################################################################
## 6: leer serie precipitacion ####################################
###################################################################

(variable,fechaForecast)=('164','2018-05-01')
i=0
# one in 'all' (all day) or '6to18'(from 6am to 6pm)
Hours = 'all'
TCCThreshold = 0.8

def generarArraysTotalCloudCover(variable,fechaForecast):

    #timeDim = int(1242/6)
    timeDim = 207
    
    #matrices a cero para ser rellenadas    
    seriepromedio51numbersBruto=np.zeros((timeDim,721,1440), dtype=float) 
    seriemaximo51numbersBruto = np.zeros((timeDim,721,1440), dtype=float) 
    serieminimo51numbersBruto = np.zeros((timeDim,721,1440), dtype=float)
    serietime=[]
    serieProbab51numbersBruto = np.zeros((timeDim,721,1440), dtype=float)
    
    #definicion del nombre de la variable dentro del nc
    if variable=='164':
        codigoVariableEnNc='tcc'
        ruta=rutaTCC
    else: 
        print('codigoErroneo!!!!!!!')

    #apertura de un unico archivo para capturar lat, lons, time y var_units
    print("Abriendo un primer archivo para analizar el formato")
    fhPrimerArchivo = netCDF4.Dataset(ruta+'/'+'ecmf'+variable+fechaForecast+'step_'+'6'+'.nc', mode='r')
    print(fhPrimerArchivo)
    print(fhPrimerArchivo.dimensions)
    print(fhPrimerArchivo.variables)
    lons = fhPrimerArchivo.variables['longitude'][:]
    lats = fhPrimerArchivo.variables['latitude'][:]
    #varAllNumbers = fh.variables[codigoVariableEnNc][:] #para 51 'mx2t24', para 52 'mn2t24'
    time = fhPrimerArchivo.variables['time'][:]
    number = fhPrimerArchivo.variables['number'][:]
    var_units = fhPrimerArchivo.variables[codigoVariableEnNc].units
    fhPrimerArchivo.close() #con esto cerramos el archivo para no dañarlo
    print ("Lat, lons, time y var_units netCDF Inicial importandos en arrays numpy")
    print ("Por las lats y lons obtenidas, estas indican el punto central de cada celda")

    #bucle que analiza todo
    
    Days = int(timeDim/4)

    #seriesDailyForProbs = np.zeros((1,51,721,1440), dtype=float)
    probHighTCC = np.zeros((Days, 721, 1440), dtype=float)
    seriesTemp = np.zeros((4,51,721,1440), dtype=float)

    for i in range(timeDim):
              
        print ("--Leyendo step "+str(i*6+6)+" Var: "+codigoVariableEnNc)
        fhTemporal = netCDF4.Dataset(ruta+'/'+'ecmf'+variable+fechaForecast+'step_'+str(i*6+6)+'.nc', mode='r')
        varAllNumbersTemporal = fhTemporal.variables[codigoVariableEnNc][:]
        time = fhTemporal.variables['time'][:]
        fhTemporal.close()
        print(varAllNumbersTemporal)
        
        seriepromedio51numbersBruto[i,:,:]=(np.nanmean(varAllNumbersTemporal, axis=1)) 
        seriemaximo51numbersBruto[i,:,:]=(np.nanmax(varAllNumbersTemporal, axis=1))
        serieminimo51numbersBruto[i,:,:]=(np.nanmin(varAllNumbersTemporal, axis=1))
        
        
        k = i%4

        seriesTemp[k,:,:,:] = varAllNumbersTemporal
        
        if k == 3:
            
            day_index = int(i/4)
            seriesDailyForProbs = (np.nanmean(seriesTemp, axis=0))
            varAllNumbersSiNo=seriesDailyForProbs>TCCThreshold
            probHighTCC[day_index, :, :] = np.nanmean(varAllNumbersSiNo,axis=0)
            serietime.append(time)    

    seriesDailyAverage = np.zeros((Days,721,1440), dtype=float) 
    seriesDailyMax = np.zeros((Days,721,1440), dtype=float) 
    seriesDailyMin = np.zeros((Days,721,1440), dtype=float)
    
    serieProbab51numbersBruto = probHighTCC
    
    
    
    for day in range(Days):
        
        indices = 4*day+np.arange(0,4)
        seriesDailyAverageTemp = seriepromedio51numbersBruto[indices[0]:indices[3],:,:]
        seriesDailyAverage[day,:,:] = (np.nanmean(seriesDailyAverageTemp, axis=0))
        seriesDailyMaxTemp = seriemaximo51numbersBruto[indices[0]:indices[3],:,:]
        seriesDailyMax[day,:,:] = (np.nanmax(seriesDailyMaxTemp, axis=0))
        seriesDailyMinTemp = serieminimo51numbersBruto[indices[0]:indices[3],:,:]
        seriesDailyMin[day,:,:] = (np.nanmin(seriesDailyMinTemp, axis=0))
        
    
        
    return(seriesDailyAverage,seriesDailyMax,seriesDailyMin,serietime,lons,lats,serieProbab51numbersBruto)
    
#Generate indicators for tcc
arrayTCCAverage, arrayTCCMax, arrayTCCMin, serietime, lons, lats, arrayProbHighTCC=generarArraysTotalCloudCover('164', '2018-05-01')
GuardarEnNC(arrayTCCAverage, 'TCCAverage.nc', 'TCCAverage', 'tcc', '(0 - 1)', lats, lons, serietime)
GuardarEnNC(arrayTCCMax, 'TCCMax.nc', 'TCCMax', 'tcc', '(0 - 1)', lats, lons, serietime)
GuardarEnNC(arrayTCCMin, 'TCCMin.nc', 'TCCMin', 'tcc', '(0 - 1)', lats, lons, serietime)
GuardarEnNC(arrayProbHighTCC, 'TCCProbHigh.nc', 'TCCProbHigh', 'tcc', '%', lats, lons, serietime)