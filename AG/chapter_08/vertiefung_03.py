
import random

top: int = int(input(f"top\n> "))
bottom: int = int(input(f"bottom\n> "))
num: int = random.randint(bottom, top)
tries: int = 0

while True:
    while tries < 5:
        guess: int = int(input("Guess\n> "))
        match guess:
            case n if n < num:
                print(f"the number is bigger than {guess}")
                tries += 1 
            case n if n > num:
                print(f"the number is smaller than {guess}")
                tries += 1 
            case _:
                print(f"you guessed right!\nthe number was {num}.\nyou took {tries} tries.")
                print("continue?")
                match input("yes or no?\n> "):
                    case "yes":
                        top: int = int(input(f"top\n> "))
                        bottom: int = int(input(f"bottom\n> "))
                        num: int = random.randint(bottom, top)
                        tries: int = 0
                    case _:
                        quit()


    print("you have guessed 5 times.")
    print("continue?")
    match input("yes or no?\n> "):
        case "yes":
            top: int = int(input(f"top\n> "))
            bottom: int = int(input(f"bottom\n> "))
            num: int = random.randint(bottom, top)
            tries: int = 0
        case _:
            quit()

# einer der besten wege ist es immer in der mitte zu raten und so die moeglich keiten zu halbieren
