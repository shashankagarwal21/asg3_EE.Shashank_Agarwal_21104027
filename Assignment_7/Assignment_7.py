fib = [0, 1]  # First 2 terms of fibonacci sequence
new_ele = 0  # variable to aff next number
average = 0  # variable for average

num_terms = int(input("How may terms would you like to calculate "))  # Number of element in list

# if num_term > 2 then add the sequence to the list fib and print it
if num_terms > 2:
    for i in range(2, num_terms):
        new_ele = fib[i - 1] + fib[i - 2]
        fib.append(new_ele)
    average = (sum(fib)/num_terms)
    print("Sequence is " + str(fib))
    print("Average is " + str(average))

# else if num_term = 1 then 0 is sequence and if num_term = 2 then sequence is 0, 1
else:
    if num_terms == 1:
        print("sequence is " + str(fib[0]))
        print("Average is 0")
    elif num_terms == 2:
        print("sequence is " + str(fib[0]) + ", " + str(fib[1]))
        print("Average is 0.5")
    else:
        print("error:Enter a positive integer")
