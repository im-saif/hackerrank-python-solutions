def is_leap(year):
    leap = False

    # Write your logic here
    leap = year % 4 == 0 and (year % 100 != 0 or (year % 100 == 0 and year % 400 == 0))

    return leap