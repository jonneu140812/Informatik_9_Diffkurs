import random

x = random.randint(1000, 20000)
print(x)

y = random.randint(1, 50)
print(y)

z = random.randint(10, 20)
print(z)

#a
print(x + y + x)

#b
print(x - y)

#c
print(x * y * z)

#d
print(x / y)

#e
print(y ** z)

#f
print(f"{y // x} Rest: {y % x}")

# print(y ** 2 / (x ** 0 - 1))
# diese Rechnung schlagt fehl, weil
# x^0 = 1 ist und minus eins gleich 0.
# folgend wird versucht durch 0 zu teilen,
# dies fürt sie einem fehler ,weil
# durch 0 zu teilen kein ergebnis gibt.
