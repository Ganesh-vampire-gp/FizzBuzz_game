# Full path: /matrix_product_2arrays.py
# A program that computes the product of two matrices.
# A matrix is a two-dimensional array of numbers. For example, the following is a 2x3 matrix:
# 1 2 3
# 4 5 6
# The product of two matrices A and B is a matrix C such that C[i][j] is the dot product of the ith row of A and the jth column of B.
# Write a program that reads two matrices A and B from the user, and then computes and prints their product.
# The input consists of three parts:
# The number of rows of the first matrix n (1 <= n <= 100).
# The elements of the first matrix A, which is a n x n matrix.
# The elements of the second matrix B, which is a n x n matrix.
# The output is the product of the two matrices A and B.
import numpy as np
n=int(input())
A= np.array([list(map(int,input().split()))for _ in range(n)])
B= np.array([list(map(int,input().split()))for _ in range(n)])

print(np.dot(A, B))
