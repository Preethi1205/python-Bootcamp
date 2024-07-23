'''if n <8:
            print("follow the conditions")
            str[0]='@'
            str[1]='/'
            for i in password:
                if(i in str[0] or str[1]) and i is not="":
                    count+=1
                    break
                    '''


my_list=list(map(int,input().split()))
#count=0
#sum=0
for i in range(1,len(my_list)-1):
    if my_list[i]>my_list[i-1] and my_list[i]>my_list[i+1]:
       # count=i
        #sum+=my_list[i]# to print the sum of peek elements
        print(my_list[i],end=" ")
#print(sum)



#optimized way
my_list=list(map(int,input().split()))
count=0
for i in range(1,len(my_list)-1):
       if my_list[1]>my_list[i-1] and my_list[i]>my_list[i+1]:
            count=1
if(my_list[-1]>my_list[-2] and my_list[-1]>count):
    count=len(my_list)-1
print(my_list[count])