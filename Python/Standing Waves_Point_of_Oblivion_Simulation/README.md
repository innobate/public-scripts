## standing_wave_simulation
The provided script implements a simulation of a standing wave phenomenon. Here's a breakdown of its components:

Constants Definition: Constants such as Planck's length, Planck's time, length of the medium (L), total time (T), number of spatial points (Nx), number of time steps (Nt), angular frequency (omega), spatial step (dx), and temporal step (dt) are defined.

Frequency Calculation: The frequency (frequency) is calculated from the angular frequency.

Output of Constants: The values of the length of the medium, total time, and frequency are printed.

Spatial and Temporal Grids: Arrays for spatial (x) and temporal (t) grids are generated using NumPy's linspace function.

Amplitude Initialization: An array A is initialized to store the amplitude of the wave at each spatial point and time step.

Energy Initialization: An array energy is initialized to store the energy of the wave at each time step.

Initial Conditions: The initial conditions for the amplitude are set using a cosine function.

Phase Shift: A phase shift (phase_shift) is defined.

Amplitude and Energy Update: The amplitude and energy are updated over time. The amplitude undergoes a phase shift in each time step.

Total Energy Calculation: The total energy of the wave is calculated by summing the energy at each time step.

Plotting: The script generates two subplots: one for the amplitude of the standing wave over time and another for the energy of the standing wave over time.

Finding Points of Zero Amplitude: Time points where the amplitude is close to zero are identified.

Finding Points of Amplitude Close to 1: Time points where the amplitude is close to 1 are identified.

Finding Peaks and Valleys: Using SciPy's find_peaks function, peaks and valleys of the standing wave are identified.

Energy Generated Each Cycle: The difference in energy between consecutive peaks and valleys is calculated, representing the energy generated each cycle.

This script can be used to analyze the dynamics of standing waves, including the concept of points of oblivion and their role in energy generation and storage. The energy generated each cycle, calculated based on the difference in energy between consecutive peaks and valleys, provides insight into how energy accumulates and releases within the system.

## standing_wave_simulation_point_of_oblivion_probability
This script models a standing wave phenomenon over time and space, analyzing its amplitude and energy characteristics. Here's a summary of its key elements and sections:

Constants and Parameters: The script begins by defining various constants and parameters such as the Planck length, total time (T), length of the medium (L), number of spatial points (Nx), number of time steps (Nt), and angular frequency (omega).

Initializations: It initializes arrays to store the amplitude (A) and energy (energy) of the standing wave at different time steps.

Initial Conditions: The initial condition of the standing wave is set with a cosine function.

Phase Shift: A phase shift is introduced to demonstrate the effect of changing the phase of the wave.

Amplitude and Energy Calculation: The amplitude and energy of the standing wave are updated over time using a loop. The amplitude is calculated based on the phase-shifted cosine function, while the energy is calculated by summing the squared values of the amplitude integrated over the volume.

Total Energy Calculation: The total energy of the system is calculated by summing all the energy values.

Plotting: The script generates two subplots: one for the amplitude of the standing wave over time and another for the energy of the standing wave over time. The amplitude subplot shows the standing wave at various time steps, highlighting the point of oblivion. The energy subplot displays how the energy of the standing wave evolves over time.

Probability Calculation: It calculates the probabilities of the amplitude being 0, 1, or neither 0 nor 1 at each time step. The probabilities are calculated based on the number of occurrences where the amplitude falls within specified ranges.

Output Probabilities: Finally, the script outputs the probabilities of the amplitude being 0, 1, or neither 0 nor 1.

This script provides a comprehensive analysis of a standing wave model, including its amplitude and energy characteristics over time, as well as the probabilities associated with different states of the amplitude.

![standing_wave_simulation_point_of_oblivion_probability](Screenshot%202024-05-15%20011100.png)

## lagrangian_standing_wave_model
This script simulates a standing wave model and analyzes its Lagrangian as a function of time. Here's a breakdown of each key element:

1. **Parameters Definition**:
   - `L`: Length of the medium.
   - `Nx`: Number of spatial points.
   - `dx`: Spatial step calculated as the ratio of the length of the medium to the number of spatial points.
   - `x`: Spatial grid created using `np.linspace()`.

2. **Constants**:
   - `rho`: Mass density.
   - `A`: Cross-sectional area.
   - `k`: Stiffness constant.

3. **Displacement Function**:
   - `q(x, t)`: Defines the displacement function as a sinusoidal wave along the spatial dimension `x` and time `t`.

4. **Time Derivative of Displacement**:
   - `dq_dt(x, t)`: Defines the time derivative of displacement, necessary for calculating kinetic energy.

5. **Kinetic Energy Calculation**:
   - `kinetic_energy(q, dq_dt)`: Calculates the kinetic energy term of the Lagrangian using the trapezoidal rule to integrate the kinetic energy density over the spatial grid.

6. **Potential Energy Calculation**:
   - `potential_energy(q)`: Calculates the potential energy term of the Lagrangian using the trapezoidal rule to integrate the potential energy density over the spatial grid.

7. **Lagrangian Calculation**:
   - `lagrangian(q, dq_dt)`: Calculates the Lagrangian as the difference between kinetic and potential energies.

8. **Time Array for Visualization**:
   - `t_values`: Array of time values for visualization.

9. **Plotting**:
   - `lagrangian_values`: Computes the Lagrangian for each time value in `t_values`.
   - Plots the Lagrangian as a function of time using `plt.plot()`.



In Lagrangian mechanics, the Lagrangian 𝐿 is typically defined as the difference between the kinetic energy (𝑇) and the potential energy (𝑉) of the system.

For a standing wave system, we can represent the motion of each particle (or point) in the medium using a generalized coordinate. Let's denote the displacement of each point from its equilibrium position as 𝑞(𝑥,𝑡), where 𝑥 is the spatial coordinate and 𝑡 is time.

The kinetic energy term depends on the rate of change of displacement with time, i.e., the velocity (𝑞˙). The potential energy term depends on the displacement itself.

Given these considerations, the Lagrangian for your standing wave model can be expressed as:

𝐿 = 𝑇 - 𝑉

Where:

𝑇 = 1/2 ∫ 0 𝐿 𝜌 𝐴 (∂𝑞/∂𝑡)² dx

is the kinetic energy, and

𝑉 = 1/2 ∫ 0 𝐿 𝑘 𝑞² dx

is the potential energy. Here, 𝜌 is the mass density of the medium, 𝐴 is the cross-sectional area, 𝑘 is the stiffness constant, and 𝐿 is the length of the medium.




