# phai lam gi neu xay ra ngoai le

# neu cong lenh tra ve ngoai le in ra "Something went wrong"

try:
    x>3
except:
    print("Something went wrong")

print("-------------------------------------------")

x="hello"
try:
    x>3

    # viet thong bao neu ten loi
except NameError:
    print("You have a variable tha is not definded.")

    # viet thong bao neu typeerror
except TypeError:
    print("You are comparing values of different type")


print("----------------------------------------")

# co gang thuc thi cau lenh gay ra loi, nhung trong truong hop nay khong co loai loi nao duoc xac dinh
try:
    x=1/0
except NameError:
    print("You have a variable that is not definded.")
except TypeError:
    print("You are comparing values of different type")
except:
    print("Something else went wrong")