# Part 1 and Part 2

input = open("input.txt", "r")
lines = input.readlines()

p1_total = 0
p2_total = 0
for line in lines:
    pairs = line.split(",")
    pair1 = pairs[0]
    pair2 = pairs[1]
    pair1_start = int(pair1[:pair1.find("-")])
    pair1_end = int(pair1[pair1.find("-") + 1:])
    pair2_start = int(pair2[:pair2.find("-")])
    pair2_end = int(pair2[pair2.find("-") + 1:])
    
    if (pair1_start >= pair2_start and pair1_end <= pair2_end) or (pair2_start >= pair1_start and pair2_end <= pair1_end):
        p1_total += 1
    if (pair1_start <= pair2_end and pair1_end >= pair2_start) or (pair2_start <= pair1_end and pair2_end >= pair1_start):
        p2_total += 1

print("Part 1:", p1_total)
print("Part 2:", p2_total)
