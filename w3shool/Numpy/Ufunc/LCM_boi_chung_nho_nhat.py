# boi chung nho nhat

import numpy as np 
num1 = 4
num2 = 6

x=np.lcm(4, 6)
print(x)

# tim boi chung nho nhat trong mot mang

arr = np.arange(1, 11)
y=np.lcm.reduce(arr)
print(y)