#gcd of 2 numbers
#a Euclidean algorithm
'''a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
while b!=0:
    a,b=b,a%b
print(f"the gcd of a&b is: {a}")
#------------------------------------'''
#lcm
a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
lcm=0
while b!=0:
    a,b=b,a%b
    gcd=a
print(lcm)