#!/usr/bin/env python
import code
import sys
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import EarthLocation,SkyCoord, AltAz
from astropy.time import Time
from astropy import units as u


PLOT = 0

zenDist = []
maxAzVel = []
maxAltVel = []
maxAzAcc = []
max AzVel = []

def main():
    
    for i in np.linspace(-2,2,8):
        zenDist.append(i)
        print i
        maxAz.append(maxSpeed(i))
        print maxAz[-1]
        
    plot()
       





def breaktoconsole():
    code.interact(local=locals())
    return 


def maxSpeed (zenDist):

    # LT observing location 
    obsLoc = EarthLocation(lat='28.7624', lon='17.8792', height=2400*u.m)  

    #zenDist = float(sys.argv[1])
    ra = 0 # float(sys.argv[2])
    dec = obsLoc.lat.deg - zenDist


    # Set time at the first point of Libra J2000 where 0h0m0s is transiting the meridian.
    obsTime = Time('2000-09-22 22:30:08.5')  
    coord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree)

    # Initiate the lists of values
    azAng= [0]
    altAng= [0]
    azAcc= [0]
    azVel= [0]
    altAcc= [0]
    altVel= [0]
    timeAr= [0]


    for step in range(-600, 600):
        obsTime += u.second
        
        aa = AltAz(location=obsLoc, obstime=obsTime)
        altAz = coord.transform_to(aa)

        
        
        
        timeAr.append(step)
        altAng.append(altAz.alt.deg)
        azAng.append(altAz.az.deg)
        altVel.append(abs(altAz.alt.deg-altAng[-2]))
        
        if ((altAz.az.deg-azAng[-2]) > 180):
            azVel.append(abs(altAz.az.deg-azAng[-2]-360))
        else:
            azVel.append(abs(altAz.az.deg-azAng[-2]))
            
        azAcc.append((abs(azVel[-2] - azVel[-1])))
        altAcc.append((abs(altVel[-2] - altVel[-1])))
        
        
        
    if PLOT:
        fig, ax1 = plt.subplots()
        ax1.plot(timeAr[3:], altAcc[3:], 'b-')
        ax1.set_xlabel('time (s)')
        ax1.set_ylabel('Angular Velocity [deg / s]', color='b')
        ax1.set_ylim(bottom=0)
        ax1.tick_params('y', colors='b')

        ax2 = ax1.twinx()

        ax2.plot(timeAr[3:], altAng[3:], 'r.')
        ax2.set_ylabel('Angle', color='r')
        ax2.tick_params('y', colors='r')

        fig.tight_layout()
        plt.show()
        

    return max(altAcc[3:])

def plot():

    fig, ax1 = plt.subplots()
    ax1.plot(zenDist, maxAz, 'b-')
    ax1.set_xlabel('Zenith Distance at transit')
    ax1.set_ylabel('Angular Velocity [deg / s]', color='b')
    ax1.tick_params('y', colors='b')

    fig.tight_layout()
    plt.show()


main()
