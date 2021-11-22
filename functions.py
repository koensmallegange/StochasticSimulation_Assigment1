'''
Contains helper functions for all the mandelbrot scripts
'''

import numpy as np
import colorsys



def mandelbrot(c, max_iter = 100):
    '''
    Contains the mandelbrot function, returns amount of iterations need to blow up.
    '''
    z = c + 0.0j
    n = 0
    
    while(z.real * z.real + z.imag * z.imag <= 4 and n < max_iter):
        z = z*z + c
        n = n + 1
        
    return n




def setup_grid(cmin, cmax, samples):
    '''
    Sets up the grid on which the mandelbrot will be created. Grid is in Cartesian coordinates.
    '''
    resolution = samples 

    # determine x values in cartesian coordinates 
    xs = [cmin.real, cmax.real]
    xs.sort()
    xmin,xmax = xs
    
    # determine y values in cartesian coordinates 
    ys = [cmin.imag, cmax.imag]
    ys.sort()
    ymin,ymax = ys

    # get range
    xrange = xmax-xmin
    yrange = ymax-ymin
    
    if xrange >= yrange:
        xdim = int(resolution)
        ydim = int(xdim*(yrange/xrange))
        delta = xrange/xdim
        
    else:
        ydim = int(resolution)
        xdim = int(ydim*(xrange/yrange))
        delta = yrange/resolution

    return xmin, xmax, ymin, ymax, xrange, yrange, xdim, ydim, delta





def set_colors(cmin, cmax, max_iter, samples):
    '''
    Computes the color values needed to vizualise the mandelbrot set.
    '''
    xmin, xmax, ymin, ymax, xrange, yrange, xdim, ydim, delta = setup_grid(cmin, cmax, samples)

    # 3D array to make a picture of the fractal
    color_array = np.zeros((ydim,xdim,3))

    for i in range(ydim):
        for j in range(xdim):
            c = complex(xmin + j*delta, ymin + i*delta)
            iter_of_c = mandelbrot(c, max_iter)

            # set hue and saturation
            hue = int(255 * iter_of_c / max_iter) / 255
            saturation = 255 / 255

            # determine value
            if iter_of_c < max_iter:
                value = 255 / 255
            else:
                value = 0

            # convert HSV to RGB and add to 3D array
            color_array[i,j] = colorsys.hsv_to_rgb(hue, saturation, value) 

    return color_array



def compute_areas(complex_values, max_iter, total_area):
    '''
    Computes the area of the mandelbrot set given a list with points in the complex plane
    '''
    total = 0
    unescaped = 0
    areas_mandelbrot = []

    for i in range(len(complex_values)):
        iter_of_c = mandelbrot(complex_values[i], max_iter)
        total += 1
        if iter_of_c == max_iter:
            unescaped += 1
        ratio = unescaped / total
        area_mandelbrot = total_area * ratio
        areas_mandelbrot.append(area_mandelbrot)
    
    return areas_mandelbrot



def mean(data):
    '''
    extract the mean of all sims per point in time
    '''
    
    sims = len(data)
    samples = (len(data[0]))
    
    mean = []
    for i in range (samples):
        points = []
        
        for j in range(sims):
            x_value = data[j][i]
            points.append(x_value)
        
        mean.append(np.mean(points))
    
    return mean


def std(data):
    '''
    extract the variance of all sims per point in time
    '''
    sims = len(data)
    samples = (len(data[0]))
    
    std = []
    for i in range (samples):
        points = []
        
        for j in range(sims):
            x_value = data[j][i]
            points.append(x_value)
        
        std.append(np.std(points))
    
    return std