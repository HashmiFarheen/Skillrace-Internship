import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
values = np.random.normal(loc=0, scale=1, size=1000)

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(values, bins=30, edgecolor='black', alpha=0.7)
plt.xlabel('Data Points')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.grid(True)
plt.show()

# Create a density plot
plt.figure(figsize=(10, 6))
sns.kdeplot(values, fill=True)
plt.xlabel('Data Points')
plt.ylabel('Density')
plt.title('Density Plot of Random Data')
plt.grid(True)
plt.show()
