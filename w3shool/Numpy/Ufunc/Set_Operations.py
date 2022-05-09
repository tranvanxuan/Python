import numpy as np

# arr=np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
# x=np.unique(arr) # ham unique tim cac phan tu duy nhat trong mot mang
# print(x)

# tim cac gia tri duy nhat trong 2 mang
# dung phuong thuc union1d()

# arr1=np.array([1, 2, 3, 4])
# arr2=np.array([3, 4, 5, 6])
# newarr=np.union1d(arr1, arr2)
# print(newarr)

# tim giao cua 2 tap hop dung phuong thuc intersect1d
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])
# newarr = np.intersect1d(arr1, arr2, assume_unique=True)
# print(newarr)
# tim gia tri trong tap dau tien khong co trong tap thu 2 
# dung ham setdiff1d
# doi so assume_unique giup tang toc do tinh toan
# no phai luo dat la true khi tinh toan vs tap hop
# arr1 = np.array([1, 2, 3, 4])
# arr2 = np.array([3, 4, 5, 6])
# newarr = np.setdiff1d(arr1, arr2, assume_unique=True)
# print(newarr)

# tim cac gia tri khong co trong ca 2 tap hop
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)
