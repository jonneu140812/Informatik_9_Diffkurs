schule = "Gymnasium Hückelhoven"
schueler = 900
lehrer = 70
klassen = 32

print(f"Am {schule} lernen zur Zeit etwa  {str(schueler)}  SchülerInnen in ca. {str(klassen)} Klassen. Sie werden von ungefähr {str(lehrer)} LehrerInnen unterrichtet.")

print(f"Auf jeden Lehrer kommen also durchschnittlich  {str(int(900/70*100)/100)} SchülerInnen.")

print(f"Die Zahlen:\n 0{str(schueler)} SchuelerInnen\n 00{str(lehrer)} LehrerInnen\n 00{str(klassen)} Klassen")
