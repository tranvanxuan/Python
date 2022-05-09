from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6]), hist=False)
plt.show()
