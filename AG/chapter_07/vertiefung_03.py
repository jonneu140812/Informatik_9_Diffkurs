
print(f"Bauer Hampel: Hallo, Kunde was ist dein Name.")
kundenname: str = input(">")
produkte: list[str] = ["Apfel","Birnen","Erdbeeren","Kartoffeln","Eier"]
print(f"Bauer Hampel: Wir haben heute folgende Produkte im Angebot: {produkte}")
print("Welches Produkt willst du kaufen?")
gewProdukt: str = input(">")
if produkte.count(gewProdukt) == 0:
    print(f"Bauer Hampel: Schade, wir haben leider keine {gewProdukt}")
    
else:
    print(f"Bauer Hampel: Bitte schön, hier sind ihre {gewProdukt}")
    match gewProdukt:
        case "Apfel":
            print("Apfel: 2,59 Euro")
        case "Birnen":
            print("Birnen: 2,79 Euro")
        case "Erdbeeren":
            print("Erdbeeren: 4,29 Euro")
        case "Kartoffeln":
            print("Kartoffeln: 5,99 Euro")
        case "Eier":
            print("Eier: 2,29 Euro")
        case _:
            print("")
print(f"Tschuss, bis zum nachsten Mal, {kundenname}!")
