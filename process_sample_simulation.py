'''
Processes data from the sample simulation. Shows data as a plot. 
'''
from numpy import genfromtxt
import matplotlib.pyplot as plt
from functions import mean, std


# ----------------------------------------------------------------------------------------------------------------------------
# READ DATA OF SIM
# ----------------------------------------------------------------------------------------------------------------------------

random = genfromtxt('data_backup/sample_sim/samplesim_random.csv', delimiter=',')
lhc = genfromtxt('data_backup/sample_sim/samplesim_lhc.csv', delimiter = ',')
ortho = genfromtxt('data_backup/sample_sim/samplesim_orthogonal.csv', delimiter = ',')
qmc = genfromtxt('data_backup/sample_sim/samplesim_qmc.csv', delimiter = ',')


# ----------------------------------------------------------------------------------------------------------------------------
# COMPUTE MEAN AND STD OF DATA
# ----------------------------------------------------------------------------------------------------------------------------

random_mean = mean(random)
random_std = std(random)

lhc_mean = mean(lhc)
lhc_std = std(lhc)

ortho_mean = mean(ortho)
ortho_std = std(ortho)

qmc_mean = mean(qmc)
qmc_std = std(qmc)

sims = len(random)
samples = (len(random[0]))

# ----------------------------------------------------------------------------------------------------------------------------
# PLOT DATA
# ----------------------------------------------------------------------------------------------------------------------------


# figure style 
plt.rcParams.update({'font.size': 14})
plt.rcParams['mathtext.fontset'] = 'stix'
plt.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams['figure.dpi']= 500

fig, axs = plt.subplots(3, 1, figsize=(14, 12))
fig.tight_layout(pad = 5)
fig.suptitle(f"Area of {sims} simulations of the Mandelbrot set with {samples} samples and 100 iterations")

axs[0].plot(random_mean[0:200], label = 'Random sampling', lw = .5)
axs[0].plot(lhc_mean[0:200], label = 'LHC sampling', lw = .5)
axs[0].plot(ortho_mean[0:200], label = 'Orthogonal sampling', lw = .5)
axs[0].set_title(f"Mean of area over first 200 samples of {sims} simulations per sampling technique")
axs[0].legend()
axs[0].set_xlabel('Samples')
axs[0].set_ylabel('Area')
axs[0].grid()

for spine in ('top', 'right', 'bottom', 'left'):
    axs[0].spines[spine].set_visible(False)

axs[1].plot(random_mean, label = 'Random sampling', lw = .5)
axs[1].plot(lhc_mean, label = 'LHC sampling', lw = .5)
axs[1].plot(ortho_mean, label = 'Orthogonal sampling', lw = .5)
axs[1].set_title(f"Mean of area over {sims} simulations per sampling technique")
axs[1].legend()
axs[1].set_xlabel('Samples')
axs[1].set_ylabel('Area')
axs[1].grid()

for spine in ('top', 'right', 'bottom', 'left'):
    axs[1].spines[spine].set_visible(False)

axs[2].plot(random_std[20:1200], label = 'Random sampling', lw = .5)
axs[2].plot(lhc_std[20:1200], label = 'LHC sampling', lw = .5)
axs[2].plot(ortho_std[20:1200], label = 'Orthogonal sampling', lw=.5)
axs[2].set_title(f"Standard deviation of {sims} simulations per sampling technique")
axs[2].legend()
axs[2].set_xlabel('Samples')
axs[2].set_ylabel('Area')
axs[2].grid()

for spine in ('top', 'right', 'bottom', 'left'):
    axs[2].spines[spine].set_visible(False)


plt.show()

print(random_mean[-1])
print(lhc_mean[-1])
print(ortho_mean[-1])
print(qmc_mean[-1])

# fig, axs = plt.subplots(2, 1, figsize=(14, 12))
# fig.tight_layout(pad = 5)
# fig.suptitle(f"Area of {sims} simulations of the Mandelbrot set with {samples} samples and 100 iterations")

# axs[0].plot(random_mean[0:200], label = 'Random sampling', lw = .5)
# axs[0].plot(lhc_mean[0:200], label = 'LHC sampling', lw = .5)
# axs[0].plot(ortho_mean[0:200], label = 'Orthogonal sampling', lw = .5)
# axs[0].plot(qmc_mean[0:200], label = 'Quasi-Monte Carlo sampling', lw = 1)
# axs[0].set_title(f"Mean of area over first 200 samples of {sims} simulations per sampling technique")
# axs[0].legend()
# axs[0].set_xlabel('Samples')
# axs[0].set_ylabel('Area')
# axs[0].grid()

# for spine in ('top', 'right', 'bottom', 'left'):
#     axs[0].spines[spine].set_visible(False)

# axs[1].plot(random_mean, label = 'Random sampling', lw = .5)
# axs[1].plot(lhc_mean, label = 'LHC sampling', lw = .5)
# axs[1].plot(ortho_mean, label = 'orthogonal sampling', lw = .5)
# axs[1].plot(qmc_mean, label = 'Quasi-Monte Carlo sampling', lw = 1)
# axs[1].set_title(f"Mean of area over {sims} simulations per sampling technique")
# axs[1].legend()
# axs[1].set_xlabel('Samples')
# axs[1].set_ylabel('Area')
# axs[1].grid()

# for spine in ('top', 'right', 'bottom', 'left'):
#     axs[1].spines[spine].set_visible(False)


# plt.show()

        
    
# fig, axs = plt.subplots(2, 1, figsize=(14, 12))
# fig.tight_layout(pad = 5)
# fig.suptitle("Area of Mandelbrot set with a fixed amount of iterations")

# axs[0].plot(random_mean, lw = .5)
# axs[0].set_title(f"Mean of area over {sims} simulations")
# axs[0].legend()
# axs[0].set_xlabel('Samples')
# axs[0].set_ylabel('Area')
# axs[0].grid()

# for spine in ('top', 'right', 'bottom', 'left'):
#     axs[0].spines[spine].set_visible(False)

# axs[1].plot(random_std, lw = .5)
# axs[1].set_title(f"Standard deviation of mean area of {sims} simulations")
# axs[1].legend()
# axs[1].set_xlabel('Samples')
# axs[1].set_ylabel('Area')
# axs[1].grid()

# for spine in ('top', 'right', 'bottom', 'left'):
#     axs[1].spines[spine].set_visible(False)


# plt.show()



# fig, axs = plt.subplots(2, 1, figsize=(14, 12))
# fig.tight_layout(pad = 5)
# fig.suptitle("Area of Mandelbrot set with a fixed amount of iterations using quasi-montecarlo sampling")

# axs[0].plot(qmc_mean[0:200], lw = .5)
# axs[0].set_title(f"Mean of area over first 200 samples of {sims} simulations with qasi-montecarlo sampling")
# axs[0].legend()
# axs[0].set_xlabel('Samples')
# axs[0].set_ylabel('Area')
# axs[0].grid()

# for spine in ('top', 'right', 'bottom', 'left'):
#     axs[0].spines[spine].set_visible(False)

# axs[1].plot(qmc_mean, lw = .5)
# axs[1].set_title(f"Mean of area over {sims} simulations with quasi-montecarlo sampling")
# axs[1].legend()
# axs[1].set_xlabel('Samples')
# axs[1].set_ylabel('Area')
# axs[1].grid()


# for spine in ('top', 'right', 'bottom', 'left'):
#     axs[1].spines[spine].set_visible(False)


# plt.show()
    


