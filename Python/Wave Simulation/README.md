
# Wave Simulation Script

This Python script simulates wave propagation in a medium over time. It generates data for the wave amplitude and energy, lists amplitude and time values, and plots the amplitude versus time.

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- SciPy

## Installation

Make sure you have Python 3.x installed. You can install the required libraries using pip:

```sh
pip install numpy matplotlib scipy
```

## Usage

1. **Constants and Parameters:**

   The script uses the following constants and parameters:
   - `PLANCK_LENGTH`: Planck length in meters.
   - `PLANCK_TIME`: Planck time in seconds.
   - `L`: Length of the medium in meters.
   - `T`: Total time in seconds.
   - `Nx`: Number of spatial points.
   - `Nt`: Number of time steps.
   - `omega`: Angular frequency.
   - `phase_shift`: Phase shift in radians.

   These parameters can be modified according to your requirements.

2. **Generate Data:**

   The `generate_data` function generates wave amplitude and energy data over time:

   ```python
   A, energy, x, t, total_energy = generate_data(PLANCK_LENGTH, PLANCK_TIME, L, T, Nx, Nt, omega, phase_shift)
   ```

   This function prints the length of the medium, total time, and total energy, and returns:
   - `A`: Array of amplitude values.
   - `energy`: Array of energy values.
   - `x`: Spatial grid.
   - `t`: Temporal grid.
   - `total_energy`: Total energy of the system.

3. **List Amplitude and Time Values:**

   The `list_amplitude_and_time` function creates a list of tuples containing time and amplitude values:

   ```python
   amplitude_time_list = list_amplitude_and_time(A, t)
   ```

   This function returns a list of tuples where each tuple contains the time and the corresponding amplitude value.

4. **Plot Amplitude vs. Time:**

   The `plot_amplitude_time` function plots the amplitude versus time:

   ```python
   plot_amplitude_time(amplitude_time_list)
   ```

   This function generates a plot showing how the amplitude changes over time.

5. **Running the Script:**

   To run the script, simply execute it using Python:

   ```sh
   python wave_simulation.py
   ```

   The script will output the length of the medium, total time, total energy, and the time and corresponding amplitude values. It will also display a plot of amplitude versus time.

## Example Output

The script prints the following information to the console:

```
Length of the medium (L): 1.616255e-35 meters
Total time (T): 750 seconds
Total energy: [Total energy value]
Time and corresponding amplitude values:
Time: [Time value] s, Amplitude: [Amplitude value]
...
```

It also displays a plot showing the amplitude versus time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.