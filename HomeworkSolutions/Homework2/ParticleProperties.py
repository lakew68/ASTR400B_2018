## ASTR400B Homework 2
## Code to return properties of a given particle of a given type
## G. Besla

import numpy as np
import astropy.units as u
from ReadFile import Read


# define a function that takes in the desired particle type
#  and the particle number and prints the 3D position, 
#  velocity and mass
#  input:  Ptype e.g. 1,2,3
#  PNum:  particle number e.g. 100 
#  filename "MW_000.txt"
# Return 3D Pos and 3D Vel and mass

def ParticleInfo(PType, PNum, filename):


	# read in the file 
	time, total, data = Read(filename)

	#create an array to store indexes of particles of desired Ptype
	index = np.where(data['type'] == PType)

	# create new arrays with the m, x, y, z, 
	# vx, vy, vz of just the Ptype desired
	# units are added using astropy
	mnew = data['m'][index]*1e10*u.Msun
	xnew = data['x'][index]*u.kpc
	ynew = data['y'][index]*u.kpc
	znew = data['z'][index]*u.kpc
	vxnew = data['vx'][index]*u.km/u.s
	vynew = data['vy'][index]*u.km/u.s
	vznew = data['vz'][index]*u.km/u.s
    
     	# 3D position
	# Round to 3 decimal places
	R3D = np.round(np.sqrt(xnew[PNum-1]**2 + ynew[PNum-1]**2 + znew[PNum-1]**2),3)
    
   	# 3D velocity
	# Round to 3 decimal places
	V3D = np.round(np.sqrt(vxnew[PNum-1]**2 + vynew[PNum-1]**2 + vznew[PNum-1]**2),3)
    	
	# Mass
	# Round to 3 decimal places
	Mass = np.round(mnew[PNum-1],3)
    
	return R3D, V3D, Mass



 
# Example case. 100th Disk particle

R, V, M = ParticleInfo(2,100,"MW_000.txt")
print("")
print("3D Distance:",R)
print("")
print("3D Velocity:",V)
print("")
print("Mass of Particle:", M)
print("")
print("3D Distance in Lyr:",np.round(R.to(u.lyr),3))
print("")  
    

