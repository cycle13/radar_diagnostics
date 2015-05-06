#! /usr/bin/env python
from matplotlib import use
use('agg')
import pyart
from matplotlib import pyplot as plt
import sys
import numpy as np
from time import time
from netCDF4 import num2date, date2num

if __name__ == '__main__':
    filename = sys.argv[1]
    print('Doing ' + filename)
    outdir = sys.argv[2]
    radar = pyart.io.read(filename)
    datestr = num2date(radar.time['data'][0], radar.time['units'])
    sstr = datestr.strftime('%Y%m%d_%H%M%S')
    print(sstr)
    #create an instance of the class using our radar
    display = pyart.graph.RadarMapDisplay(radar)
    #create a Matplotlib figure
    f = plt.figure(figsize = [17,8])
    #now we are going to do a three panel plot, resolution is a basemap parameter and determines the resolution of
    #the coastline.. here we set to intermediate or 'i' ('h' for high 'l' for low)
    plt.subplot(2, 3, 1)
    display.plot_ppi_map('differential_reflectivity',
                         vmin = -7, vmax = 7,
                         resolution = 'i')
    plt.subplot(2, 3, 2)
    display.plot_ppi_map('reflectivity',
                         vmin = -8, vmax = 64,
                         resolution = 'i')
    plt.subplot(2, 3, 3)
    display.plot_ppi_map('velocity',
                         vmin = -15, vmax = 15,
                         resolution = 'i')

    plt.subplot(2, 3, 4)
    display.plot_ppi_map('clutter_filtered_differential_reflectivity',
                         vmin = -7, vmax = 7,
                         resolution = 'i')
    plt.subplot(2, 3, 5)
    display.plot_ppi_map('clutter_filtered_reflectivity',
                         vmin = -8, vmax = 64,
                         resolution = 'i')
    plt.subplot(2, 3, 6)
    display.plot_ppi_map('clutter_filtered_copolar_correlation_coefficient',
                         vmin = 0.5, vmax = 1,
                         resolution = 'i')
    print('saveing ' + outdir + 'diag_'+sstr+'.png' )
    plt.savefig(outdir + '/diag_'+sstr+'.png')



