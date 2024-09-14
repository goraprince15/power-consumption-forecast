import numpy as np
import pandas as pd
import numpy as np

# Load your historical consumption and temperature data
data = pd.read_csv('data.csv')

# Handle missing data
data.fillna(method='ffill', inplace=True)

# Feature Engineering: Add lagged consumption values and time-based features
data['lag1'] = data['consumption'].shift(1)
data['lag2'] = data['consumption'].shift(2)
data['hour'] = pd.to_datetime(data['timestamp']).dt.hour
data['day_of_week'] = pd.to_datetime(data['timestamp']).dt.dayofweek

# Drop rows with missing values after creating lagged features
data.dropna(inplace=True)
