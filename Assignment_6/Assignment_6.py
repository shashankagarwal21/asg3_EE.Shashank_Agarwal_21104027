true_list = ["y", "Y", "yes", "Yes", "YES"]  # List to store yes conditions
false_list = ["n", "N", "no", "No", "NO"]  # List to store no conditions
choice = input("Do you want to add a student (y/n) ")  # take input from user
temp_key = 0
data = {}  # dictionary to store user entered data
value_sorted_data = {}  # dictionary to store value sorted data
key_sorted_data = {}  # dictionary to store key sorted data

# Input Loop
while True:
    # if choice is yes take input, if no then exit list, else ask user for valid input
    if choice in true_list:
        temp_key = int(input("Enter student sid "))
        data[temp_key] = input("Enter student name ")
    elif choice in false_list:
        break
    else:
        choice = input("Enter a valid choice(y/n)")
        continue

    choice = input("Do you want to add another student(y/n) ")
# END


# Print students details stored in the dictionary
print("\n")
print("Student data: " + str(data))
# END


# Sort dictionary using student names
data_key = list(data.keys())
data_value = list(data.values())
data_value.sort()

# sorting loop
for i in data_value:
    for k in data_key:
        if data[k] == i:
            value_sorted_data[k] = data[k]
            break

print("\n")
print("Data sorted by name of student: " + str(value_sorted_data))
# END


# Sort dictionary using SID
data_key.sort()
for i in data_key:
    key_sorted_data[i] = data[i]

print("\n")
print("Data sorted by SID: " + str(key_sorted_data))
# END


# Search a student details with SID and print name of that student
sid_input = int(input("Enter SID of student you want to search "))
print(str(data[sid_input]) + " has SID " + str(sid_input))
# END
