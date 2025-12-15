import matplotlib.pyplot as plt
import numpy as np

# Example data
np.random.seed(0)
x = np.random.rand(50) * 10        # 50 values between 0 and 10
y = x * 1.5 + (np.random.randn(50) * 3)  # some linear-ish relationship with noise
sizes = (np.random.rand(50) * 200) + 20  # point sizes
colors = np.random.rand(50)            # color scale

plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.75, edgecolor='k')
plt.colorbar(label='Color scale (random)')
plt.xlabel('X variable')
plt.ylabel('Y variable')
plt.title('Example Scatter Plot')
plt.grid(True)
plt.tight_layout()
plt.show()