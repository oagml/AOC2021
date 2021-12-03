#Day 3

originalInput = open("puzzleInput").read().split('\n')
originalInput.pop() #Remove the last blank character

'''
oneCount = 0
zeroCount = 0
gama = ''
epsilon = ''

for digit in range(len(originalInput[0])):
    for number in originalInput:
        if number[digit] == '1':
            oneCount += 1
        else: #if number[digit] == '0'
            zeroCount += 1

    if oneCount > zeroCount:
        #gama.append(1)
        #epsilon.append(0)
        gama += '1'
        epsilon += '0'
    else: 
        #gama.append(0)
        #epsilon.append(1)
        gama += '0'
        epsilon += '1'

    oneCount = 0
    zeroCount = 0


print(f"Gama is equal to: {gama}")

print(f"Epsilon is equal to: {epsilon}")

'''

#Part 2 -----------------------------------------------------------------------

gamaList = originalInput.copy()
epsilonList = originalInput.copy()

print(gamaList)

oneCount = 0
zeroCount = 0
gamaTemp = []
epsilonTemp = []

numberSize = len(originalInput[0])

#Filter the gama number
for digit in range(numberSize):

    print(f"Looking at index: {digit}")

    #Find the most common number in each bit position:
    for number in gamaList:
        if number[digit] == '1':
            oneCount += 1
        else: #if number[digit] == '0'
            zeroCount += 1

    #Break when the list has been reduced to 1
    if(len(gamaList)== 1):
        break

    #If 1 is the most common digit at the current position, remove the numbers with the digit 0
    if(oneCount >= zeroCount):
        for number in gamaList:
            if(number[digit] == '1'):
                print(f"Most common number in position {digit} is 1, keeping {number}")
                gamaTemp.append(number)
            elif(number[digit] == '0'):
                print(f"Most common number in position {digit} is 1, removing {number}")
                #index = (gamaList.index(number))
                #gamaList.remove(number)
            else:
                print("Error: Something happened")

        gamaList = gamaTemp.copy()
        gamaTemp = []


    #If 0 is the most common digit at the current position, remove the numbers with the digit 1
    if(oneCount < zeroCount):
        for number in gamaList:
            if(number[digit] == '0'):
                print(f"Most common number in position {digit} is 0, keeping {number}")
                gamaTemp.append(number)
            else:
                print(f"Most common number in position {digit} is 0, removing {number}")
                #index = (gamaList.index(number))
                #gamaList.pop(index)

        gamaList = gamaTemp.copy()
        gamaTemp = []

    oneCount = 0
    zeroCount = 0


#Filter the epsilon number
for digit in range(numberSize):

    #Find the most common number in each bit position:
    for number in epsilonList:
        if number[digit] == '1':
            oneCount += 1
        else: #if number[digit] == '0'
            zeroCount += 1

    #Break when the list has been reduced to 1
    if(len(epsilonList)== 1):
        break

    #If 1 is the most common digit at the current position, remove the numbers with the digit 1
    if(oneCount >= zeroCount):
        for number in epsilonList:
            if(number[digit] == '1'):
                print(f"Most common number in position {digit} is 1, removing {number}")
            elif(number[digit] == '0'):
                print(f"Most common number in position {digit} is 1, keeping {number}")
                epsilonTemp.append(number)
            else:
                print("Error: Something happened")

        epsilonList = epsilonTemp.copy()
        epsilonTemp = []


    #If 0 is the most common digit at the current position, remove the numbers with the digit 1
    if(oneCount < zeroCount):
        for number in epsilonList:
            if(number[digit] == '0'):
                print(f"Most common number in position {digit} is 0, removing {number}")
            else:
                print(f"Most common number in position {digit} is 0, keeping {number}")
                epsilonTemp.append(number)

        epsilonList = epsilonTemp.copy()
        epsilonTemp = []

    oneCount = 0
    zeroCount = 0

print("Second part")
print(gamaList)
print(epsilonList)
