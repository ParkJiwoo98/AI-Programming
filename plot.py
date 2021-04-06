import numpy as np
import matplotlib.pyplot as plt

file1 = open('FirstChoiceTSP100.txt', 'r')
file2 = open('SimulatedAnnealingTSP100.txt', 'r')

y1 = []
numLine = 0
for line in file1:
    numLine += 1
    y1.append(float(line))
file1.close()
x1 = np.arange(numLine)

y2 = []
numLine = 0
for line in file2:
    numLine += 1
    y2.append(float(line))
file2.close()
x2 = np.arange(numLine)

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.xlabel('Number of Evaluations')
plt.ylabel('Tour Cost')
plt.title('Search Performance (TSP-100)')

plt.legend(['First-Choice HC', 'Simulated Annealing'])
plt.show()