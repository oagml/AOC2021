#Day 1
#Part 1 -------------------------------------------------------------------

inputList = open("puzzleinput",mode='r', newline='\r\n').read().split('\n')
puzzleInput = []

for i in inputList:
    if i != '':
        puzzleInput.append(int(i))

count = 0
for i in range(1, len(puzzleInput)):
    if(puzzleInput[i] > puzzleInput[i-1]):
        count += 1
        #print(f"{puzzleInput[i]} is greater than {puzzleInput[i-1]}")

#print(count)
#print("The size of the data is " + str(len(puzzleInput))) 
#print("The last element of the list is " + str(puzzleInput[1999]))

#Part 2 -----------------------------------------------------------------

count = 0
for i in range(3, len(puzzleInput)):
    if((puzzleInput[i] + puzzleInput[i-1] + puzzleInput[i-2]) > (puzzleInput[i-1] + 
        puzzleInput[i-2] + puzzleInput[i-3])):
        count += 1
        print(f"{puzzleInput[i]} is greater than {puzzleInput[i-1]}")

print(count)
