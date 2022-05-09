# lay mot phan tu ra mot mang va tao mot mang moi goi la loc

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
