import numpy as np
import matplotlib.pyplot as plt

# (a)
x = np.arange(-2, 2, 0.01)
y = 1 / (1 + np.exp(-x))
plt.plot(x, y)
plt.show()

# (b)
x1 = np.arange(8)
y1 = []
file1 = open("tError.txt", "r")
for line in file1:
    y1.append(float(line))
file1.close()

x2 = np.arange(10)
y2 = []
file2 = open("vError.txt", "r")
for line in file2:
    y2.append(float(line))
file2.close()

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlabel('model complexity')
plt.ylabel('error rate')
plt.show()