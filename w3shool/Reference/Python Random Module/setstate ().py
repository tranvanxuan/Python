# khoi phuc trang thai ben trong cua trinh tao so ngau nhien

# nam bat va khoi phuc trang thai cua trinh tao so ngau nhien

import random

# in so ngau nhien
print(random.random())

# chup so
state=random.getstate()

# in mot so ngau nhien ra man hinh
print(random.random())

# khoi phuc lai so
random.setstate(state)

# va so ngau nhien tiep theo giong nhu khi ban bat duoc trang thai
print(random.random())

# cu phap random.setstate (state)
    # can thiet. mot doi tuong state. phuong thuc se tra ve state cua trinh tao so ngau nhien