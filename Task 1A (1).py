import pandas as pd
import numpy as np

# Updated data
data = {
    'W': [10, 20, np.nan, 40, 50, np.nan, 70],
    'X': [np.nan, 20, 30, 40, np.nan, 60, 70],
    'Y': ['apple', 'banana', 'cherry', np.nan, 'date', 'elderberry', 'fig'],
    'Z': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Checking for missing data
missing_data = df.isna()
print("\nMissing Data in DataFrame:")
print(missing_data)

# Dropping rows with any missing data
df_dropna_rows = df.dropna()
print("\nDataFrame after dropping rows with any missing data:")
print(df_dropna_rows)

# Dropping columns with any missing data
df_dropna_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with any missing data:")
print(df_dropna_cols)

# Filling missing data with specified values
df_fillna = df.fillna(value={'W': df['W'].mean(), 'X': df['X'].mean(), 'Y': 'missing', 'Z': 0})
print("\nDataFrame after filling missing data:")
print(df_fillna)

# Adding a duplicate row
df_with_duplicates = df.append(df.iloc[2], ignore_index=True)
print("\nDataFrame with Duplicates:")
print(df_with_duplicates)

# Checking for duplicates
duplicates = df_with_duplicates.duplicated()
print("\nDuplicates in DataFrame:")
print(duplicates)

# Removing duplicates
df_no_duplicates = df_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)
