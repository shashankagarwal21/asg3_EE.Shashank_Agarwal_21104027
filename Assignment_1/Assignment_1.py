input_string = input("Enter a word or a sentence ")  # take input form user
word_split = []  # list to split words of input_string
counter = {}  # create a dictionary called counter to store the number of occurance

word_split = input_string.split()  # count number of words

#  if there are more than one word don't count letters and count words
if len(word_split) > 1:
    # a for loop starting from first element to last of list
    for i in range(0,len(word_split)):
        if word_split[i] in counter:  # if world already exist in dictionary add 1 to counter else add it to dictionary
            counter[word_split[i]] = counter[word_split[i]] + 1
        else:
            counter[word_split[i]] = 1
else:
    # a for loop starting from first to last element of string
    for i in range(len(input_string)):
        if input_string[i] in counter:  # if letter already exists then add one to it, if it doesn't then add it to the dictionary
            counter[input_string[i]] = counter[input_string[i]] + 1
        else:
            counter[input_string[i]] = 1

print(counter)  # print the dictionary containing the counter