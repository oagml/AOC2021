#Day 5

import numpy as np

#First, let's get the puzzle input
raw_data = open("puzzleInput").read().split('\n')
#Remove any empty characters from the list
raw_data.remove('')

#Function that creates  an np array of size n rows by n columns and returns it
def initialize_array():
    row_size = 1000
    col_size = 1000
    return np.zeros((row_size, col_size))

#Function that converts a list of strings into a list of ints:
def convert_str_to_int(input_list : list):
    int_list = []
    for element in input_list:
        int_list.append(int(element))

    return int_list


#Function that takes a string of type "278,281 -> 278,47" and returns two lists of size two
#One list contains the coordinates x1,y1(start) and the other contains x2,y2(end)
def extract_coordinates(input_str : str):
    start, end = input_str.split(" -> ")
    start = start.split(",")
    end = end.split(",")

    start = convert_str_to_int(start)
    end = convert_str_to_int(end)

    return start, end


array = initialize_array()

#print(f"The size of the input puzzle is {len(raw_data)}")
#print(raw_data)

for line in raw_data:
    #print(f"The current line being examined is {line}")
    start, end = extract_coordinates(line)

    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    #print(f"Which contains the x1,y1 values of {start} and the x2,y2 values of {end}")

    #Examine if the current input creates a horizontal line
    #x1 = x2 and y1 != y2
    if(x1 == x2):
        #Loop through every element between the start and end and add + 1 to each element
        for count in range(abs(y1 - y2) + 1):
            #print(f"There is a distance of {abs(y1 - y2)}")
            #print(f"Current iteration is {count}")
            if (y1 > y2):
                #print(f"Value to be update contains the coordinates {x1},{y2 + count}")
                #print(f"The value at these coordinates is {array[start[0]][end[1]+count]}")
                array[x1][y2+count] += 1
            else:
                array[x1][y1+count] += 1

    #Examine if the current input creates a vertical line
    elif(y1 == y2):
        #Loop through every element between the start and end and add + 1 to each element
        for count in range(abs(x1 - x2) + 1):
            if (x1 > x2):
                array[x2+count][y1] += 1
            else:
                array[x1+count][y1] += 1

    #Examine if the current input creates a diagonal line at exactly 45 (degrees) (slope == abs(1))
    else:
        if (abs((y2 - y1) / (x2 - x1)) == 1.0):
            print(f"The current input {start} , {end} creates a diagonal line of 45 deg")
            #There are 4 possible ways to create 45 degree diagonal lines
            #Increment or decrement in a for loop to connect start and end
            if(x1 > x2 and y1 > y2):
                distance = abs(x1 - x2)
                for count in range(distance + 1):
                    array[x2 + count][y2 + count] += 1

            elif(x1 > x2 and y1 < y2):
                distance = abs(x1 - x2)
                for count in range(distance + 1):
                    array[x2 + count][y2 - count] += 1

            elif(x1 < x2 and y1 > y2):
                distance = abs(x1 - x2)
                for count in range(distance + 1):
                    array[x2 - count][y2 + count] += 1

            elif(x1 < x2 and y1 < y2):
                distance = abs(x1 - x2)
                for count in range(distance + 1):
                    array[x2 - count][y2 - count] += 1
            else:
                print("Error: Diagonal line error")



#Count the elements that are greater than 1, this number represents where the lines overlap
count = 0
for row in array:
    for column in row:
        if column > 1:
            count += 1

print(f"There are {count} spaces where the lines overlap")
#print(array)
