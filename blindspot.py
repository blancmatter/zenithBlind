#!/usr/bin/env python
import code
import sys
import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import EarthLocation,SkyCoord, AltAz
from astropy.time import Time
from astropy import units as u


# Plotting of each zenDist switch
PLOT = 0



zenDist = []
maxAltVel = []
maxAltAcc = []
maxAzVel = []
maxAzAcc = []

def main():
    
    for i in createZenDist:
        
        zenDist.append(i)
        
        results = maxSpeed(i)
        print (i, "of 10000") 
        print results
        print
       
        maxAltVel.append(results[0])
        maxAltAcc.append(results[1])
        maxAzVel.append(results[2])
        maxAzAcc.append(results[3])
 
    plot()
       





def breaktoconsole():
    code.interact(local=locals())
    return 


def maxSpeed (zenDist):
    # Returns the maximum axis speeds and accelerations of Alt and Cass for a given zenDist

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
        altVel.append(altAz.alt.deg-altAng[-2])
        
        if ((altAz.az.deg-azAng[-2]) > 180):
            azVel.append(abs(altAz.az.deg-azAng[-2]-360))
        else:
            azVel.append(abs(altAz.az.deg-azAng[-2]))
            
        azAcc.append((abs(azVel[-2] - azVel[-1])))
        altAcc.append((abs(altVel[-2] - altVel[-1])))
        
        
        
    if PLOT > 0:
        
        fig, [[ax1,ax2],[ax3,ax4],[ax5,ax6]] = plt.subplots(nrows=3, ncols=2)
        
       
         
        ax1.plot(timeAr[3:], altAng[3:], 'r.')
        ax1.set_xlabel('time (s)')
        ax1.set_ylabel('Position [deg]', color='b')
        ax1.tick_params('y', colors='b')

        ax2.plot(timeAr[3:], azAng[3:], 'r.')
        ax2.set_xlabel('time (s)')
        ax2.set_ylabel('Position [deg]', color='b')
        #ax2.set_ylim(bottom=-1)
        ax2.tick_params('y', colors='b')
      
      
        ax3.plot(timeAr[3:], altVel[3:], 'b.')
        ax3.set_xlabel('time (s)')
        ax3.set_ylabel('Angular Velocity [deg / s]', color='b')
        ax3.tick_params('y', colors='b')
      
        ax4.plot(timeAr[3:], azVel[3:], 'b.')
        ax4.set_xlabel('time (s)')
        ax4.set_ylabel('Angular Velocity [deg / s]', color='b')
        ax4.tick_params('y', colors='b')
        
        
        ax5.plot(timeAr[3:], altAcc[3:], 'g.')
        ax5.set_xlabel('time (s)')
        ax5.set_ylabel('Angular Acceleration [deg / s^2]', color='b')
        ax5.tick_params('y', colors='b')
        
        ax6.plot(timeAr[3:], azAcc[3:], 'g.')
        ax6.set_xlabel('time (s)')
        ax6.set_ylabel('Angular Acceleration [deg / s^2]', color='b')
        ax6.tick_params('y', colors='b')
        
       
        #fig.tight_layout()
        plt.show()
        
        # PLOT+=-1
        

    return (max(altVel[3:]),max(altAcc[3:]),max(azVel[3:]),max(azAcc[3:]))

def createZenDist:
    # Creates a zenDist population
    


def plot():

    fig, [[ax1,ax2],[ax3,ax4]] = plt.subplots(nrows=2, ncols=2)
    
    
    ax1.plot(zenDist, maxAltVel, 'b-')
    ax1.set_xlabel('Zenith Distance at transit')
    ax1.set_ylabel('Angular Velocity [deg / s]', color='b')
    ax1.tick_params('y', colors='b')
    
    
    ax2.plot(zenDist, maxAzVel, 'r-')
    ax2.set_xlabel('Zenith Distance at transit')
    ax2.set_ylabel('Angular Velocity [deg / s]', color='b')
    ax2.tick_params('y', colors='b')
    
    ax3.plot(zenDist, maxAltAcc, 'g-')
    ax3.set_xlabel('Zenith Distance at transit')
    ax3.set_ylabel('Max Angular Acceleration [deg / s^2]', color='b')
    ax3.tick_params('y', colors='b')
    
    ax4.plot(zenDist, maxAzAcc, 'k-')
    ax4.set_xlabel('Zenith Distance at transit')
    ax4.set_ylabel('Max Angular Acceleration [deg / s^2]', color='b')
    ax4.tick_params('y', colors='b')

    fig.tight_layout()
    plt.show()
    
    breaktoconsole()


main()
