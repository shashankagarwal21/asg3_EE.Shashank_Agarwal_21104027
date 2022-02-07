# create a dictionary of list to store grade and comment corresponding to the grade point
grade = {4: ["D", "Poor"], 5: ["C", "Below Average"], 6: ["C+", "Average"], 7: ["B", "Good"], 8: ["B+", "Very Good"], 9: ["A", "Excellent"], 10: ["A+", "Outstanding"]}

grade_point = int(input("Enter your Grade point "))  # take grade point from user

# if grade point is greater than 4 then search the dictionary
while True:
    if 4 <= grade_point <= 10:
        print("Your grade is \'" + grade[grade_point][0] + "\' and " + grade[grade_point][1] + " Performance")
        break
    # else print failed
    elif 0 <= grade_point < 4:
        print("Sorry you failed")
        break
    else:
        grade_point = int(input("please enter a valid grade point "))
