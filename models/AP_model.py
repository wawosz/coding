import numpy as np
import matplotlib.pyplot as plt

# Define constants
C_m = 1.0    # Membrane capacitance (uF/cm^2)
g_Na = 120.0 # Maximum conductances (mS/cm^2)
g_K = 36.0
g_L = 0.3
E_Na = 50.0  # Reversal potentials (mV)
E_K = -77.0
E_L = -54.4

# Time parameters
t_max = 100.0  # Max simulation time (ms)
dt = 0.01     # Time step (ms)
t = np.arange(0, t_max, dt)

# Initialize variables
V = np.zeros_like(t)    # Membrane potential (mV)
m = np.zeros_like(t)    # Sodium activation
h = np.zeros_like(t)    # Sodium inactivation
n = np.zeros_like(t)    # Potassium activation

# Initial conditions
V[0] = -65.0  # Resting potential (mV)
m[0] = 0.05
h[0] = 0.6
n[0] = 0.32

# Functions for ion channel dynamics
def alpha_m(V): return 0.1*(V+40)/(1 - np.exp(-(V+40)/10))
def beta_m(V):  return 4.0*np.exp(-(V+65)/18)
def alpha_h(V): return 0.07*np.exp(-(V+65)/20)
def beta_h(V):  return 1/(1 + np.exp(-(V+35)/10))
def alpha_n(V): return 0.01*(V+55)/(1 - np.exp(-(V+55)/10))
def beta_n(V):  return 0.125*np.exp(-(V+65)/80)

# External stimulus
def I_ext(t):
    return 10 * (t > 5) * (t < 80)  # External current (uA/cm^2)

# Main simulation loop
for i in range(1, len(t)):
    # Update gating variables
    m[i] = m[i-1] + dt * (alpha_m(V[i-1]) * (1 - m[i-1]) - beta_m(V[i-1]) * m[i-1])
    h[i] = h[i-1] + dt * (alpha_h(V[i-1]) * (1 - h[i-1]) - beta_h(V[i-1]) * h[i-1])
    n[i] = n[i-1] + dt * (alpha_n(V[i-1]) * (1 - n[i-1]) - beta_n(V[i-1]) * n[i-1])

    # Calculate ionic currents
    I_Na = g_Na * m[i]**3 * h[i] * (V[i-1] - E_Na)
    I_K = g_K * n[i]**4 * (V[i-1] - E_K)
    I_L = g_L * (V[i-1] - E_L)

    # Update membrane potential
    V[i] = V[i-1] + dt * (I_ext(t[i-1]) - I_Na - I_K - I_L) / C_m

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(t, V, label='Normal Conditions')
plt.title('Action Potential - Normal Conditions')
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.legend()
plt.grid(True)
plt.ylim(-80, 50)
plt.show()