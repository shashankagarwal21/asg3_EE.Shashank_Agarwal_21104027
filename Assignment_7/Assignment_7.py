fib = [0, 1]  # First 2 terms of fibonacci sequence
average = 0  # variable for average

# Number of element in list
num_terms = int(input("How may terms would you like to calculate "))

# If entered number is negative ask user to enter it again
while num_terms <= 0:
    num_terms = int(input("Enter a positive integer "))

# if num_term > 2 then add the sequence to the list fib
if num_terms > 2:
    for i in range(2, num_terms):
        new_ele = fib[i - 1] + fib[i - 2]
        fib.append(new_ele)

# calculate average of sequence
average = (sum(fib[0:num_terms])/num_terms)

# Print the sequence
print("Sequence is ", end="")
print(fib[0:num_terms])

# Print the average of sequence
print("Average is " + str(average))
