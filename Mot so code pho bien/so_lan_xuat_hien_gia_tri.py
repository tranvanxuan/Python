# tim so lan xuat hien cua moi phan tu trong LIst
#import Counter

from collections import Counter

my_list = ['a', 'a', 'b', 'b', 'b', 'c', 'd', 'd', 'd', 'd', 'd']

count = Counter(my_list)  # xac dinh doi tuong counter

print(count)  # in thong tin tat ca
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

print(count['b'])
# in so lan xuat hien cua phan tu b

print(count.most_common(1))
# phan tu xuat hien nhieu nhat
