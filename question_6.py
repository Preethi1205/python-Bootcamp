'''you will take list of elements and count no of even and odd number
take a space seperated input from user and print alternate elements

n=int(input())
li=list(map(int,input().split()))
alter=li[::2]
print(*alter)



# using for loop
n=int(input())
li=list(map(int,input().split()))
for i in range(0,len(li),2):
    print(li[i])
'''



'''quest you are given with  a comma seperated natural numbers 1 to 10 print only the even nummbers'''

