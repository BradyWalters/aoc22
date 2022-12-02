input = open("input.txt", "r")
input_lines = input.readlines()

elf_cals = []
curr_cals = 0
for line in input_lines:
    if line == "\n":
        elf_cals.append(curr_cals)
        curr_cals = 0
    else: 
        curr_cals += int(line)

elf_cals.sort()
print("Part 1:", elf_cals[len(elf_cals) - 1])
print("Part 2:", elf_cals[len(elf_cals) - 1] + elf_cals[len(elf_cals) - 2] + elf_cals[len(elf_cals) - 3])
