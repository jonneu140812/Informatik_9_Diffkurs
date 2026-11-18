
spielzeug = ["Ball", "Puppe", "Auto", "Puzzle", "Buch", "Teddy", "Lego", "Karten"]

print(spielzeug)

rm: str = input("Welches willst du verkaufen? > ")

if spielzeug.count(rm) != 0:
    spielzeug.remove(rm)
    print(spielzeug)
else:
    print(f"Das Spielzeug {rm} ist leider nicht in der kiste.")

