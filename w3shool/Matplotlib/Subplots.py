import matplotlib.pyplot as plt
import numpy as np

# plot1
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("SALES")

# plot2
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x, y)
plt.title("INCOME")

# plot 3
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x, y)
plt.title("HOME")
# plot 4
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 4)
plt.plot(x, y)
plt.title("MARKET")
# plot5
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 5)
plt.plot(x, y)
plt.title("SUGAR")
# plot 6
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 6)
plt.plot(x, y)
plt.title("ZZ")

# show
plt.suptitle("MY SHOP")
plt.show()
