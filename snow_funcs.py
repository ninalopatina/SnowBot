# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:58:21 2017

@author: ninalopatina
"""
import os
import pickle
import pandas as pd
import snow_params
import datetime
from urllib2 import urlopen
import json

def pickle_wunderground():
    prms = snow_params.importer()

    wdict = {} #initialize dictionary for storing dataframes with wunderground data
    os.chdir(prms.dir_data) #go to pickle directory
    if prms.newcall==1: #if you're calling the API
        for day in range(prms.num_days): #check weather for # days set in snow_params
            #initialize dataframes with columns = resorts, index = weather measurements:
            df = pd.DataFrame(index = prms.weather_key_save, columns = prms.resort_dict.keys())
            for name,pws in prms.resort_dict.iteritems(): #pws is the name of the weather station closest to that resort
                #name = resort name, pws = wunderground station name, #df = initialized dataframe,
                #day = day in the for loop, today_file = filename you'll store this pickle under
                df, parsed_json = get_wunderground(name, pws, df,day)
                wdict[day]=df #dictionary of dataframes of measurements by resort; dict over forecast days

        pickle.dump(wdict, open('df'+prms.today_file, "wb" ) ) #pickle the forecast data dictionary of dataframes
    else: #if not calling, load pickled data
        
        wdict = pd.read_pickle( open('df'+ prms.today_file, "rb" ) )
    return wdict

def get_wunderground(name, pws, df,day):
    prms = snow_params.importer()
    #API specifies your API key + the weather station (pws, below)
    wurl = 'http://api.wunderground.com/api/'+prms.API_keys.wunderground+'/forecast/q/pws:'+pws+'.json'
    req = urlopen(wurl)
    parsed_json = json.load(req) #load a parsed json file from the url
    os.chdir(prms.dir_data) #go to pickle directory
    pickle.dump(parsed_json, open(name+prms.today_file, "wb" )) #pickle all these data for future reference
    #FYI, how to read the parsed_json file:
    #parsed_json['forecast']['simpleforecast']['forecastday'][0].keys() #all the keys on day 1
    tot_keys= len(prms.weather_keys) # total # keys set in parameters

    for wkn,wk in enumerate(prms.weather_keys): #wkn = weather key number, wk = weather key
        if wkn<tot_keys-1: #if you're not on the last key
            wk2= prms.weather_keys2[wkn]
            aa = parsed_json['forecast']['simpleforecast']['forecastday'][day][wk][wk2]
        else:
            aa = parsed_json['forecast']['simpleforecast']['forecastday'][day][wk]
        if aa is u'': #if you got a blank value from API
            ### temporary manual fix:
            print('ERROR in API recall!!!!!') #temporary code to alert me to API failures till I fix this
            print('error at field #' + str(wkn) + ',field ' + str(wk) + ', weather station ' + str(pws) +', day ' + str(day))
            aa = 49 #temp fix for glitch in kirkwood high temp
        df.set_value(prms.weather_key_save[wkn], name,aa) #save the values for that key in a dataframe
    return df, parsed_json
