def is_leap(year):


    leap = False
    if year in range(1900,10**5):
        x = year % 4
        z = year % 100
        y = year % 400
    if (x==0 or y==0) and z!=0:

        leap = True
    elif  z==0 and y==0:
        leap=True




    return leap



year = int(input())
print(is_leap(year))