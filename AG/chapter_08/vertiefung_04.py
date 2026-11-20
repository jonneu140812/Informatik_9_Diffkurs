
import random

totalGuess: list[int] = []
validGuesses: int = 0
correctNumbers: list[int] = []
for _ in range(5):
    correctNumbers.append(random.randint(1, 49))
correctGuess: int = 0

while True:
    while validGuesses != 5:
        guess: int = int(input("Guess 1-49\n> "))
        match guess:
            case n if n > 49:
                print("please guess within the correct range")
            case n if n < 1:
                print("please guess within the correct range")
            case n if n in totalGuess:
                print("please no repeated numbers")
            case _:
                totalGuess.append(guess)
                validGuesses += 1
    for i in range(0, 5):
        if totalGuess[i] in correctNumbers:
            correctGuess += 1
    print(f"you got {correctGuess} correct.\ncorrect numbers {correctNumbers}.\nyour numbers {totalGuess}.")
    print("continue?")
    match input("yes or no?\n> "):
        case "yes":
            totalGuess: list[int] = []
            validGuesses: int = 0
            correctNumbers: list[int] = []
            for _ in range(5):
                correctNumbers.append(random.randint(1, 49))
            correctGuess: int = 0
        case _:
            quit()
