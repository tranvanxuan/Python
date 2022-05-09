import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherries", "Dates"]

plt.pie(y, labels=mylabels)
plt.legend(title="Four Fruits:")
plt.show()
