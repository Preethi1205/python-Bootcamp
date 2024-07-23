''' 1) find number is even or odd
n=int(input())
if n%2==0:
    print("even")
else:
    print("odd")'''



'''2) find greatest of three
a,b,c=map(int,input().split())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)'''



'''3) sum of all elments in ana array

li=list(map(int,input().split()))
sum=0
for i in li:
    sum+=i
print(sum)'''


'''4) find max element in an array

li=list(map(int,input().split()))
ans=0
for i in range(len(li)):
    if ans<li[i]:
        ans=li[i]
print(ans)'''




'''5) find second max element in an array
'''
'''li=list(map(int,input().split()))
#li.sort()
print(li)
max=0
ans=0
for i in range(len(li)):
    if(ans<li[i]):
        ans=li[i]
for i in range(len(li)):
    if li[i]<ans and li[i]<max:
       max=li[i]
    
print(max) '''




'''6) reverse an array without using functions

li=list(map(int,input().split()))
#rev=li[::-1]

for i in range(len(li)-1,-1,-1):
   print(li[i],end=" ")
'''


''' 8) find the sum of squares of given number-123=14
     9) find sum of squares of even and odd digits 
      10) check whether given number is palindrome or not 
      11)write a program  to print first n fibonacci series '''



'''8) program 
n=int(input())
val=0
while n>0:
    num=n%10
    if num%2==0:#(for even square numbers)
        val=val+(num**2)
    n=n//10
print(val)
'''


'''9) program
n=int(input())
even=0
odd=0
while n>0:
    num=n%10
    if num%2==0:
        even+=(num**2)
    else:
        odd+=(num**2)
    n=n//10
sum=(even+odd)//2#average of sum of even and odd elements in an array
print(sum)
'''



'''10) program

n=int(input())
org=n
rev=0
while n>0:
    num=n%10
    rev=rev*10+num
    n=n//10
if rev==org:
    print(f"{org} is a palindrome")
else:
    print(f"{org} is not a palindrome")
'''




'''11) program

n=int(input())
n1=0
n2=1
count=0
if n==1:
    print(n1)
else:
    while count<n:
        print(n1,end=" ")
        val=n1+n2
        n1=n2
        n2=val
        count+=1'''



