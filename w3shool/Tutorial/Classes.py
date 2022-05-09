class Person():
    """docstring for Person"""
    def __init__(mysillyobject, name, age):
        super(Person, mysillyobject).__init__()
        mysillyobject.mysillyobject = mysillyobject
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Jonh", 36)
p1.myfunc()
