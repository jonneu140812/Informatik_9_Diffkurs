
wort: str = input("> ")
x: int = 0 
rev: str = ""


print(len(wort))

while len(wort) > x:
    rev = (wort[x]) + rev
    x += 1

print(rev)
