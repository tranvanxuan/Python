# ham super () tra ve mot doi tuong dai dien cho lop cha
# tao lop Parent
class Parent:
    # tat ca cac lop co mot ham goi la __init__() luon duoc thuc thi khi lop dang bat dau
    # su dung de gan gia chi cho thuoc tinh doi tuong hoac cac hoat dong khac
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)
# tao lop Child ke thua tat ca cac thuoc tinh va phuong thuc lop Parent
class Child(Parent):
  def __init__(self, txt):
      # tra ve doi tuong dai dien cho lop cha
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

