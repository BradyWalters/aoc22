# Part 1

input = open("input.txt", "r")
lines = input.readlines()

lower_start = ord("a")
upper_start = ord("A")
total = 0
for line in lines: 
    half = int(len(line) / 2)
    com1 = line[:half]
    com2 = line[half:]

    for c in com1:
        if com2.find(c) != -1:
            if c.isupper():
                total += (ord(c) - upper_start + 27)
            else:
                total += (ord(c) - lower_start + 1)
            break

print("Part 1:", total)

# Part 2
input = open("test_input.txt", "r")
lines = input.readlines()

for i in range(int(len(lines) / 3)):
    for j in range(3):
        print(lines[(i * 3) + j])
