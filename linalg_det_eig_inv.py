# find the determinant of a matrix

import numpy as np

n=int(input("enter"))
A=np.array([list(map(float, input().split()))for _ in range(n)])
print(np.linalg.det(A))



