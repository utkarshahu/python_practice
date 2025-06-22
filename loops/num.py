num = [1,2,3,4,5,6,7,8,9,10]
count=0
sum=0

for i in num:
    if i%2==0:
        sum+=i
    
    if i>0:
        count+=1
print(count,sum)
