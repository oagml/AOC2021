#Day 7

from matplotlib import pyplot as plt
import statistics

#Get puzzle input in a list:
input_list  = open("puzzleInput").read().split(',')
for index in range(len(input_list)):
    input_list[index] = int(input_list[index])


#Calculate the mean value
total_sum = sum(input_list)
mean = int((total_sum/len(input_list)))

#Calculate the mode
mode = statistics.mode(input_list)

#Calculate the median
median = statistics.median(input_list)

#Calculate the distance to the mean and add all the distances
total_distance = 0
for value in input_list:
    total_distance += abs(value - median)

print(f"The mean of the input values is {mean}")
print(f"The median of the input is {median}")
print(f"The mode of the input is : {mode}")
print(f"The size of the puzzle input is: {len(input_list)}")
print(f"The total distance to the mean is: {total_distance}")

#Part 2 -----------------------------------------------------------


#Plot the graph
mean_y_axis = [mean]*(len(input_list))
median_y_axis = [median]*(len(input_list))
plt.plot(input_list, 'ro')
plt.plot(x_axis, median_y_axis)
plt.show()
