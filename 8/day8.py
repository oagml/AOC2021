#Day 8

puzzle_input = open("puzzle_input").read().split('\n')
puzzle_input.pop()

def separate_signals(raw_data):
    signal_patterns = []
    signal_outputs = []

    for string in raw_data:
        signal_pattern, signal_output = string.split(' | ')

        signal_patterns.append(signal_pattern)
        signal_outputs.append(signal_output)

        #print(f"The signal pattern of this string is: {signal_pattern}")
        #print(f"The signal output this string is: {signal_output}")

    return signal_patterns, signal_outputs

def split_signal_outputs(signal_outputs):
    return signal_outputs.split(' ')

def find_one(string):
    count = 0
    for element in string:
        if len(element) == 2:
            count += 1
    return count

def find_four(string):
    count = 0
    for element in string:
        if len(element) == 4:
            count += 1
    return count

def find_seven(string):
    count = 0
    for element in string:
        if len(element) == 3:
            count += 1
    return count

def find_eight(string):
    count = 0
    for element in string:
        if len(element) == 7:
            count += 1
    return count


def find_digits(signal_outputs):
    count_of_numbers = [0]*10
    print(count_of_numbers)
    for signal_output in signal_outputs:
        current_output = split_signal_outputs(signal_output)
        for index in range(len(count_of_numbers)):
            if index == 1:
                count_of_numbers[index] += find_one(current_output)
                print(f"Adding {find_one(current_output)} to the one count")
            elif index == 4:
                count_of_numbers[index] += find_four(current_output)
            elif index == 7:
                count_of_numbers[index] += find_seven(current_output)
            elif index == 8:
                count_of_numbers[index] += find_eight(current_output)

    print(f"The total of numbers found for each digit is {count_of_numbers}")
    print(f"The total number of all digits found is {sum(count_of_numbers)}")


signal_patterns, signal_outputs = separate_signals(puzzle_input)
find_digits(signal_outputs)


