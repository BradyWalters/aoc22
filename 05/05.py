# Part 1 and Part 2

input = open("input.txt", "r")
lines = input.readlines()

stacks1 = [[]]
stacks2 = [[]]
for line in lines:
    if line[0] == " " or line[0] == "[":
        spaces = 4
        stack_num = 0
        for c in line:
            if c == " ":
                spaces -= 1
                if spaces == 0:
                    if len(stacks1) == stack_num:
                        stacks1.append([])
                        stacks2.append([])
                    stack_num += 1
                    spaces = 4
            elif c == "]":
                spaces = 5
            elif c.isalpha():
                if len(stacks1) == stack_num:
                    stacks1.append([])
                    stacks2.append([])
                stacks1[stack_num].append(c)
                stacks2[stack_num].append(c)
                stack_num += 1
    elif line.startswith("move"):
        line = line.split()
        num_crates = int(line[1])
        from_stack = int(line[3])
        to_stack = int(line[5])
        
        for i in range(num_crates):
            stacks1[to_stack - 1].insert(0, stacks1[from_stack - 1].pop(0))
            stacks2[to_stack - 1].insert(i, stacks2[from_stack - 1].pop(0))
        
print("Part 1:", end=" ")
for stack in stacks1:
    print(stack[0], end="")
print()
print("Part 2:", end=" ")
for stack in stacks2:
    print(stack[0], end="")
