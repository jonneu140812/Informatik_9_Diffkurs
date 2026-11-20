import random 

x: int = -20

while x != 21:
    print(x)
    x += 1 

print("//1")

y: int = 100

while y != -1:
    print(y)
    y -= 1 

print("//2")

z: int = 7

while z < 100:
    print(z)
    z += 7 

print("//3")

a: int = 2

while a < 1000:
    print(a, a ** 2)
    a += 1 

print("//4")

b: int = 0

while b != 7:
    print(b)
    b = random.randint(1, 10) 

print("//5")

c: str = ""
d: list[str] = []

while c != "exit":
    c = input("> ")
    d.append(c)

d.remove("exit")

print(d)

print("//6")

e: int = 0
f: int = 1

while e != f:
    e = random.randint(1, 6)
    f = random.randint(1, 6) 
    print(e, f)

print("//7")

g: int = 0
h: int = 0

while g != 6:
    g += 1
    while h != 6:
        h += 1
        print(g, h)
    h = 0
