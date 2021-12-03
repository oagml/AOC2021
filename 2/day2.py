#Day 2

originalInput = open("puzzleInput").read().split('\n')

originalInput.pop() #Remove the last blank character

#print(originalInput)

#Create tuples that contain direction and value:
puzzleInput = []
for i in originalInput:
    puzzleInput.append(i.split(' '))

#Since both parts are strings, convert the second element of the list to integers:
for i in puzzleInput:
    i[1] = int(i[1]) #Convert second element to integer


#print(puzzleInput)

#Initialize position:
horizontal = 0
depth = 0

for inst in puzzleInput:

    if inst[0] == "forward":
        horizontal += inst[1]
    elif inst[0] == "down":
        depth += inst[1]
    elif inst[0] == "up":
        depth -= inst[1]
    else:
        print("Error: Unknown instruction")


print(f"Depth: {depth}")
print(f"Horizontal {horizontal}")

print(f"Product of both {depth * horizontal}")

#Part 2 -----------------------------------------------------------------------------------

aim = 0

horizontal = 0
depth = 0

for inst in puzzleInput:

    if inst[0] == "forward":
        horizontal += inst[1]
        depth += (aim * inst[1])
    elif inst[0] == "down":
        aim += inst[1]
    elif inst[0] == "up":
        aim -= inst[1]
    else:
        print("Error: Unknown instruction")

print("Part 2 of the puzzle")
print(f"Depth: {depth}")
print(f"Horizontal {horizontal}")

print(f"Product of both {depth * horizontal}")
