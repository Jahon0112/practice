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

# DEFINE -build


def greet(a):
    print(f"How do you do, {a}")


def greeting(b):
    print("greeting is executd")
    return f"HI {b}"

# CALL -execute


result1 = greet('Jakhongir')
print("result1:", result1)

result2 = greeting("Justin")
print("result2:", result2)
