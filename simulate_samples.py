'''
Generates data containing the area of the mandlebrotset obtained with a fixed number of iterations and different number of samples. Simulation can be run 
a predefined amount of times. Area is determined with four different methods. Data is stored as txt files. 
'''

import numpy as np
from functions import compute_areas, setup_grid
from sampling_methods import random_sampling, lhc_sampling, ortho_sampling, quasi_montecarlo


# set parameters of the complex grid
cmin = -2-1.3j
cmax = 0.6+1.3j

# set the parameters of the simulation
samples = 10 ** 2
max_iter = 100

# set parameters of the cartesian grid the grid
xmin, xmax, ymin, ymax, xrange, yrange, xdim, ydim, delta = setup_grid(cmin, cmax, samples)

# -----------------------------------------------------------------------------------------------------------------------------------------------
# RUN MANDLEBROT SIM WITH DIFFERENT SAMPLING TECHNIQUES
# -----------------------------------------------------------------------------------------------------------------------------------------------
data = []
random_x = []
lhc_x = []
ortho_x = []
qmc_x = []
sims = 10

for i in range(0, sims):
    print('', end = '\r')
    print(f"simulating: {int(i / sims * 100)} %", end = '\r')
    
    # save area of mandelbrot
    total = 0
    unescaped = 0
    areas_mandelbrot = []
    
    # compute total area 
    total_area = xrange * yrange
    
    # random sampling
    rand_samp_complex_vals = random_sampling(xmin, ymin, xrange, yrange, samples)
    rand_samp_areas_mandelbrot = compute_areas(rand_samp_complex_vals, max_iter, total_area)
    random_x.append(rand_samp_areas_mandelbrot)
    
    # latin hypercube samling
    lhc_samp_complex_vals = lhc_sampling(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples)
    lhc_samp_areas_mandelbrot = compute_areas(lhc_samp_complex_vals, max_iter, total_area)
    lhc_x.append(lhc_samp_areas_mandelbrot)
    
    # orthogonal sampling 
    ortho_samp_complex_vals = ortho_sampling(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples)
    ortho_samp_areas_mandelbrot = compute_areas(ortho_samp_complex_vals, max_iter, total_area)
    ortho_x.append(ortho_samp_areas_mandelbrot)
    
    # quasi montecarlo sampling
    quasi_montecarlo_complex_vals = quasi_montecarlo(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples)
    quasi_montecarlo_areas_mandelbrot = compute_areas(quasi_montecarlo_complex_vals, max_iter, total_area)
    qmc_x.append(quasi_montecarlo_areas_mandelbrot)
 
# -----------------------------------------------------------------------------------------------------------------------------------------------
# STORE DATA OF SIMS IN TXT FILES
# -----------------------------------------------------------------------------------------------------------------------------------------------

# save data
random_x = np.asarray(random_x)
lhc_x = np.asarray(lhc_x)
ortho_x= np.asarray(ortho_x)
qmc_x = np.asarray(qmc_x)
    
np.savetxt("data/samplesim_random.csv", random_x, delimiter=",")
np.savetxt("data/samplesim_lhc.csv", lhc_x, delimiter=",")
np.savetxt("data/samplesim_orthogonal.csv", ortho_x, delimiter=",")
np.savetxt("data/samplesim_qmc.csv", qmc_x , delimiter=",")

print('')
print('finished simulating')





