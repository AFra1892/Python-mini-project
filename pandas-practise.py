import pandas as pd

df = pd.read_csv('orders.csv')
#print(df)

print(df.columns)
print(df.iloc[10]['Shipped'])