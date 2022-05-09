from scipy import io

import numpy as np

mydata=io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])