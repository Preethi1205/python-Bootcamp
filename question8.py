'''given an space sepaerated int list find the avg of elements present in the even index'''


li=list(map(int,input().split(",")))
#new=[]
sum=0
for i in range(len(li)):
    #if i%2==0:
       # new.append(li[i])
#print(new)
#for i in li:
    sum+=li[i]
print(sum/len(li))
