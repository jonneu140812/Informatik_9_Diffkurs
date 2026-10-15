"""
Bedingte Anweisungen mit if, elif und else.
"""

zahl: int = int(input("Bitte eine Zahl eingeben: "))
msg: str = ""

if zahl > 0:
    msg = "Die Zahl ist größer 0!"
elif zahl < 0:
    msg = "Die Zahl ist kleiner 0!"
else:
    msg = "Treffer!"

print(msg)