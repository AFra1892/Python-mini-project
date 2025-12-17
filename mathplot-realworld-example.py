import matplotlib.pyplot as plt
import pandas as pd

gas = pd.read_csv("gas_prices.csv")
plt.figure(figsize=(8,5))

plt.title("Gas Prices over Time (in USD)" , fontdict={"fontweight":"bold" , "fontsize":"22"})
plt.plot(gas.Year , gas.Australia , "r.-" , label="Australia")
plt.plot(gas.Year, gas.France , "b.-" , label = "France")
plt.xlabel("Year")
plt.ylabel("Dollar")

plt.xticks(gas.Year[::3])


plt.legend()
plt.show()
