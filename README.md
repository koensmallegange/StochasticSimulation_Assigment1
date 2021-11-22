# Code for assignment 1, stochastical simulation 

The code used in this research is split up in different scripts. In this file an overview of these scripts can be found. 

### README.md
contains overview of all scripts and additional information

### sampling_methods.py
Contains functions for all sampling methods. Sampling methods used in this research are random sampling, latin hypercube sampling , orthogonal sampling and quasi-montecarlo sampling. These function take the dimensions of the grid in which they should sample and the amount of samples they should take. They return a list of samples, which are complex values.

### functions.py
Contains all the helper functions that are used in this research. 

### mandelbrot.py
Visualizes the mandelbrot set for a given amount of samples and iterations.

### simulate_samples.py
Executes a given amount of simulations in which the area of the mandelbrot set is determined by the four different sampling methods for a fixed amount of iterations and different amount of samples. Data is stored in txt files. 

### simulate_iterations.py
Executes a given amount of simulations in which the area of the mandelbrot set is determined by the four different sampling methods for a fixed amount of samples and different amount of iterations. Data is stored in txt files.

### process_sample_simulation.py
Processes and plots the data obtained from the sample simulations. 


### process_iteration_simulation.py
Processes and plots the data obtained from the iterations simulations.

### data folder
Contains the txt files from the simulations

### data_backup folder
Contains a copy of datasets obtained by large simulations. In case that the data in the datafolder gets overwritten by accidental simulations. 


