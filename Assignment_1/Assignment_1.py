input_string = input("Enter a String ")  # take input form user
counter = {}  # create a dictionary called counter to store the number of occurance

#  if there are more than one word don't count letters and ouptut error
if " " in input_string:
    print("error: Please enter a single word")
else :
    # a for loop starting from first to last element of string
    for i in range(len(input_string)) :
        if input_string[i] in counter :  # if letter already exists then add one to it, if it doesn't then add it to the dictionary
            counter[input_string[i]] = counter[input_string[i]] + 1
        else:
            counter[input_string[i]] = 1

    print(counter)  # print the dictionary containing the counter
