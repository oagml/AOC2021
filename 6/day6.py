#Day 6

#For day 6 we need to loop through a list of numbers and decrease by 1 when they are not equal to 0,
#If they are equal to 0, append a new number and start it with 8, after 80 days, how many numbers
#are in the list?

#Get the puzzle input
initial_fish = open("puzzleInput").read().split(',')

for index in range(len(initial_fish)):
    initial_fish[index] = int(initial_fish[index])


for iteration in range(40):
    print(iteration)
    print(len(initial_fish))
    for index in range(len(initial_fish)):
        age = initial_fish[index]
        if(age > 0):
            initial_fish[index] = age - 1
        elif(age == 0):
            initial_fish[index] = 6
            initial_fish.append(8)
        else:
            print("Error: Something happened")

print(initial_fish)
print(len(initial_fish))
