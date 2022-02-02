month_upper = [1, 3, 5, 7, 8, 10, 12]
date = input("Enter date in DD/MM/YYYY format ")
leap_check = False
day_limit = 0

while True:
    list_date = date.split("/")
    day = int(list_date[0])
    month = int(list_date[1])
    year = int(list_date[2])

    if (1 <= day <= 31) & (1800 <= year <= 2025) & (1 <= month <= 12):
        break

    else:
        date = input("Enter a valid date between year 1800 and 2025")


if year % 100 == 0:
    if year % 400 == 0:
        leap_check = True
    else:
        leap_check = False
elif year % 4 == 0:
    leap_check = True
else:
    leap_check = False


if month in month_upper:
    day_limit = 31
elif month == 2:
    if leap_check:
        day_limit = 29
    else:
        day_limit = 28
else:
    day_limit = 30

day = day + 1

if day > day_limit:
    day = 1
    month = month + 1

if month > 12:
    month = 1
    year = year + 1

print(str(day) + " / " + str(month) + " / " + str(year))