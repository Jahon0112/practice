'''
(1)Define and Call
(2)Parametr and Argument
(3)Keyword & default arguments
(4)Scope

'''

print("===Define and Call===")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in JAVA, Python uses indetation!

# DEFINE -build (parametr)


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executd")
    return f"HI {b}"

# CALL -execute (argument)


result1 = greet('Jakhongir')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)

print("====Keyword & default arguments====")
# DEFINE


def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# CALL
result3 = give_greet(name="Jastin", age=20)
print("result3:", result3)

result4 = give_greet("John",)
print("result4:", result4)
