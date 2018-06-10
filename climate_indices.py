#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 13:48:36 2018

@author: mcucchi
"""

from netCDF4 import Dataset
import numpy as np
#import xarray as xr
import datetime
#from datetime import datetime, timedelta #for writing dates in nc
#import time #for current time record in .nc
import os
#TO BE CHANGED!!!!!
MainDirectory="D:/WheWhe/" #en esta carpeta se almacena este script y los archivos generados
os.chdir(MainDirectory)

#############################################
## 1: extract lon/lat from .nc ##############
#############################################

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

#############################################
## 2: extract var from .nc ##############
#############################################

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

#####################################################################################
## MAIN: function to extract indices given lon,lat,arrival date and departure date #####
#####################################################################################

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
    
#    ds = xr.open_dataset("/home/mcucchi/projects/whewhe/" + file_name, decode_times=False)
#    
#    var_array = ds['pop']
#    
#    var_time_series = var_array.sel(lon=280.0, lat=75.0)


climate_indices(40, 3, "2018-06-12", "2018-06-15")
