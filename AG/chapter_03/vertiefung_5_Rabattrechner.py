
preis: int = int(input("Preis: "))
rabatt: int = int(input("Rabatt: "))

rabattPreis = preis * rabatt / 100

print(f"Der Rabatt betragt {rabattPreis} Euro")
print(f"Der neue Preis beträgt {preis - rabattPreis} Euro")