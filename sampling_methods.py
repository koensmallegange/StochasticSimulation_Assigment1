'''
Contains functions for the different sampling methods used in the simulations. Methods used:
    - Linear sampling
    - Random sampling
    - Latin hypercube samling 
    - Orthogonal sampling
    - Quasi montecarlo sampling using a Halton sequence
'''

import numpy as np
import itertools 
import math 
import random
from scipy.stats import qmc


def linear_sampling(xmin, ymin, xdim, ydim, delta):
    '''
    return a list of complex samples determined by looping over the grid
    '''
    # store the values 
    complex_values = []
    
    # get the values by looping over the grid 
    for i in range(ydim):
        for j in range(xdim):
            c = complex(xmin + j*delta, ymin + i*delta)
            complex_values.append(c)
            
    return complex_values



def random_sampling(xmin, ymin, xrange, yrange, samples):
    '''
    return a list of complex samples determined in a random fashion
    '''
    # store the values 
    complex_values = []
    
    # generate certain amount of samples 
    for sample in range(samples):
        # generate random complex number 
        real_part = xmin + xrange * np.random.random()
        imaginary_part = ymin + yrange * np.random.random()
        
        # store random sample 
        c = complex(real_part, imaginary_part)
        complex_values.append(c)
        
    return complex_values




def lhc_sampling(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples):
    '''
    return a list of complex samples determined by a latin hypercube algortihm
    '''
    # number of samples
    possible_x_values = np.linspace(xmin, xmax, xdim)
    possible_y_values = np.linspace(ymin, ymax, ydim)
    
    # for each sample point remember in which row and column the sample point was taken
    filled_rows = []
    filled_columns = []
    placed_samples = 0
    complex_values = []
    
    # keep creating samples until desired amount is reached 
    while placed_samples < samples:     
        x = random.choice(possible_x_values)
        y = random.choice(possible_y_values)
        
        # check legality of the sample 
        if x not in filled_rows and y not in filled_columns:
            filled_rows.append(x)
            filled_columns.append(y)

            # remove the sample location from the possible locations 
            possible_x_values = np.delete(possible_x_values, np.where(possible_x_values == x))
            possible_y_values = np.delete(possible_y_values, np.where(possible_y_values == y))

            placed_samples += 1

            c = complex(x, y)
            complex_values.append(c)

    return complex_values




def ortho_sampling(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples):
    '''
    return a list of complex samples by a orthogonal sampling algorithm 
    '''
    # determine the amount of subsquares needed
    subsquares = samples
  
    
    # determine the x and y dimensions of the grid and store them as list for easy acces 
    grid_dim = int(math.sqrt(samples))
    subsq_rows = []
    subsq_cols = []
    
    for i in range(0, grid_dim):
        subsq_rows.append(i)
        subsq_cols.append(i)

    # store all x and y values where samples can be taken 
    possible_x_values = np.linspace(xmin, xmax, samples)
    possible_y_values = np.linspace(ymin, ymax, samples)
    
    # keep track of samples
    check_list = []
    subsquares_filled = []

    # divide possible_x_values into lists corresponding to the subsquares
    for i in range(len(subsq_rows)):
        for j in range(len(subsq_cols)):
            subsq_x = possible_x_values[0+grid_dim*subsq_cols[j]:grid_dim*subsq_cols[j] + grid_dim]
            subsq_y = possible_y_values[0+grid_dim*subsq_rows[i]:grid_dim*subsq_rows[i] + grid_dim]

            s = [subsq_x, subsq_y]

            coordinates = list(itertools.product(*s))
            check_list.append(coordinates)
    
    # keep track of samples
    filled_rows = []
    filled_columns = []
    placed_samples = 0
    complex_values = []
    
    # keep placing samples until desired amount is reached 
    while placed_samples < samples:  
        x = random.choice(possible_x_values)
        y = random.choice(possible_y_values)
        
        # go through all squares and check if sample is legal
        for i in range(subsquares):
        
            # check if the coordinate of the sample point corresponds to a coordinate on the grid 
            if (x, y) in check_list[i]:
                # check if the subsquare is not already filled 
                if i not in subsquares_filled:
                    subsquares_filled.append(i)

                    # check if the location of the point outside the subsquare is not already filled
                    if x not in filled_rows and y not in filled_columns:
                        filled_rows.append(x)
                        filled_columns.append(y)
                    
                        # remove the sample point from the possible points 
                        possible_x_values =  np.delete(possible_x_values, np.where(possible_x_values == x))
                        possible_y_values =  np.delete(possible_y_values, np.where(possible_y_values == y))
                        
                        # place the sample 
                        placed_samples += 1

                        # store the sample 
                        c = complex(x, y)
                        complex_values.append(c)   
    
    return complex_values





def quasi_montecarlo(xmin, ymin, xmax, ymax, xrange, yrange, xdim, ydim, delta, samples):
    '''
    returns a list of complex samples with obtained with a quasi monte carlo simulator 
    '''
    
    complex_values = []
    rand = int(np.random.random(1) * 100)
    sampler = qmc.Halton(d=2, scramble=False, seed=rand)
    sample = sampler.random(n=samples)
    
    l_bounds = [xmin, ymin]
    u_bounds = [xmax, ymax]
    
    sample = qmc.scale(sample, l_bounds, u_bounds)
    
    for i in range(0, len(sample)):
        complex_values.append(complex(sample[i][0], sample[i][1]))
    
    return complex_values



    
    