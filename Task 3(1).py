import pandas as pd
import numpy as np

# Generate date range
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

# Generate random data
values = np.random.randn(len(dates))

# Create a time series DataFrame
df = pd.DataFrame(values, index=dates, columns=['Measurement'])

# Display the first few rows of the DataFrame
print(df.head())
