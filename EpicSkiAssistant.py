# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:58:21 2017

@author: ninalopatina
"""

#this code inputs weather and traffic data for ski resorts included in the 
#Tahoe Epic Pass (Kirkwood, Heavenly, Northstar), 
#plus other user-selected resorts (Mt. Rose), 
#Outputs the optimal resort to go to & when based on the user's preferences. 


#get all the parameters
import snow_params #separate file with all the parameters
prms = snow_params.importer() #params stored as prms.__ ; see snow_params.py for all 

import snow_funcs #functions the main script calls on

#get the weather dictionary
wdict = snow_funcs.pickle_wunderground()

def dash_fig(dictt):
    import snow_params 
    prms = snow_params.importer() 
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec 
    #make a figure for a quick glance at the next few days' weather
    #create the new figure + subplot parameters
    fig = plt.figure(figsize = (prms.gridspecsC*prms.sizerC,prms.gridspecsR*prms.sizerR))
    gs = gridspec.GridSpec(prms.gridspecsR,prms.gridspecsC)
    rs = []
    cs = []
    for i in range(prms.gridspecsR):
        for j in range(prms.gridspecsC):
            rs.append(i)
            cs.append(j)
            
    for day,df in dictt.iteritems():
        df = df.transpose() #transpose is harder to read, easier to plot from
        #fix temp stored as unicode issue:
        df.high_temp = df.high_temp.astype(float)
        df.low_temp = df.low_temp.astype(float)
        dictt[day] = df #transpose is harder to read, easier to plot from
        ax = plt.subplot(gs[rs[day], cs[day]])
        df[prms.sum_keys].plot(ax = ax)#,legend=False)
        ax.set_ylim([-5,65])
        ax.set_title('day ' + str(day))
        ax.set_xticks([0,1,2,3])
        ax.set_xticklabels(df.index.values)
        ax.axhline(prms.freeze,color='k')
        ax.text(0,prms.freeze,'freezing temp')

#plot a dashboard figure
dash_fig(dictt = wdict)