import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
# tra ve (2,4) nghia la mang co 2 chieu va 4 phan tu

arr1 = np.array([1, 2, 3, 4], ndmin=5) # tao mang co 5 thu nguyen

print(arr1)
print('shape of array :', arr1.shape)

# shape la so phan tu trong 1 chieu
# shape cho biet dieu gi? vi du tren thu nguyen thu 5 co 4 phan tu