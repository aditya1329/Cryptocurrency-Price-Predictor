import pandas as pd
df = pd.read_csv('Ethereum Historical Data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df.to_csv('Ethereum_Historical_Data_Updated.csv', index=False)
