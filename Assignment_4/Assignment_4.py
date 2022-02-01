# create a dictionary of list to store grade and comment corresponding to the grade point
grade = {4: ["D", "Poor"], 5: ["C", "Below Average"], 6: ["C+", "Average"], 7: ["B", "Good"], 8: ["B+", "Very Good"], 9: ["A", "Excellent"], 10: ["A+", "Outstanding"]}

grade_point = int(input("Enter your Grade point "))  # take grade point from user

# if grade point is greater than 4 then search the dictionary
if grade_point >= 4:
    print("Your grade is \'" + grade[grade_point][0] + "\' and " + grade[grade_point][1] + " Performance")
# else show error
else:
    print("Sorry you failed")