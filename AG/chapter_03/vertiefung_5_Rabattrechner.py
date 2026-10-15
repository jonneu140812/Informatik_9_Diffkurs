
preis: float = float(input("Preis: "))
rabatt: float = float(input("Rabatt: "))

rabattPreis: float = preis * rabatt / 100

print(f"Der Rabatt betragt {rabattPreis:.2f} Euro")
print(f"Der neue Preis beträgt {preis - rabattPreis:.2f} Euro")