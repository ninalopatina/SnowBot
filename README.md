# SnowBot 
is a Python library for assisting users in choosing a ski resort to go to given weather and traffic conditions.

This is a work in progress and will be updated with new features.

# Getting started:
# Step 1: Set up the codebase
download all of the files and folders in this repository. 
The scripts are: 
i) EpicSkiAssistant, with the main code, 
ii) snow_params, with the parameters, 
iii) snow_func, with supporting functions that EpicSkiAssistant calls.

# Step 2: Set the home directory
In EpicSkiAssistant.py & snow_params.py, change dir_home to the folder containing these files.

# Step 3: Set up your data: pickled or fresh from the API
option A: change dir_API to a directory with a wunderground API formatted as described in snow_params.py, or

option B: use the pickled data, and, if it's not current to today, change prms.today_file to the date of the file in the data folder. Make sure that, in snow_params.py, newcall = 0

# Step 4: run EpicSkiAssistant.py

# Step 5: Look at the output
The current output is a .pdf of high temp, low temp, max wind, and precip% for Heavenly, Mt Rose, Kirkwood, and Northstar, over the next 4 days. 
The variables and resorts that are displayed can be adjusted in snow_params
