# Dunder  "double under score",__builtins(system variable), _init(Python negiz)
message = "PATHON: Everything is object!"
print(message)

result = type(message)
print("result:", result)

'''In Python, there are builtin tools:
(1)TYPES > int float str list dict
(2) FUNCTION > pront() len() input() type()
(3)CONSTANTS > True False None

'''

print(dir(__builtins__))
