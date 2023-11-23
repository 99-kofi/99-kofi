import numpy as np
import matplotlib.pyplot as plt

# Number of stars (adjust as needed)
n = 1000

# Constants for the spiral
a = 0.5
b = 0.6

# Generate random angles (theta)
th = np.random.randn(n)

# Convert to Cartesian coordinates
x = a * np.exp(b * th) * np.cos(th)
y = a * np.exp(b * th) * np.sin(th)

# Plot the stars
plt.scatter(x, y, s=1, color='white')
plt.title("Logarithmic Spiral Galaxy")
plt.axis('off')  # Hide axes
plt.show()
