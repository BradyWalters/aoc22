def determineOutcome(p, o):
    if (p == "X" and o == "C") or (p == "Y" and o == "A") or (p == "Z" and o == "B"):
        return 6
    elif (p == "X" and o == "B") or (p == "Y" and o == "C") or (p == "Z" and o == "A"):
        return 0
    else:
        return 3

input = open("input.txt", "r")
lines = input.readlines()

scores = {"X": 1, "Y": 2, "Z": 3}
total = 0
for line in lines:
    choices = line.split()
    opponent = choices[0]
    player = choices[1]
    total += (scores[player] + determineOutcome(player, opponent))

print("Part 1:", total)
