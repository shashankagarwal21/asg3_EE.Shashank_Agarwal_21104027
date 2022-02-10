fib = [0, 1]  # First 2 terms of fibonacci sequence
new_ele = 0  # variable to add next number
average = 0  # variable for average
sum_terms = 0  # variable for sum of terms

num_terms = int(input("How may terms would you like to calculate "))  # Number of element in list

# If entered number is negative ask user to enter it again
while num_terms <= 0:
    num_terms = int(input("Enter a positive integer "))

# if num_term > 2 then add the sequence to the list fib
if num_terms > 2:
    for i in range(2, num_terms):
        new_ele = fib[i - 1] + fib[i - 2]
        fib.append(new_ele)

# Calculate sum of terms in sequence
for i in range(num_terms):
    sum_terms = sum_terms + fib[i]

# calculate average of sequence
average = (sum_terms/num_terms)

# Print the sequence
print("Sequence is ", end="")
for i in range(num_terms):
    print(fib[i], end=" ")

# Print the average of sequence
print("\nAverage is " + str(average))
