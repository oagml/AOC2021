#Day 6

#For day 6 we need to loop through a list of numbers and decrease by 1 when they are not equal to 0,
#If they are equal to 0, append a new number and start it with 8, after 80 days, how many numbers
#are in the list?

#Get the puzzle input
initial_fish = open("puzzleInput").read().split(',')

for index in range(len(initial_fish)):
    initial_fish[index] = int(initial_fish[index])

'''
for iteration in range(80):
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
        '''

#Part 2 ------------------------------------------------------------------------------
#Define a function that counts the number of fish with their number of days left
#For example: 100 fish with 0 days left, 50 fish with 1,  42 with 2, etc.
def fish_count(fish_list, days):
    fish_lifespan = [0]*9
    #Count the the days left for each fish from the input list
    for i in fish_list:
        fish_lifespan[i] += 1        

    #Calculate the number of fish that there will be for a x number of days
    for iteration in range(days):
        newfish = fish_lifespan[0]
        fish_lifespan[0] = fish_lifespan[1]
        fish_lifespan[1] = fish_lifespan[2]
        fish_lifespan[2] = fish_lifespan[3]
        fish_lifespan[3] = fish_lifespan[4]
        fish_lifespan[4] = fish_lifespan[5]
        fish_lifespan[5] = fish_lifespan[6]
        fish_lifespan[6] = fish_lifespan[7] + newfish
        fish_lifespan[7] = fish_lifespan[8]
        fish_lifespan[8] = newfish


    #Count the total number of fish
    count = 0
    for i in range(len(fish_lifespan)):
        count += fish_lifespan[i]

    return count


#print(initial_fish)
print(fish_count(initial_fish, 256))
