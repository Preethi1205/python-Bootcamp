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