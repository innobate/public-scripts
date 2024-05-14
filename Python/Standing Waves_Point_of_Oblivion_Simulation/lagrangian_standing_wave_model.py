import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
L = 100  # Length of the medium
Nx = 100  # Number of spatial points
dx = L / Nx  # Spatial step
x = np.linspace(0, L, Nx)  # Spatial grid

# Define the constants
rho = 1  # Mass density
A = 1  # Cross-sectional area
k = 1  # Stiffness constant

# Define the displacement function
def q(x, t):
    return np.sin(np.pi * x / L) * np.cos(np.pi * t)

# Define the time derivative of the displacement
def dq_dt(x, t):
    return -np.pi * np.sin(np.pi * x / L) * np.sin(np.pi * t)

# Calculate the kinetic energy term
def kinetic_energy(q, dq_dt):
    return 0.5 * np.trapz(rho * A * dq_dt**2, x)

# Calculate the potential energy term
def potential_energy(q):
    return 0.5 * np.trapz(k * q**2, x)

# Calculate the Lagrangian
def lagrangian(q, dq_dt):
    return kinetic_energy(q, dq_dt) - potential_energy(q)

# Time array for visualization
t_values = np.linspace(0, 2, 100)

# Plot the Lagrangian as a function of time
lagrangian_values = [lagrangian(q(x, t), dq_dt(x, t)) for t in t_values]

plt.plot(t_values, lagrangian_values)
plt.xlabel('Time')
plt.ylabel('Lagrangian')
plt.title('Lagrangian of Standing Wave Model')
plt.grid(True)
plt.show()
