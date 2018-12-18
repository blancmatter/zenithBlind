#!/usr/bin/env python
import pickle as pkl
import sys
import matplotlib.pyplot as plt

[zenDist, maxAltVel, maxAzVel, maxAltAcc, maxAzAcc] = pkl.load( open( "plotdata.pkl", "rb" ) )

zenDist = []
maxAltVel = []
maxAltAcc = []
maxAzVel = []
maxAzAcc = []

def main():
    for i in range (1,len(sys.argv)):
        print "here number", sys.argv[i]
    exit()
    plot()
    
    
def upkl(filename):
    [a, b, c, d, e] = pkl.load( open( filename, "rb" ) )
    
    zenDist.append(a)
    maxAltVel.append(b)
    maxAzVel.append(c)
    maxAltAcc.append(d)
    maxAzAcc.append(e)
    
    return

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


main()    
