# Schechter Function 
# In Class Assignment 1: Part 1 
# Jan 25 2018

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#get_ipython().magic('matplotlib inline')


# Define the Schechter Luminosity function (in terms of Magnitude)
# Takes as input:  an array of Absolute Magnitudes M 
# defaults from Smith+2009 in Kband
# nstar = 0.0166*h^3 Mpc^-3
# Mstar = -23.19 + 5*log(h)
# alpha = -0.81
def Schechter(M,nstar,Mstar,alpha):
    
    return 0.4*np.log(10)*nstar*10**(0.4*(Mstar - M)*(alpha +1.0))*np.exp(-10**(0.4*(Mstar - M)))


# Compute default accounting for little h
Mstar = -23.19 #- 5*np.log10(h)
nstar = 0.0166 #*h**3


# Plot the Schechter Function
#################################
fig = plt.figure(figsize=(10,10))
ax = plt.subplot(111)

# Create an array to store Kband Magnitudes from -26 to -17
MK = np.arange(-26,-17,0.1)

# Plot the default values
# y axis is log 
plt.semilogy(MK,Schechter(MK,nstar,Mstar,-0.81), color='blue', linewidth=5, label='Smith+09')

# change alpha and overplot
plt.semilogy(MK,Schechter(MK,nstar,Mstar,-0.6), color='blue', linestyle=":", linewidth=3, label=r'low $\alpha$')
plt.semilogy(MK,Schechter(MK,nstar,Mstar,-1.35), color='blue', linestyle="--",linewidth=3, label=r'high $\alpha$')

# Add labels
plt.xlabel(r'M$_k$ + 5Log($h$)', fontsize=22)
plt.ylabel(r'$\Phi$ (Mpc$^{-3}h^3$/mag)', fontsize=22)

#set axis limits
plt.xlim(-17,-26)

#adjust tick label font size
label_size = 22
matplotlib.rcParams['xtick.labelsize'] = label_size 
matplotlib.rcParams['ytick.labelsize'] = label_size

# add a legend with some customizations.
legend = ax.legend(loc='upper right',fontsize='x-large')

# Save to a file
ax.set_rasterized(True)
plt.savefig('Schechter_Jan25.eps', rasterized=True, dpi=350)







