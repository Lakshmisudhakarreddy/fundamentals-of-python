#write a program to enter marks of five subjects and calculate total,average and percentage
a=float(input("enter sanskrit marks:"))
b=float(input("enter telugu marks:"))
c=float(input("enter science marks:"))
d=float(input("enter maths marks:"))
e=float(input("enter social marks:"))
t=a+b+c+d+e
avg=t/5
per=(t/500)*100
print("total:",t,"average:",avg,"percentage%:",per)