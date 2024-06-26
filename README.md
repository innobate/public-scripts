# public-scripts
Contains scripts for experiments, research etc.

## Schrödinger equation
The Schrödinger equation is fundamental in quantum mechanics and can be used to describe the energy distribution of quantum systems. The equation provides a way to calculate the wave function of a particle, which contains all the information about the system, including the probability distribution of its energy.

Here's a basic outline of how the Schrödinger equation can be used to show energy distribution:

### Time-Independent Schrödinger Equation
For a particle in a potential \(V(x)\), the time-independent Schrödinger equation is given by:

\[
-\frac{\hbar^2}{2m} \frac{d^2 \psi(x)}{dx^2} + V(x) \psi(x) = E \psi(x)
\]

where:
- \(\psi(x)\) is the wave function,
- \(E\) is the energy of the particle,
- \(\hbar\) is the reduced Planck constant,
- \(m\) is the mass of the particle,
- \(V(x)\) is the potential energy.

### Solving the Schrödinger Equation
1. **Define the Potential**: Choose the potential \(V(x)\) for the system. Common examples include the infinite potential well, harmonic oscillator, and the finite potential well.
2. **Solve for Wave Functions and Energies**: Solve the Schrödinger equation to find the wave functions \(\psi_n(x)\) and corresponding energy levels \(E_n\).
3. **Energy Distribution**: The energy levels \(E_n\) represent the quantized energy states that the particle can occupy. The square of the wave function \(|\psi_n(x)|^2\) gives the probability density of finding the particle at position \(x\).

### Example: Infinite Potential Well
Consider a particle in a one-dimensional infinite potential well (also known as a particle in a box) of width \(L\):

### Visualization
Let's implement this in Python to visualize the wave functions and the corresponding energy levels.
```python
import numpy as np
import matplotlib.pyplot as plt

def infinite_potential_well(L, n_max, num_points=1000):
    x = np.linspace(0, L, num_points)
    wave_functions = []
    energies = []
    
    for n in range(1, n_max + 1):
        psi_n = np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
        E_n = (n**2 * np.pi**2 * (6.62607015e-34)**2) / (2 * 9.10938356e-31 * L**2)
        wave_functions.append(psi_n)
        energies.append(E_n)
    
    return x, wave_functions, energies

# Parameters
L = 1e-10  # 1 angstrom
n_max = 5  # First 5 energy levels

x, wave_functions, energies = infinite_potential_well(L, n_max)

# Plot wave functions and energy levels
plt.figure(figsize=(12, 8))

for n in range(n_max):
    plt.plot(x, wave_functions[n] + energies[n], label=f"n={n+1}")

plt.title("Wave Functions and Energy Levels in an Infinite Potential Well")
plt.xlabel("Position (x)")
plt.ylabel("Energy")
plt.legend()
plt.grid(True)
plt.show()

# Output the energy levels
for n, E in enumerate(energies):
    print(f"Energy level n={n+1}: {E} Joules")
```
### Explanation
- **Defining the Potential Well**: We define the potential well with width \( L \).
- **Calculating Wave Functions and Energies**: We use the analytical solutions for the infinite potential well to calculate the wave functions and energy levels.
- **Visualization**: We plot the wave functions shifted by their corresponding energy levels for clarity. The energy levels are displayed as horizontal lines in the plot.
This example illustrates the concept of energy quantization in a quantum system. The Schrödinger equation can be solved for various potentials to understand the energy distribution and wave functions of different quantum systems.


## Calculate energy of wave from its intensity
To calculate the energy of a standing wave using the rate of change of intensity (\( \frac{dI}{dt} \)), we need to understand the relationship between intensity and the physical quantities involved in the standing wave.

### Intensity and Energy Relationship

For a wave, intensity \( I \) is related to the energy per unit area per unit time. The energy density (energy per unit volume) of the wave can be expressed in terms of the square of the displacement velocity \( \left( \frac{\partial u}{\partial t} \right) \).

The formula for intensity \( I \) is:
\[ I = \frac{1}{2} \rho \left( \frac{\partial u}{\partial t} \right)^2 v \]
where:
- \( \rho \) is the density of the medium,
- \( v \) is the speed of the wave,
- \( \frac{\partial u}{\partial t} \) is the displacement velocity.

For a standing wave, the energy is contained within the oscillations of the wave and does not propagate. However, we can relate the intensity to the energy density as follows:
\[ I = \frac{dE}{dA \cdot dt} \]

### Energy Calculation using Rate of Change of Intensity

Given the intensity \( I \), the energy \( E \) over a length \( L \) can be calculated by integrating the intensity over the time and spatial dimensions.

1. **Expression for Energy Density**:
   \[
   E_{\text{density}} = \frac{1}{2} \rho \left( \frac{\partial u}{\partial t} \right)^2
   \]

2. **Rate of Change of Intensity**:
   The rate of change of intensity \( \frac{dI}{dt} \) can be expressed as:
   \[
   \frac{dI}{dt} = \frac{d}{dt} \left( \frac{1}{2} \rho \left( \frac{\partial u}{\partial t} \right)^2 v \right)
   \]
   Since the speed \( v \) is constant for a given medium and wave type, we get:
   \[
   \frac{dI}{dt} = \frac{1}{2} \rho v \cdot \frac{d}{dt} \left( \left( \frac{\partial u}{\partial t} \right)^2 \right)
   \]

3. **Calculating the Energy \( E \)**:
   To find the total energy, integrate the energy density over the length \( L \) of the medium:
   \[
   E = \int_0^L \frac{1}{2} \rho \left( \frac{\partial u}{\partial t} \right)^2 dx
   \]

4. **Connecting to Intensity**:
   Since intensity \( I \) relates to the energy flow per unit area, the total energy in the standing wave can also be interpreted through the integrated intensity:
   \[
   E = \int_0^T \int_0^L I \, dx \, dt
   \]

5. **Using the Rate of Change of Intensity**:
   If we know the rate of change of intensity \( \frac{dI}{dt} \), we can integrate this over time to find the change in intensity, and thus the energy:
   \[
   I(t) = \int \frac{dI}{dt} \, dt
   \]
   And the energy over the length \( L \):
   \[
   E = \int_0^L I(t) \, dx
   \]

### Detailed Steps and Equations

1. **Calculate the Rate of Change of Intensity**:
   \[
   \frac{dI}{dt} = \frac{1}{2} \rho v \cdot 2 \left( \frac{\partial u}{\partial t} \right) \left( \frac{\partial^2 u}{\partial t^2} \right)
   \]
   Simplify to:
   \[
   \frac{dI}{dt} = \rho v \left( \frac{\partial u}{\partial t} \right) \left( \frac{\partial^2 u}{\partial t^2} \right)
   \]

2. **Integrate to Find Intensity**:
   \[
   I(t) = \int \rho v \left( \frac{\partial u}{\partial t} \right) \left( \frac{\partial^2 u}{\partial t^2} \right) \, dt
   \]

3. **Calculate the Energy**:
   \[
   E = \int_0^L I(t) \, dx = \int_0^L \int_0^T \rho v \left( \frac{\partial u}{\partial t} \right) \left( \frac{\partial^2 u}{\partial t^2} \right) \, dt \, dx
   \]

This approach integrates the rate of change of intensity over time to get the intensity and then integrates this intensity over the spatial domain to obtain the total energy of the standing wave. This provides a detailed method to link the rate of change of intensity to the energy in the standing wave.
