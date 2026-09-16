'''
Objects
(1) What is object
(2)Iterable objects & Range
(3)Dictionary
(4)Error handling system
'''

import array  # package/module
import math  # package
from math import ceil
print("==== What is object====")
# An object has state and method properties
# Everything is object in python!

print(type('Hello world!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigms > functional programming(chiziqli programming) & OOP (object oriented progeamming)
# OOP 4 concepts > Abstraction | Encapsulation | Inheritence | Polimorpism
result1 = math.ceil(97.7)  # CALL
print("result1:", result1)

result2 = ceil(98.7)
print("result2:", result2)
