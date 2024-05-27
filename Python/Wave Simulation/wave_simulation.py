import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def generate_data(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift):
    dx = L / Nx                     # Spatial step
    dt = T / Nt                     # Temporal step


    # Output the values of length of medium, total time, and frequency
    print("Length of the medium (L):", L, "meters")
    print("Total time (T):", T, "seconds")

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

    # Update the amplitude and energy over time
    for i in range(1, Nt):
        A[i] = np.cos(omega * t[i] + phase_shift) * np.cos(omega * t[i] + phase_shift)
        energy[i] = 0.5 * np.sum(A[i] ** 2) * dx  # Integrate over the volume

    # Sum all the energy values
    total_energy = np.sum(energy)

    # Output the total energy
    print("Total energy:", total_energy)

    return A, energy, x, t, total_energy

def list_amplitude_and_time(A, t):
    amplitude_time_list = []
    for i in range(len(t)):
        amplitude_time_list.append((t[i], A[i, 0]))
    return amplitude_time_list


def plot_amplitude_time(amplitude_time_list):
    times = [item[0] for item in amplitude_time_list]
    amplitudes = [item[1] for item in amplitude_time_list]
    
    plt.figure(figsize=(10, 6))
    plt.plot(times, amplitudes, color='orange')
    plt.title("Amplitude vs. Time")
    plt.xlabel("Time (t)")
    plt.ylabel("Amplitude (A)")
    plt.grid(True)
    plt.show()

# Constants
PLANCK_LENGTH = 1.616255e-35    # meters
PLANCK_TIME = 5.39116e-44       # seconds
L = PLANCK_LENGTH               # Length of the medium
T = 750                         # Total time
Nx = 100                        # Number of spatial points
Nt = 500                        # Number of time steps
omega = np.pi                   # Angular frequency
phase_shift = np.pi / 1         # Example phase shift of pi/4 radians (45 degrees)

A, energy, x, t, total_energy = generate_data(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift)

amplitude_time_list = list_amplitude_and_time(A, t)

# Output the amplitude and corresponding time values
print("Time and corresponding amplitude values:")
for time, amplitude in amplitude_time_list:
    print(f"Time: {time:.5f} s, Amplitude: {amplitude:.5f}")

plot_amplitude_time(amplitude_time_list)
