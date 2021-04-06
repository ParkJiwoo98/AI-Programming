import numpy as np
# (b)
def findOne(arr):
    count = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if arr[i][j] == 1:
                count += 1
    return count

# (a)
a = np.ones(16)
a = a.reshape(4, 4)
b = np.eye(4, 4)
c = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

sum_ = a + b
sub = a - c
print(np.average(sum_))

# (b)
d = np.random.randint(0, 5, size=(5, 5))
print(d)
print(findOne(d))
print(np.where(d == 1, 'O', 'X'))