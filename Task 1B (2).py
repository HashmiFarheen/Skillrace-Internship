import matplotlib.pyplot as plt
import numpy as np
# Generate data for plotting
t = np.linspace(0, 25, 250)
signal1 = np.sin(t / 3)
signal2 = np.cos(t / 3)
# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
# Plot the first signal (sin(t/3))
ax1.plot(t, signal1, label='sin(t/3)', color='orange', linestyle='-')
ax1.set_title('Sine Function (t/3)')
ax1.set_xlabel('Time')
ax1.set_ylabel('sin(t/3)')
ax1.grid(True)
ax1.legend(loc='upper right')
ax1.set_xticks(np.arange(0, 26, 2))
ax1.set_yticks(np.arange(-1, 1.5, 0.5))
ax1.set_xticklabels([f'{i}' for i in range(0, 26, 2)])
ax1.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
# Annotate a peak in the sine wave
ax1.annotate('Maximum', xy=(np.pi*1.5, 1), xytext=(np.pi*1.5 + 3, 0.8), arrowprops=dict(facecolor='black', shrink=0.05))

# Plot the second signal (cos(t/3))
ax2.plot(t, signal2, label='cos(t/3)', color='green', linestyle='--')
ax2.set_title('Cosine Function (t/3)')
ax2.set_xlabel('Time')
ax2.set_ylabel('cos(t/3)')
ax2.grid(True)
ax2.legend(loc='upper right')
ax2.set_xticks(np.arange(0, 26, 2))
ax2.set_yticks(np.arange(-1, 1.5, 0.5))
ax2.set_xticklabels([f'{i}' for i in range(0, 26, 2)])
ax2.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
# Annotate a valley in the cosine wave
ax2.annotate('Minimum', xy=(np.pi*3, -1), xytext=(np.pi*3 + 3, -0.8),   arrowprops=dict(facecolor='black', shrink=0.05))
# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('trig_wave_plot.png')
plt.show()
