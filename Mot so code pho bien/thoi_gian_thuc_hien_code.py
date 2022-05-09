# import thu vien time
import time

# kiem tra thoi gian bat dau
start_time = time.time()

# code can kiem tra
a, b = 1, 2
c = a+b
# kiem tra thoi gian ket thuc
end_time = time.time()

# tinh thoi gian chenh lech
time_taken_in_micro = (end_time - start_time)*(10**6)

# in ket qu
print("Thoi gian thuc thi micro_seconds: {0} ms".format(time_taken_in_micro))
