#Package to install to run this script
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Function for the rate of change of intensity
def rate_of_change_intensity(t, A):
    omega = 1  # You can adjust the angular frequency as needed
    return 2 * A * np.gradient(A) * np.cos(omega * t)**2 - A**2 * omega * np.sin(2 * omega * t)

# Time values
t_values = np.linspace(0, 10, 500)

# Amplitude function, you can modify this based on your requirement
A_values = np.exp(0.2 * t_values)

# Calculate the rate of change of intensity
dI_dt_values = rate_of_change_intensity(t_values, A_values)

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t_values, A_values, label='Amplitude ($A(t)$)')
plt.title('Amplitude vs Time')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_values, dI_dt_values, label='Rate of Change of Intensity ($\\frac{dI}{dt}$)')
plt.title('Rate of Change of Intensity vs Time')
plt.xlabel('Time')
plt.ylabel('Rate of Change of Intensity')
plt.legend()

plt.tight_layout()
plt.show()
