import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


# Constants
PLANCK_LENGTH = 1.616255e-35    # meters
PLANCK_TIME = 5.39116e-44       # seconds
L = PLANCK_LENGTH               # Length of the medium
T = 1250                        # Total time
Nx = 100                        # Number of spatial points
Nt = 500                        # Number of time steps
omega = np.pi                   # Angular frequency
dx = L / Nx                     # Spatial step
dt = T / Nt                     # Temporal step

# Calculate frequency from angular frequency
frequency = omega / (2 * np.pi)

# Output the values of length of medium, total time, and frequency
print("Length of the medium (L):", L, "meters")
print("Total time (T):", T, "seconds")
print("Frequency (f):", frequency, "Hz")

# Spatial and temporal grids
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)

# Initialize the amplitude A(t)
A = np.zeros((Nt, Nx))

# Initialize the energy array
energy = np.zeros(Nt)

# Define the initial conditions
A[0] = np.cos(omega * t[0]) * np.cos(omega * t[0])

# Calculate energy for the initial condition
energy[0] = 0.5 * np.sum(A[0] ** 2) * dx  # Sum of squared values integrated over the volume

# Define a phase shift
phase_shift = np.pi / 1  # Example phase shift of pi/4 radians (45 degrees)

# Update the amplitude and energy over time
for i in range(1, Nt):
    A[i] = np.cos(omega * t[i] + phase_shift) * np.cos(omega * t[i] + phase_shift)
    energy[i] = 0.5 * np.sum(A[i] ** 2) * dx  # Integrate over the volume

# Sum all the energy values
total_energy = np.sum(energy)

# Output the total energy
print("Total energy:", total_energy)

# Plotting
plt.figure(figsize=(12, 8))

# Plot the amplitude
plt.subplot(2, 1, 1)
plt.title("Amplitude of the Standing Wave over Time")
plt.xlabel("Position (x)")
plt.ylabel("Amplitude (A)")
plt.ylim(-1.1, 1.1)
plt.grid(True)

# Plot the standing wave at various time steps
for i in range(Nt):
    if i % (Nt // 10) == 0:  # Plot only every tenth time step
        plt.plot(x, A[i], label=f"t = {t[i]:.2f}")

# Highlight the point of oblivion
plt.plot([L/2], [0], marker='o', markersize=8, color="red", label="Point of Oblivion")
plt.legend()

# Plot the energy
plt.subplot(2, 1, 2)
plt.title("Energy of the Standing Wave over Time")
plt.xlabel("Time (t)")
plt.ylabel("Energy")
plt.grid(True)

# Plot the energy over time
plt.plot(t, energy, color='green')
plt.ylim(0, max(energy) * 1.1)

plt.tight_layout()
plt.show()

# Initialize a list to store time points where amplitude is zero
zero_amplitude_times = []

# Check each time step for zero amplitude
for i in range(Nt):
    if np.abs(np.cos(omega * t[i] + phase_shift)) < 0.01 :  # Check if amplitude is close to zero
        zero_amplitude_times.append(t[i])

# Output time points where amplitude is zero
print("Time points where amplitude is zero:", zero_amplitude_times)

# Define a tolerance level for amplitude to be considered 1
amplitude_tolerance = 1

# Initialize a list to store time points where amplitude is close to 1
amplitude_1_times = []

# Check each time step for amplitude close to 1
for i in range(Nt):
    if np.abs(np.cos(omega * t[i] + phase_shift)) == 1.0:  # Check if amplitude is close to zero
        amplitude_1_times.append(t[i])

# Output time points where amplitude is close to 1
print("Time points where amplitude is 1:", amplitude_1_times)


# Find peaks and valleys
peaks, _ = find_peaks(A[:, 0], height=0)
valleys, _ = find_peaks(-A[:, 0], height=0)

# Initialize a list to store energy generated each cycle
energy_generated_each_cycle = []

# Calculate energy generated each cycle
for i in range(len(peaks) - 1):
    energy_generated_each_cycle.append(np.abs(energy[peaks[i + 1]] - energy[peaks[i]]))

for i in range(len(valleys) - 1):
    energy_generated_each_cycle.append(np.abs(energy[valleys[i + 1]] - energy[valleys[i]]))

# Output energy generated each cycle
print("Energy generated each cycle:", energy_generated_each_cycle)


