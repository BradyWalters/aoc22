# I KNOW THIS IS TERRIBLE I GOT REAL LAZY FOR PART TWO
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
p1_total = 0
p2_total = 0
for line in lines:
    choices = line.split()
    col1 = choices[0]
    col2 = choices[1]
    p1_total += (scores[col2] + determineOutcome(col2, col1))

    player = ""
    opp = ord(col1) - ord("A")
    if col2 == "X":
        player = 2 if opp == 0 else opp - 1
    elif col2 == "Z":
        player = 0 if opp == 2 else opp + 1
    else:
        player = opp
    p_choice = list(scores)[player]
    p2_total += (scores[p_choice] + determineOutcome(list(scores)[player], col1))

print("Part 1:", p1_total)
print("Part 2:", p2_total)
