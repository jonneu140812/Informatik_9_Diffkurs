def main() -> None:
    """
    Aufgaben zu Methoden des Datentyps Liste
    """
    # - Lege eine leere Liste mit dem Namen 'farben' an.
    farben: list[str] = []

    # - Füge die Farben 'Blau', 'Grün', 'Gelb' und 'Rot' (Datentyp String) in die Liste ein.
    farben.extend(["Blau","Grün","Gelb","Rot"])
    print(farben)

    # - Füge 3 Mal den String 'Blau' hinten an die Liste an.
    farben.extend(["Blau","Blau","Blau"])
    print(farben)

    # - Gib aus, wie viele Elemente die Liste hat.
    print(len(farben))

    # - Gib aus, wie oft 'Blau' in der Liste vorkommt.
    print(farben.count("Blau"))

    # - Füge die Farbe 'Grün' ganz vorne in die Liste ein.
    farben.insert(0, "Grün")
    print(farben)

    # - Gib aus, an welchem Index sich die Farbe 'Gelb' befindet und speichere diesen Wert in der
    #   Variable 'idx_gelb'.
    idx_gelb: int = farben.index("Gelb")
    print(idx_gelb)

    # - Füge die Farben 'Blau', 'Grün', 'Lila', 'Grün' und 'Blau' hinter 'Gelb' ein. Benutze die
    #   Variable 'idx_gelb'.
    farben.insert(idx_gelb + 1, "Blau")
    farben.insert(idx_gelb + 1, "Grün")
    farben.insert(idx_gelb + 1, "Lila")
    farben.insert(idx_gelb + 1, "Grün")
    farben.insert(idx_gelb + 1, "Blau")
    print(farben)

    # - Lösche die Farbe 'Gelb' wieder aus der Liste.
    farben.remove("Gelb")
    print(farben)

    # - Gib aus, an welchem Index sich die Farbe 'Rot' befindet und speichere diesen Wert in der
    #   Variable 'idx_rot'.
    idx_rot = farben.index("Rot")
    print(idx_rot)

    # - Ersetze 'Rot' durch 'Lila' (benutze die Variable 'idx_rot').
    farben.pop(idx_rot)
    farben.insert(idx_rot, "Lila")
    print(farben)

    # - Gib aus, an welcher Position sich zum ersten Mal die Farbe 'Grün' befindet.
    print(farben.index("Grün"))

    # - Lösche die zweite Farbe aus der Liste und gib aus, welche Farbe das war.
    print(farben[1])
    farben.pop(1)

    # - Gib aus, welche Farbe jetzt die zweite Farbe in der Liste ist.
    print(farben[1])

    # - Gib aus, welche Farbe als Letztes in der Liste steht.
    print(farben[len(farben) - 1])

    # - Wenn es die Farbe 'Orange' noch nicht in der Liste gibt, dann füge sie ans Ende der Liste ein.

    # - Sortiere die erste Liste.

    # - Lösche alle Elemente aus der Liste.


if __name__ == "__main__":
    main()
