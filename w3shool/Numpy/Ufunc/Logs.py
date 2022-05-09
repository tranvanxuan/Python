import numpy as np 
from math import log 

nplog=np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
print(nplog(9, 3))