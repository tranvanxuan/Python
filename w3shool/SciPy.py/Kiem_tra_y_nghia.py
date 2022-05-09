import numpy as np
from scipy.stats import normaltest

v = np.random.normal(size=100)

print(normaltest(v))
