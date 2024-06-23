import pandas as pd

# Generate date range with UTC timezone
start_date_first = '2024-01-01'
end_date_first = '2024-01-05'
date_index_first = pd.date_range(start=start_date_first, end=end_date_first, freq='D', tz='UTC')
print(date_index_first)

# Localize timezone to America/New_York
date_index_second = pd.date_range(start=start_date_first, end=end_date_first, freq='D')
date_index_second = date_index_second.tz_localize('America/New_York')
print(date_index_second)

# Convert timezone to Europe/London
date_index_third = date_index_second.tz_convert('Europe/London')
print(date_index_third)

# Combine date ranges from different timezones
date_index_fourth = pd.date_range(start=start_date_first, periods=3, freq='D', tz='UTC')
date_index_fifth = pd.date_range(start=start_date_first, periods=3, freq='D', tz='America/New_York')
combined_index = date_index_fourth.union(date_index_fifth)
print(combined_index)
