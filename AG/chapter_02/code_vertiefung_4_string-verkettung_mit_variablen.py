x: int = 10
y: int = 5
z: int = 15

print(str(z) + " = " + str(x) + " + " + str(y))
# wird es nicht konvertiert kommet ein Typerror,
# weil man integer und string nicht addieren kann

print(f"{z} = {x} + {y}")



