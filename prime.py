'''n=int(input())
c=0
#r=n**0.5
if n<2:
    print("not a prime number")
elif n==2:
    print("prime number")
else:
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            c=c+1
            break
    if c==0:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")'''


# write a program to print all the prime numbers in a given range

'''n=int(input())
c=0
a=2
#r=n**0.5
if n<2:
    print("not a prime number")
elif n==2:
    print("prime number")
for i in range(a,n+1):
    if a%i==0:
        c=c+1
        break
else c==0:
    print(i,end=" ")
    #else:
       # print(n,"is not a prime number")'''



'''a=int(input())
b=int(input())
for i in range(a,b+1):# to all the prime numbers in a given range
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")'''