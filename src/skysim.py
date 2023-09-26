#!/usr/bin/env python3
"""
Script to generate a simulated star catalogue, for stars around the Andromeda
galaxy
"""
#new comment here
import math
import random

NSRC = 1_000

def generate_positions(nsrc):
    # Determine Andromeda location in ra/dec degrees
    # from wikipedia
    ra = '01:42:44.3'
    dec = '40:16:09'

    # convert to decimal degrees

    d, m, s = dec.split(':')
    dec = int(d)+int(m)/60+float(s)/3600

    h, m, s = ra.split(':')
    ra = 15*(int(h)+int(m)/60+float(s)/3600)
    ra = ra/math.cos(dec*math.pi/180)

    # make 1000 stars within 1 degree of Andromeda
    ras = []
    decs = []
    for i in range(nsrc):
        ras.append(ra + random.uniform(-1,1))
        decs.append(dec + random.uniform(-1,1))
    return ras, decs

def save_positions_to_file(ras, decs):
    # now write these to a csv file for use by my other program
    f = open('catalogue.csv','w')
    print("id,ra,dec", file=f)
    assert len(ras) == len(decs)
    for (i, (ra, dec)) in enumerate(zip(ras, decs)):
        print("{0:07d}, {1:12f}, {2:12f}".format(i, ra, dec), file=f)

def main():
    ras, decs = generate_positions(NSRC)
    # several hundred intervening lines
    save_positions_to_file(ras, decs)

# if this is invoked as a script, then
if __name__ == "__main__":
    main()
