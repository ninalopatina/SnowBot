# SnowBot 
is a Python library for assisting users in choosing a ski resort to go to given 
weather and traffic conditions

This is a work in progress and will be updated with new features

#Getting started:
#1) download all of the files and folders in this repository. 
#scripts are: 
#i)EpicSkiAssistant, with the main code
#ii)snow_params, with the parameters
#iii)snow_func, with supporting functions that EpicSkiAssistant calls

#2) In EpicSkiAssistant.py & snow_params.py, change dir_home to the folder
#containing these files.

#3)  
# option A: change dir_API to a directory with a wunderground API formatted as 
#described in snow_params.py, or

# option B: use the pickled data, and, if it's not current to today, change 
#prms.today_file to the date of the file in the data folder. Make sure that, 
#in snow_params.py, newcall = 0

#4) run EpicSkiAssistant.py

#5) Look at the output: 
#the current output is a .pdf of high temp, low temp, max wind, and precip% for
# heavenly, mt rose, kirkwood, and northstar, over the next 4 days. 
#which variables and which resorts are displayed can be adjusted in the snow_params
