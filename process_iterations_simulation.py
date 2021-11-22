'''
Processes data from the iteration simulation. Shows data as a plot. 
'''

from numpy import genfromtxt
import matplotlib.pyplot as plt
import numpy as np

# random = genfromtxt('data_backup/sample_sim/itsim_random.csv', delimiter=',')
# lhc = genfromtxt('data_backup/sample_sim/itsim_lhc.csv', delimiter = ',')
# ortho = genfromtxt('data_backup/sample_sim/itsim_orthogonal.csv', delimiter = ',')
# qmc = genfromtxt('data_backup/sample_sim/itsim_qmc.csv', delimiter = ',')

# figure style 
plt.rcParams.update({'font.size': 14})
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['figure.dpi']= 500

random = genfromtxt('data_backup/sample_sim/total_rand_v01.csv', delimiter=',')

max_iters = np.array([10])
max_iters = np.append(max_iters, np.arange(20,100,10))
max_iters = np.append(max_iters, np.arange(100,1000,100))
max_iters = np.append(max_iters, np.arange(1000,11000,1000))

# for i in range(0, len(random)):
fig, axs = plt.subplots(1, 1, figsize=(14, 12))
for i in range(3, len(random), 4):
    axs.plot(random[i][100:], linewidth=0.5, label=f'{max_iters[i]} iters')
    
axs.set_title('Area convergence for different iterations for 10,000 samples using random sampling')
axs.set_xlabel('Samples')
axs.set_ylabel('Area')
plt.legend(loc='upper right')
plt.grid()

for spine in ('top', 'right', 'bottom', 'left'):
    axs.spines[spine].set_visible(False)
plt.show()

max_iters,final_rand_areas = np.loadtxt("data_backup/sample_sim/iterconv_rand.csv", delimiter=",", unpack=True)
max_iters,final_lhc_areas = np.loadtxt("data_backup/sample_sim/iterconv_lhc.csv", delimiter=",", unpack=True)
max_iters,final_ortho_areas = np.loadtxt("data_backup/sample_sim/iterconv_ortho.csv", delimiter=",", unpack=True)
max_iters,final_quasi_areas = np.loadtxt("data_backup/sample_sim/iterconv_quasi.csv", delimiter=",", unpack=True)

# plot the data 
fig, axs = plt.subplots(1, 1, figsize=(14, 12))
 
axs.plot(max_iters, final_rand_areas, label = 'Random sampling')
axs.plot(max_iters, final_lhc_areas, label = 'LHC sampling')
axs.plot(max_iters, final_ortho_areas, label = 'Orthogonal sampling')
axs.plot(max_iters, final_quasi_areas, label = 'Quasi Monte Carlo sampling')

axs.set_title('Area estimates for different iterations after 1225 samples')
axs.set_xlabel('Iterations')
axs.set_ylabel('Area')

for spine in ('top', 'right', 'bottom', 'left'):
    axs.spines[spine].set_visible(False)
    
plt.legend(loc='upper right')
plt.grid()
plt.show()


