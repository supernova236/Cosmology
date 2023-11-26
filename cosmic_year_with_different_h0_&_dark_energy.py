# -*- coding: utf-8 -*-
"""Cosmic year with different H0 & dark energy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YbgZGetFujdHRzoqHR3CouewBmB0whVY
"""

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

H = [67.36, 67.36-0.54, 67.36+0.54, 73.24, 73.24-1.74, 73.24+1.74,
     69.88, 69.88+1.17, 69.88-1.17, 70.46,70.46-1.18,70.46+1.18]
# Hubble constant list H
# Plank Collaboration et all. 2018, 67.36 by CMB
# A.G.RIESS et al. 73.24 by type 1a Sne
# Freedman et al. 69.88, 70.46 by TRGB

H_list = []
# Hubble constant list
set_list = []
# Initial condition list
cosmic_year_list = []
# Cosmic year depend on Hubble constant and initial condition


type_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


# function E(z)
def Cosmic_year_function(set,H0):

    def integrand(z):
        return (set[0] + (set[1]*(1+z)**4) + (set[2]*(1+z)**3) + (set[3]*(1+z)**2))** -(1/2) / (z+1) / H0

    def epoch(zs):
        out = []
        for z in zs:
            out.append((quad(integrand, 0, 10 ** 5)[0] - quad(integrand, 0, z)[0]) / (10 ** 9 * 365 * 24 * 60 * 60))
        return out

    z_end = 10 ** 2
    z_step = 10 ** -2
    z_list = np.arange(0, z_end, z_step)

    epoch_list = epoch(z_list)

    Cosmic_age = epoch_list[0]

    return(Cosmic_age)

for type in type_set:
    if type =='a':
    # dark energy, radiation, matter, curvature
        set = [0.669, 0.00, 0.331, 0.00]
    #elif type == 'b':
        #set = [0.631, 0.00, 0.369, 0.00]
    #elif type == 'c':
        #set = [0.707, 0.00, 0.293, 0.00]
    elif type == 'd':
        set = [0.6847, 0.00, 0.3153, 0.00]
    #elif type == 'e':
        #set = [0.6854, 0.00, 0.3146, 0.00]
    #elif type == 'f':
        #set = [0.6840, 0.00, 0.3160, 0.00]
    #elif type == 'g':
        #set = [0.0, 0.00, 0.3160, 0.6840]
    else:
        set = [0.00, 0.00, 1.00, 0.00]
    for H0 in H:
        H_list.append(H0)

        H0 = H0*1000/3.0842208e+22
        # kilometers per second per megaparsec into 1/s

        set_list.append(set[0])
        year = Cosmic_year_function(set, H0)
        cosmic_year_list.append(year)

# Drawing Cosmic age with different Hubble constant &initial condition
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig = plt.figure(figsize=(20, 19))
ax = plt.axes(projection='3d')
ax.scatter(H_list, set_list, cosmic_year_list, color = 'r', alpha = 0.2)
ax.set_xlabel('Hubble constant')
ax.set_ylabel('Dark Energy')
ax.set_zlabel('Age')
plt.title('Cosmic Age')
ax.set_zlim3d(9, 15)
c_list = []


for i in range(len(H_list)):
    ax.text(H_list[i],set_list[i],cosmic_year_list[i],  f'{H_list[i]:.2f}, {cosmic_year_list[i]:.1f}', size=7, zorder=1,
    color='k')