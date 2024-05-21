import numpy as np
import matplotlib.pyplot as plt

def generate_data(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift):
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

    # Update the amplitude and energy over time
    for i in range(1, Nt):
        A[i] = np.cos(omega * t[i] + phase_shift) * np.cos(omega * t[i] + phase_shift)
        energy[i] = 0.5 * np.sum(A[i] ** 2) * dx  # Integrate over the volume

    # Sum all the energy values
    total_energy = np.sum(energy)

    # Output the total energy
    print("Total energy:", total_energy)

    return A, energy, x, t, total_energy

def plot_data(A, energy, x, t, L, Nt):
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

def simulate(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift):
    # Generate data
    A, energy, x, t, total_energy = generate_data(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift)
    plot_data(A, energy, x, t, L, Nt)

    # Loop through A and return the time when amplitude is less than 0.01
    for i in range(Nt):
      for j in range(Nx):
        if np.abs(A[i, j]) < 0.01:
            print(f"Amplitude is less than 0.01 at time {t[i]} seconds and position {x[j]} meters.")
            remaining_time = T - t[i]
            if remaining_time > 0:  # If there is remaining time, call the function recursively
                simulate(PLANCK_LENGTH, PLANCK_TIME, L, remaining_time, Nx, Nt, omega, phase_shift)

# Constants
PLANCK_LENGTH = 1.616255e-35    # meters
PLANCK_TIME = 5.39116e-44       # seconds
L = 1                        # Length of the medium
T = 50                    # Total time
Nx = 100# Number of spatial points
Nt = 500# Number of time steps
omega = np.pi                   # Angular frequency
phase_shift = np.pi / 1 # Example phase shift of pi/4 radians (45 degrees)

# Call the simulate function
simulate(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift)

print(f"End of sim.")
