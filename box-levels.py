#!/usr/bin/python

print("Outputting levels of 3D infinite cubic well.")

# Problem:
# nx, ny, and nz can be any integer from 1 to infty.
# E is propto nx**2+ny**2+nz**2
# What's the energy and degeneracy of each level?
# (For some of the lower-ish levels.)

# Method:
# 1. We know that nx**2+ny**2+nz**2 must be an integer.
# 2. Loop over this integer (e)
# 3. For each integer, loop nx, ny, and nz range from 1 to, say, 10.
# 4. Calculate nx**2+ny**2+nz**2 and compare to e.  Count successes.
# We are then pretty sure that we've got the degeneracies correct up to energy 10**2+1**2+1**2=102.
# Yes, I would call this brute force.

import numpy as np

nmax=100

elevel=0

for e in range(3,nmax**2+1**2+1**2):
    d=0
    for nx in range(1,nmax+1):
        for ny in range(1,nmax+1):
            for nz in range(1,nmax+1):
                if(nx**2+ny**2+nz**2==e):
                    print(nx,ny,nz)
                    d=d+1
    if(d>0):
        elevel=elevel+1
        print("Level %d, energy %d, degeneracy %d."%(elevel,e,d))
