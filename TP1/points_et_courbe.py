import numpy as np
import matplotlib.pyplot as plt

# Constants
tau = 0.1  # 100 ms
frequency = 50  # 50 Hz
timestep = 0.005  # 5 ms
num_points = 1000

# Time array
t = np.linspace(0, timestep * num_points, num_points)

# Function definition
def damped_sinusoid(t):
    return np.exp(-t / tau) * np.cos(2 * np.pi * frequency * t)

# Calculate function values
y = damped_sinusoid(t)

# Plotting
plt.plot(t, y)
plt.title("Damped Sinusoid")
plt.xlabel("Time (s)")
plt.ylabel("f(t)")
plt.grid(True)
plt.show()