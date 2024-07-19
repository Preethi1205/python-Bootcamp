'''a=int(input())
b=int(input())
print(a+b,a-b,a*b,a//b,a%b,a**b)'''



''' logical operators:
1. OR
2.AND
3.'''


'''age=int(input())
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("four and two wheeler")
elif(age>45 and age<=65):
    print("all")'''


'''apple=int(input())
banana=int(input())
orange=int(input())
apple_price=15
bananas_price=4
orange_price=5
total=int(input())
apple_total=apple*apple_price
banana_total=banana*bananas_price
orange_total=orange*orange_price
sum=apple_total+banana_total+orange_total
if sum<total:
    print("the person is not cheated")
else:
    print("the person is cheated")
'''


'''a=int(input())
if (a%2)==0 and a>0:
    print("even but positive")
elif(a%2)==0 and a<0:
    print("even but negitive")
elif(a%2)!=0 and a>0:
    print("odd but positive")
elif(a%2)!=0 and a<0:
    print("odd but negitive")'''
''''mr.z is selected for olympics he is participating in swimming competition.only one is selected in the competition
mr x and mr y are 
frends of mr z mr x is paticipating in badminton and y in table tennis according to the selection comittee,'''

x_height=int(input())
x_weight=int(input())
x_fat=int(input())
y_height=int(input())
y_weight=int(input())
y_fat=int(input())
medals_w=(14*50/100)
z_success=1
if x_height==140 and (x_weight%2)==0 and x_fat<12:
    x_success=1
    if  y_height>=118 and y_height<=148 and (y_weight%medals_w)==0 and y_fat==14:
        y_success=1
if  y_success and x_success and z_success:
    print("x,y,z meet at the plane")
else:
    print("x,y,z do not meet in the plane")

    




