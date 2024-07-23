import math
a=int(input())
b=int(input())
s=a*b
while b!=0:
    a,b=b,a%b
    gcd=a
#print(gcd)
lcm=s//gcd
print(lcm)






