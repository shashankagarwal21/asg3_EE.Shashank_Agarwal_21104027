# string to store character of pattern
pattern = "ABCDEFGHIJK"

length = len(pattern)  # find length of pattern

j = 0
l = 0

# loop for printing the pattern
while j <= length:
    # loop for the spaces
    for k in range(0, l):
        print(" ", end=" ")

    # loop for character of pattern
    for i in range(0, length-j):
        print(pattern[i], end=" ")

    print("\n")

    j = j + 2
    l = l + 1
