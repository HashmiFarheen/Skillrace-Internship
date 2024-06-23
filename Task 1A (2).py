import pandas as pd
# Updated data and index
data = [100, 200, 300, 400, 500, 600]
index = pd.MultiIndex.from_tuples([('X', 1), ('X', 2), ('Y', 1), ('Y', 2), ('Z', 1), ('Z', 2)])
# Creating a Series with MultiIndex
series = pd.Series(data, index=index)
print("Series with MultiIndex:")
print(series)
# Subsetting the Series for outer index 'X'
subset_X = series.loc['X']
print("\nSubset X:")
print(subset_X)
# Subsetting the Series for index ('X', 2)
subset_X_inner_2 = series.loc[('X', 2)]
print("\nSubset X, Inner 2:")
print(subset_X_inner_2)
# Subsetting the Series for outer index 'Y'
subset_Y = series.loc['Y']
print("\nSubset Y:")
print(subset_Y)
# Subsetting the Series for index ('Z', 1)
subset_Z_inner_1 = series.loc[('Z', 1)]
print("\nSubset Z, Inner 1:")
print(subset_Z_inner_1)
# Using xs() method to subset the Series for outer index 'Y'
subset_Y_xs = series.xs('Y')
print("\nSubset Y using xs:")
print(subset_Y_xs)
# Using xs() method to subset the Series for the inner level 2
subset_inner_2 = series.xs(2, level=1)
print("\nSubset Inner Level 2 using xs:")
print(subset_inner_2)
