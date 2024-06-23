import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(0)

# Generate random data
data_dict = {
    'Group': np.random.choice(['X', 'Y', 'Z', 'W', 'V'], 100),
    'Measure': np.random.randn(100)
}

# Create DataFrame
df_data = pd.DataFrame(data_dict)

# Create a box plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Measure', data=df_data)
plt.xlabel('Group')
plt.ylabel('Measure')
plt.title('Box Plot of Measure by Group')
plt.grid(True)
plt.show()
