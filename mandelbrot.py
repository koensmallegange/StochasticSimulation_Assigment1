'''
plots the mandlebrot set given a certain amount of samples and iterations
'''


import matplotlib.pyplot as plt
from functions import set_colors, setup_grid


# set parameters of the complex grid
cmin = -2-1.3j
cmax = 0.6+1.3j

# set the parameters of the simulation
samples = 40 ** 2
max_iter = 100

# set parameters of the cartesian grid the grid
xmin, xmax, ymin, ymax, xrange, yrange, xdim, ydim, delta = setup_grid(cmin, cmax, samples)

# plot mandelbrot
color_array = set_colors(cmin,cmax, max_iter, samples)
plt.figure(figsize=(8,8))
plt.imshow(color_array, zorder=1, interpolation='none')


