# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:50:53 2017

@author: ninalopatina
"""

def importer():
    import os
    import API_keys_script
    
    #settings:
    newcall =0 # are you calling the APIs anew, or debugging with stored data? 
    num_days = 4 #number forecast days: max # is 4
    
    #API keys:
    #### these variables are all stored in a separate, un-shared file:
    API_keys_folder = '/Users/ninalopatina/Box Sync/snowbot'
    os.chdir(API_keys_folder)
    API_keys = API_keys_script.importer()  #import all the keys
    
    #for reference, API keys are as below
#    #google maps, for traffic:
#    google_directions_api = 'AIzyourkeyhere'
#    google_distance_matrix_api = 'AIzyourkeyhere'
#    #wunderground for weather data: 
#    wunderground = '665yourkeyhere'    

    #dictionary of the wunderground stations closest to the resort for each resort:
    resort_dict ={'northstar':'KCATRUCK137','kirkwood':'KCAKIRKW3','heavenly':'KCASOUTH112','mtrose':'KNVINCLI37'}
    
    #wunderground settings
    degree_mode = 'fahrenheit' # 'fahrenheit' or 'celsius'
    meas_mode = 'in' # 'in' or 'cm'
    #keys you're accessing in wunderground weather dictionary
    weather_keys = ['date','date','date','high','low','avewind','maxwind','snow_day','snow_night','qpf_allday','pop']
    weather_keys2 = ['weekday_short','month','day',degree_mode,degree_mode,'mph','mph',meas_mode,meas_mode,meas_mode]
    #keys you're saving from the wunderground dict
    weather_key_save = ['day','month','date','high_temp','low_temp','avg_wind','max_wind','snow_day','snow_night','all_day_precip','precip%']
    sum_keys = ['high_temp','low_temp','max_wind','precip%'] #summary keys
        
    #plot parameters
    gridspecsR = 2 #rows
    gridspecsC = 2 #columns
    sizerC = 5 #multiply column # by this to get size
    sizerR = 5 #multiply row # by this to get size
    
    freeze = 32 #freezing temp for graph

    
    #other variables to plug in from other sources:
    other_vars = ['distance-miles','distance-minutes','runs_open','runs_total','lifts_open','lifts_total','base','summit']
    
    class Bunch(object):
        def __init__(self, adict):
            self.__dict__.update(adict)
        
    prms = Bunch(locals())
 
    return prms