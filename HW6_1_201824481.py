import numpy as np

# (a)
a = np.full((6, 4), 2)
print(a)

# (b)
b = np.full((6, 4), 1)
b[0:6, 0:1] = 3
print(b)

# (c)
print(a * b)
# print(np.dot(a, b))
"""
a * b의 경우 단순히 각 위치에 있는 배열의 원소끼리
a[0][0] * b[0][0], a[0][1] * b[0][1], ... 과 같이
곱셈을 하게 되어 a와 b의 크기가 같다면 * 연산이 가능하다.
하지만 dot 연산의 경우 matrix multiplication 으로
이 경우 a와 b의 dot 연산이므로 a의 사이즈가 6X4라면 b의 사이즈는
4Xm이 되어야한다.
"""

# (d)
print(np.dot(a.transpose(), b))
print(np.dot(a, b.transpose()))
"""
dot(a.transpose(), b))의 경우 a를 먼저 transpose 해서
4X6이 되고, (4X6)dot(4X4) 연산을 하므로 4X4의 size 가 된다.
하지만 dot(a, b.transpose())는 b를 먼저 transpose 해서
4X6이 되고, (6X4)dot(4X6) 연산을 하므로 6X6의 size 가 된다.
"""