# print the leap year with in the given range
n=int(input())
a=int(input())
for i in range(n,a+1):#is to print  leap years in range of given numbers
    if i%400!=0 and i%4==0:#if i%4==0 and i%100!=0:
        print(i)
#else:
  #  print("not leap year")