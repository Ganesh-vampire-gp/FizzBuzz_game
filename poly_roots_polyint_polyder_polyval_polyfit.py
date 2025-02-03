#polyval - This tool evaluates the polynomial at specific value.

import numpy as np

coefficients=list(map(float, input().split()))

x= float(input())

print(np.polyval(coefficients, x))