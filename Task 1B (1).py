import matplotlib.pyplot as plt
import numpy as np
# Generating new data
time = np.linspace(0, 15, 150)
wave1 = np.sin(time)
wave2 = np.cos(time)
# Creating subplots
fig, (plot1, plot2) = plt.subplots(2, 1, figsize=(10, 8))
# Plotting first wave
plot1.plot(time, wave1, label='sin(time)', color='green', linestyle='-')
plot1.set_title('Sine Wave')
plot1.set_xlabel('Time')
plot1.set_ylabel('sin(time)')
plot1.grid(True)
plot1.legend(loc='upper right')
plot1.set_xticks(np.arange(0, 16, 1))
plot1.set_yticks(np.arange(-1, 1.5, 0.5))
plot1.set_xticklabels([f'{i}' for i in range(16)])
plot1.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
plot1.annotate('Max Peak', xy=(np.pi/2, 1), xytext=(np.pi/2+1, 0.8), arrowprops=dict(facecolor='black', shrink=0.05))
# Plotting second wave
plot2.plot(time, wave2, label='cos(time)', color='purple', linestyle='--')
plot2.set_title('Cosine Wave')
plot2.set_xlabel('Time')
plot2.set_ylabel('cos(time)')
plot2.grid(True)
plot2.legend(loc='upper right')
plot2.set_xticks(np.arange(0, 16, 1))
plot2.set_yticks(np.arange(-1, 1.5, 0.5))
plot2.set_xticklabels([f'{i}' for i in range(16)])
plot2.set_yticklabels([f'{i:.1f}' for i in np.arange(-1, 1.5, 0.5)])
plot2.annotate('Min Valley', xy=(np.pi, -1), xytext=(np.pi+1, -0.8), arrowprops=dict(facecolor='black', shrink=0.05))
# Adjusting layout and saving the figure
plt.tight_layout()
plt.savefig('wave_plot_with_annotations.png')
plt.show()
