#write a program to P,T,R and calculate simple interest And compound interest
p=float(input("enter principle amount:"))
t=float(input("enter time period:"))
r=float(input("enter rate:"))
SI=(p*t*r)/100 #simple interest=(P*T*R)/100
print("simple interest:",SI)
CI=p*(1+r/100)**t #compound interest=P(1+1/r)^t
print("compound interest:",CI)
