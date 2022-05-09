# phuong thuc extend () them danh sach chi dinh (hay bat ki vong lap nao) vao cuoi danh sach hien tai

fruits = ['apple', 'banana', 'cherry']

cars=['Ford', 'BMW', 'Volvo']

# them danh sach cars vao cuoi danh sach fruits
fruits.extend(cars)
print(fruits)

# cu phap list.extend (iterable)
    # iterable : list, set, tuple, etc

fruits=['apple', 'banana', 'cherry']
points= (1, 4, 5, 9)

fruits.extend(points)
print(fruits)