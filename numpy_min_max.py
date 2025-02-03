#find the mean, variance and standard deviation of the given array
import numpy as np

n,m=map(int, input().split())

array = np.array([list(map(int,input().split()))for _ in range(n)])
mean_value=np.mean(array, axis=1)
var_value=np.var(array, axis=0)
std_value=np.std(array, axis=None)

print(mean_value)
print(var_value)
if (std_value==0.0):
    print(std_value)
else:
    if(std_value > 0.0):
        print(f"{std_value:.11f}")

