import random
import time
from rich import print

temperatur: int = 30

while True:
    temperatur = random.randint(0, 140)

    match temperatur:
        case _ if temperatur < 60:
            farbe = "blue"
        case _ if temperatur > 100:
            farbe = "red"
        case _:
            farbe = "green"

    print(f"[{farbe}] {temperatur} [/]")
    time.sleep(0.2)