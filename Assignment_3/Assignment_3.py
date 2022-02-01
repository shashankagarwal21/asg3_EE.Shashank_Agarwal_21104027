input_list = []  # list to store input
output_list = []  # list to store output
ele = 0

num_elements = int(input("How many numbers do you want to enter "))  # take input of number of numbers

# loop to add numbers to input list
for i in range(0,num_elements):
    ele = int(input("Enter number " + str(i + 1) + " "))
    input_list.append(ele)

# loop to make a list of tuple with first element ad number and second as its square
for i in range(0,num_elements):
    ele = (input_list[i],input_list[i]**2)
    output_list.append(ele)

print("output is " + str(output_list))  # Print the output

