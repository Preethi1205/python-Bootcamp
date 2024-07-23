'''print(ord('a'))
print(ord('A'))
print(ord('0'))
print(ord('<'))
print(ord('>'))
print(chr(67))'''
#check how many vowels are present in agiven string

'''s=['a','e','i','o','u']
n=input()
c=0
for i in n:
    if i in s:
        c+=1
print(c)
'''
#write a program to print all the consonants 

'''s="bcdfghjklmnpqrstvwxyz"
a="aeiou"
n=input()
n=n.lower()
c=0
count=0
for i in n:
    if i in a:
        count+=1 
for i in n:
    if i in s:
        c+=1
print(count)
print(c)
'''

#print all the vowels followed by consonants

'''
n=input()
v="aeiou"
c="bcdfghjklmnpqrstvwxyz"
n=n.lower()
for i in n:
   if i in v:
        print(i,end="")
for i in n:
    if i in c:
        print(i,end="")
'''

#print the unique characters in a string
'''n=input()
c=0
new=[] new=""
for i in n:
    if i not in new:
        new.append(i) new+=i
    elif i in new:
        c+=1
print(*new)'''

# print the sum of numbers in a string
'''n=input()
s=0
for i in n:
    if i.isdigit():
        s+=int(i)
print(s)
'''

#without using built in ffunctions
'''n=input()
s=0
a='0123456789'
for i in n:
    if i in a:
       s+=int(i)
print(s)'''


#reverse the numbers present in agiven string
'''n=input()
n1="0123456789"
new=""
for i in n:
    if i in n1:
        new=new+i
print(int(new))
for i in range(len(new)-1,-1,-1):
    print(new[i],end=" ")'''



#to print the ascii values from of the characters
'''for i in range(32,128):
    print(chr(i),end=" ")
print("\n")'''

'''for i in range(65,91):
    print(chr(i),end=" ")
print("\n")
for i in range(97,123):
    print(chr(i),end=" ")

#print the sum of values using ascii values
n=input()
r=0
for i in n:
    if ord(i)>=48 and ord(i)<=57:
        r+=int(i)
print(r)
'''

#write a code to print all capital letters in a given string
'''n=input()
r=""
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        r+=i
print(r)
 '''

#writr a code to print all small letters in string
'''n=input()
r=""
for i in n:
    if ord(i)>=65 and ord(i)<=90:
        r+=i
print(r)
'''
#remove all the brackets from given algebraic expression

'''n=input()
a=""
for i in n:
    if ord(i)!=40 and  ord(i)!=41 and ord(i)!=91 and ord(i)!=93 and  ord(i)!=123 and  ord(i)!=125:
       #ord(i)==40 or ord(i)==41 or  ord(i)==91 or ord(i)==93 or ord(i)==123 or ord(i)==125:
       #pass
       a+=i 
    #else:
       #print(i,end=" ")
print(a)
'''



'''n=input()
for i in n:
    m=ord(i)+4
    print(chr(m),end="")
'''

n=input()
skip=int(input())
for i in n:
    x=ord(i)+skip
    if x>=122 or x>=91:
        y=x-26
        print(chr(y),end="")

        

'''n=input()
for i in n:
    m=ord(i)%4
    print(chr(m),end=" ")
'''
'''n=input()
m=0
for i in n:
    if ord(i)>=123:
        m=m-26
print(chr(m),end="")
'''


#input hello world------
#output -----helloworld
'''n=input()
y=""
count=0

for i in n:
    if ord(i)==45:
        count+=1
    else:
        y+=i
print("-"*count+y)
'''
'''*****  
   *****
   *****
   *****
   ***** print the above pattern as following'''

'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()
'''


n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print("0",end="")
        else:
            print("*",end="")
    print()

#homework questions
# print upper triangle matrix
#print lower triagular matrix
#print rhombus and parallelogram
# print number pyramid

