
spielzeug = ["Ball", "Puppe", "Auto", "Puzzel", "Buch", "Teddy", "Lego", "Karten"]
output: list[str] = []

start: int
end: int
inc: int 
reverse: str # [n]ormal, [r]everse

def Slice(start, end, inc, reverse):
    for i in range(start, end, inc):
        output.append(spielzeug[i])

    match reverse:
        case "r": 
            output.reverse()
        case _:
            pass
    return output

print(Slice(0, 3, 1, "n"))
