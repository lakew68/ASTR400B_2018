# IMF In Class Assignment 1:  Part 2
# Jan 25 2018

import numpy as np
from scipy.integrate import quad


# Salpeter IMF: Fractional distribution of stars from 0.1-120 Msun
# input: M (array of stellar masses)
# minimum mass and maximal mass for the integration. 
def SalpeterN(M,Mmin, Mmax):
    
    # Determine magnitude of the integral
    Norm = quad(lambda M: M**(-2.35), Mmin,Mmax)
    # Normalize to one
    A = 1./Norm[0]

    # return the normalized function.
    return A*M**(-2.35)


# Determine the fraction of stars more massive than the sun  (M= 1.0)
Frac = quad(lambda M: SalpeterN(M,0.1,120),1.0,120)
print("Fractional number of stars more massive than the Sun =", np.round(Frac[0],3))

# test 1:
#Frac = quad(lambda M: SalpeterN(M,0.1,120),0.1,1)
#print("Fractional number of stars less massive than the Sun =", np.round(Frac[0],3))

# test 2:
#Frac = quad(lambda M: SalpeterN(M,0.1,120),0.1,120)
#print("Should return 1.0 =", np.round(Frac[0],3))






