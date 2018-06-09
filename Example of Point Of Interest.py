# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:15:21 2018

Example of code for recovering 
"""


import requests
import json
import datetime
import numpy as np

def ReturnCityCenterCoord(city):   
    #titles=[]
    #grades=[]
    lats=[]
    lons=[]
    
    #city="Rome"
    cityCorrected=city.replace(" ","%20")
    url="https://api.sandbox.amadeus.com/v1.2/points-of-interest/yapq-search-text?city_name="+cityCorrected+"&number_of_results=10&apikey=gXJFnblmo12YO0DtWs6Zs3q8Yuc4h0qS"
    URLresponse = requests.get(url)
    print(URLresponse)
        
    if URLresponse.status_code == 200:
        print("bien!!!")
    else:
        print("error")
    URLresponse.content
    decoded=json.loads(URLresponse.content.decode('utf-8'))
    for j in range(len(decoded["points_of_interest"])):
        #titles.append(decoded["points_of_interest"][j]["title"])   
        #grades.append(decoded["points_of_interest"][j]["grades"]['yapq_grade'])   
        lats.append(decoded["points_of_interest"][j]["location"]['latitude'])
        lons.append(decoded["points_of_interest"][j]["location"]['longitude'])
    #print(titles,lats, lons, grades)
    #print(sum(grades)/len(grades))
    print(sum(lats)/len(lats))
    print(sum(lons)/len(lons))
    return(sum(lats)/len(lats),sum(lons)/len(lons))    
    
ReturnCityCenterCoord("Rome")  