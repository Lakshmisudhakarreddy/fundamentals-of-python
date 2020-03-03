##write a program to check whether leap year or not using conditional operator
year=int(input("enter year"))
if year%100==0:
    if year%400==0:
        print("it is leap year")
    else:
        print("normal year")
elif year%4==0:
    print("leap year")
else:
    print("non leap year")
        