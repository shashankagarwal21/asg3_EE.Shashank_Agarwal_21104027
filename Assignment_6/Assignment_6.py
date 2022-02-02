true_list = ["y", "Y", "yes", "Yes"]
false_list = ["n", "N", "no", "No"]
choice = input("Do you want to add a student (y/n) ")
temp_key = 0
data = {}

while True:

    if choice in true_list:
        temp_key = int(input("Enter student sid "))
        data[temp_key] = input("Enter student name ")
    elif choice in false_list:
        break
    else:
        choice = input("Enter a valid choice(y/n)")
        continue

    choice = input("Do you want to add another student(y/n) ")

print(data)