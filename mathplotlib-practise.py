import matplotlib.pyplot as plt

x= [1,2,3]
y = [2,4,6]

plt.plot(x,y, 'r--')
plt.title("first")

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
temps = [22, 24, 19, 23, 25, 27, 26]

plt.plot(days,temps,marker="o",color="tab:blue" , label="Daily Tempretures")
plt.fill_between(days, 20, 25, color='tab:green', alpha=0.15, label='Comfort Range')
plt.legend()
plt.title("Daily Temperatures (°C) — Week Summary")
plt.xlabel("days")
plt.ylabel("temps")
plt.grid(True)
plt.tight_layout()
plt.show()