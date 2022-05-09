name = "Jeremy"
age = 25

# String formatting using concatenation
print("My name is " + name + ", am I am " + str(age))

# String formatting using multiple prints
print("My name is ", end="")
print(name, end="")
print(", and I am ", end="")
print(age, end="")
print("years old.")

# String formatting using join
print(''.join(["My name is ", name, ", am I am ", str(age), " years old"]))

# String formatting using modulus operator
print("My name is %s, and I amd %d years old." % (name, age))

# function with ordered parameters
print("My name is {}, and I am {} years old".format(name, age))

# fuction with name parameters
print("My name is {n}, and I amd {a} years old.".format(a=age, n=name))

# using f-Strings
print(f"My name is {name}, and I am {age} years old")
