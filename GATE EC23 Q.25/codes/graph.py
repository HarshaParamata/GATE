import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Define the transfer function parameters
k = 1
T1 = 2
T2 = 3

# Compute the phase crossover frequency
phase_crossover_freq = 1 / np.sqrt(T1 * T2)

# Define the transfer function numerator and denominator coefficients
numerator = [k*T1*T2, k*(T1+T2), k]
denominator = [0, T1*T2, T1+T2, 0]

# Create a transfer function
sys = signal.TransferFunction(numerator, denominator)

# Frequency response
w, mag, phase = signal.bode(sys)

# Convert phase from degrees to radians
phase_rad = phase * np.pi / 180

# Plot both the magnitude and phase response on a single graph
plt.figure(figsize=(10, 6))

# Magnitude response plot
plt.semilogx(w, mag, color='blue', label='Magnitude Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

# Phase response plot
plt.semilogx(w, phase_rad, color='orange', label='Phase Response')
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (radians)')
plt.grid(True)

# Mark the phase crossover frequency
plt.scatter(phase_crossover_freq, -np.pi, color='red')
plt.text(phase_crossover_freq*1.5, -np.pi*1.5, f'{phase_crossover_freq:.2f} rad/s (Phase Crossover Frequency)', color='red')

plt.title('Frequency Response')
plt.legend()
plt.tight_layout()
plt.show()

