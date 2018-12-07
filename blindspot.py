#!/usr/bin/env python
import code
import sys
import matplotlib.pyplot as plt
from astropy.coordinates import EarthLocation,SkyCoord, AltAz
from astropy.time import Time
from astropy import units as u


# LT observing location 
obsLoc = EarthLocation(lat='28.7624', lon='17.8792', height=2400*u.m)  

zenDist = float(sys.argv[1])
ra = float(sys.argv[2])
dec = obsLoc.lat.deg - zenDist


# Set time at the first point of Libra J2000 where 0h0m0s is transiting the meridian.
obsTime = Time('2000-09-22 22:30:00')  
coord = SkyCoord(ra=ra*u.degree, dec=dec*u.degree)

# Initiate the lists of values
azAng=[0]
altAng=[0]
azVel=[0]
altVel=[0]
timeAr=[0]


for step in range(1200):
    obsTime += u.second
    
    aa = AltAz(location=obsLoc, obstime=obsTime)
    altAz = coord.transform_to(aa)

    #code.interact(local=locals())
    
    
    timeAr.append(step)
    altAng.append(altAz.alt.deg)
    azAng.append(altAz.az.deg)
    altVel.append(abs(altAz.alt.deg-altAng[-2]))
    azVel.append(abs(altAz.az.deg-azAng[-2]))
    
fig, ax1 = plt.subplots()
ax1.plot(timeAr[2:], azVel[2:], 'b-')
ax1.set_xlabel('time (s)')
ax1.set_ylabel('Angular Velocity [deg / s]', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()

ax2.plot(timeAr[2:], azAng[2:], 'r.')
ax2.set_ylabel('Angle', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()
