import numpy as np

# (a)
X = np.array([[1, 2104, 5, 1, 45, 460], [1, 1416, 3, 2, 40, 232],
              [1, 1544, 3, 2, 30, 315], [1, 852, 2, 1, 36, 178]])
assert np.shape(X) == (4, 6)

# (b)
P = X[0:4, 1:5]
assert np.shape(P) == (4, 4)

# (c)
print(np.average(X[0:4, 0]), np.average(X[0:4, 1]), np.average(X[0:4, 2]),
      np.average(X[0:4, 3]), np.average(X[0:4, 4]), np.average(X[0:4, 5]))