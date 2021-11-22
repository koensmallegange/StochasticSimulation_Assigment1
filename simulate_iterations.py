'''
Generates data containing the area of the mandlebrotset obtained with a fixed number of samples and different number of iterations. Simulation can be run 
a predefined amount of times. Area is determined with four different methods. Data is stored as txt files. 
'''

import numpy as np
import csv
from itertools import zip_longest
from functions import compute_areas, setup_grid
from sampling_methods import random_sampling, lhc_sampling, ortho_sampling, quasi_montecarlo

# set parameters of the complex grid
cmin = -2-1.3j
cmax = 0.6+1.3j

# set the parameters of the simulation
samples =  10 ** 2


# set parameters of the cartesian grid the grid
xmin, xmax, ymin, ymax, xrange, yrange, xdim, ydim, delta = setup_grid(cmin, cmax, samples)

# compute total area 
total_area = xrange * yrange

# -----------------------------------------------------------------------------------------------------------------------------------------------
# CONVERGENCE FOR DIFFERENT ITERATION INPUTS
# -----------------------------------------------------------------------------------------------------------------------------------------------


max_iters = np.array([10])
max_iters = np.append(max_iters, np.arange(20,100,10))
# max_iters = np.append(max_iters, np.arange(20,100,10))
max_iters = np.append(max_iters, np.arange(100,1100,100))

rand_samp_areas = []
final_rand_areas = []

lhc_samp_areas = []
final_lhc_areas = []

ortho_samp_areas = []
final_ortho_areas = []

quasi_samp_areas = []
final_quasi_areas = []


for max_iter in max_iters:
    print('', end = '\r')
    print(f"simulating: {int(max_iter/ max_iters[-1]*100)} %", end = '\r')
    
    # random sampling
    rand_samp_complex_vals = random_sampling(xmin, ymin, xrange, yrange, samples)
    rand_samp_areas_mandelbrot = compute_areas(rand_samp_complex_vals, max_iter, total_area)
    final_rand_areas.append(rand_samp_areas_mandelbrot[-1])
    rand_samp_areas.append(rand_samp_areas_mandelbrot)
    
    # latin hypercube samling
    lhc_samp_complex_vals = lhc_sampling(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples)
    lhc_samp_areas_mandelbrot = compute_areas(lhc_samp_complex_vals, max_iter, total_area)
    final_lhc_areas.append(lhc_samp_areas_mandelbrot[-1])
    lhc_samp_areas.append(lhc_samp_areas_mandelbrot)

    # orthogonal sampling 
    ortho_samp_complex_vals = ortho_sampling(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples)
    ortho_samp_areas_mandelbrot = compute_areas(ortho_samp_complex_vals, max_iter, total_area)
    final_ortho_areas.append(ortho_samp_areas_mandelbrot[-1])
    ortho_samp_areas.append(ortho_samp_areas_mandelbrot)
    
    # quasi montecarlo sampling
    quasi_montecarlo_complex_vals = quasi_montecarlo(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples)
    quasi_montecarlo_areas_mandelbrot = compute_areas(quasi_montecarlo_complex_vals, max_iter, total_area)
    final_quasi_areas.append(quasi_montecarlo_areas_mandelbrot[-1])
    quasi_samp_areas.append(quasi_montecarlo_areas_mandelbrot)

with open('data/iterconv_rand.csv', 'w', newline='') as myfile:
    w = csv.writer(myfile)
    for x, y in zip_longest(max_iters, final_rand_areas):
        w.writerow([x, y])

with open('data/iterconv_lhc.csv', 'w', newline='') as myfile:
    w = csv.writer(myfile)
    for x, y in zip_longest(max_iters, final_lhc_areas):
        w.writerow([x, y])

with open('data/iterconv_ortho.csv', 'w', newline='') as myfile:
    w = csv.writer(myfile)
    for x, y in zip_longest(max_iters, final_ortho_areas):
        w.writerow([x, y])

with open('data/iterconv_quasi.csv', 'w', newline='') as myfile:
    w = csv.writer(myfile)
    for x, y in zip_longest(max_iters, final_quasi_areas):
        w.writerow([x, y])

random_x = np.asarray(rand_samp_areas)
lhc_x = np.asarray(lhc_samp_areas)
ortho_x= np.asarray(ortho_samp_areas)
qmc_x = np.asarray(quasi_samp_areas)

np.savetxt("data/itsim_random.csv", random_x, delimiter=",")
np.savetxt("data/itsim_lhc.csv", lhc_x, delimiter=",")
np.savetxt("data/itsim_orthogonal.csv", ortho_x, delimiter=",")
np.savetxt("data/itsim_qmc.csv", qmc_x , delimiter=",")


# -----------------------------------------------------------------------------------------------------------------------------------------------
# Simulations for mean and variance for random sampling on iterative convergence
# -----------------------------------------------------------------------------------------------------------------------------------------------

max_iters = np.array([10])
max_iters = np.append(max_iters, np.arange(20,100,10))
max_iters = np.append(max_iters, np.arange(100,1000,100))
max_iters = np.append(max_iters, np.arange(1000,11000,1000))

total_rand = []

rand_samp_areas_v2 = []
final_rand_areas_v2 = []
for max_iter in max_iters:
    print('', end = '\r')
    print(f"simulating: {int(max_iter/ max_iters[-1] * 100)} %", end = '\r')
    # random sampling
    rand_samp_complex_vals = random_sampling(xmin, ymin, xrange, yrange, samples)
    rand_samp_areas_mandelbrot = compute_areas(rand_samp_complex_vals, max_iter, total_area)
    final_rand_areas_v2.append(rand_samp_areas_mandelbrot[-1])
    rand_samp_areas_v2.append(rand_samp_areas_mandelbrot)


random_x = np.asarray(rand_samp_areas_v2)
np.savetxt("data/total_rand_v01.csv", random_x, delimiter=",")


