import numpy as np

# Reshape co nghia la thay doi hinh dang cua mot mang
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
nearr = arr.reshape(4, 3)  # thay doi 4 mang , moi mang co 3 phan tu
print(nearr)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

newarr1 = arr1.reshape(-1)

print(newarr1)
