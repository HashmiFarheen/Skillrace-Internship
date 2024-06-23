import pandas as pd

# Using Start date and End date
start_date_1 = '2024-01-01'
end_date_1 = '2024-12-31'
date_index_1 = pd.date_range(start=start_date_1, end=end_date_1)
print(date_index_1)

# Using Start date and Periods
start_date_2 = '2024-01-01'
periods = 365  # for a full year
date_index_2 = pd.date_range(start=start_date_2, periods=periods)
print(date_index_2)

# Using End date and Periods
end_date_3 = '2024-12-31'
periods = 365  # for a full year
date_index_3 = pd.date_range(end=end_date_3, periods=periods)
print(date_index_3)

# Using Frequency
start_date_4 = '2024-01-01'
end_date_4 = '2024-12-31'
date_index_4 = pd.date_range(start=start_date_4, end=end_date_4, freq='D')

# 'D' Generates dates on daily basis
print(date_index_4)
