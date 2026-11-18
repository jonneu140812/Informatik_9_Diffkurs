
print(f"Bauer Hampel: Hallo, Kunde was ist dein Name.")

kundenname: str = input(">")

produkte: list[str] = ["Apfel", "Birnen", "Erdbeeren", "Kartoffeln", "Eier"]
mengen: list[int] = [4, 1, 6, 10, 0]
preise: list[float] = [2.59, 2.79, 4.29, 5.99, 2.29]

print(f"Bauer Hampel: Wir haben heute folgende Produkte im Angebot: {produkte}")

print("Welches Produkt willst du kaufen?")
gewProdukt: str = input(">")

print("Wie viele?")
countGewProdukt: int = int(input(">"))

if produkte.count(gewProdukt) == 0:
    print(f"Bauer Hampel: Schade, wir haben leider keine {gewProdukt}")

elif countGewProdukt > mengen[produkte.index(gewProdukt)]:
    print(f"Bauer Hampel: Wir haben leider nur {mengen[produkte.index(gewProdukt)]} {gewProdukt}. Soll ich die fehlenden {countGewProdukt - mengen[produkte.index(gewProdukt)]} für morgen bestellen?")
    print("Ja oder Nein?")
    input(">")
    
else:
    print(f"Bauer Hampel: Bitte schön, hier sind ihre {gewProdukt}")
    
    print(f"Das kostet {preise[produkte.index(gewProdukt)] * countGewProdukt} Euro ")

print(f"Tschuss, bis zum nachsten Mal, {kundenname}!")
