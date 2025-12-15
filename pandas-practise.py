import pandas as pd

df = pd.read_csv('orders.csv')
#print(df)

#print(df.columns)
#print(df.iloc[10]['Shipped'])

#print(df.tail())

#print(df[df['Country'] == "USA" & (df['OrderDate'] == '2024-06-01')] )

filt = (df['Price'] > 100) | (df['Country'] == 'UAE') 
print(df[filt])