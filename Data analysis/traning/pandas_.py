import pandas as pd
import numpy as np


# Create a DataFrame with specific index and columns, initialized with zeros
df = pd.DataFrame(0, index=['X', 'Y', 'Z'], columns=['A', 'B'])
# print dataframe
print(df)
# print row
print(df.loc['X'])
# print column
print(df['A'])  
# print specific value
df.at['X', 'A'] = 5  # Setting a specific value
print(df.at['X', 'A'])  # Accessing a specific value using .at

print(df.info())  # Display DataFrame information