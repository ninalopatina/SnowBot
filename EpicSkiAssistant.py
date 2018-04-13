# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:58:21 2017

@author: ninalopatina
"""

#this code inputs weather and traffic data for ski resorts included in the
#Tahoe Epic Pass (Kirkwood, Heavenly, Northstar),
#plus other user-selected resorts (Mt. Rose),
#Outputs the optimal resort to go to & when based on the user's preferences.

dir_home = '/Users/ninalopatina/Box Sync/snowbot/github/SnowBot/'
import os
#go to home directory
os.chdir(dir_home)
#get all the parameters
import snow_funcs #functions the main script calls on

import snow_params #separate file with all the parameters
prms = snow_params.importer() #params stored as prms.__ ; see snow_params.py for all

#import other packages
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#get the weather dictionary
wdict = snow_funcs.pickle_wunderground()


def make_float(df, var):
    df[var] = df[var].astype(float)
    return df

def dash_fig(dictt):
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
        df = make_float(df, 'high_temp')
        df = make_float(df, 'low_temp')
#        df = make_float(df, 'precip_percent')        
        dictt[day] = df #transpose is harder to read, easier to plot from
        ax = plt.subplot(gs[rs[day], cs[day]])
        df[prms.sum_keys].plot(ax = ax)#,legend=False)
        ax.set_ylim([-5,105])
        ax.set_title('day ' + str(day))
        ax.set_xticks([0,1,2,3])
        ax.set_xticklabels(df.index.values)
        ax.axhline(prms.freeze,color='k')
        ax.text(0,prms.freeze,'freezing temp')
    
    
    #save the dashboard figure   
    os.chdir(prms.dir_fig)
    fig.savefig(str(prms.num_days) +'DayDash' + str(prms.today_file) + '.pdf', format='pdf')

#plot a dashboard figure
dash_fig(dictt = wdict)
