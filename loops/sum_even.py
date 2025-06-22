n=int(input("Enter the number : "))
sum = 0
sum_even = 0

for i in range(1,n+1):
    sum+=i
    if i%2==0:
        sum_even+=i

print(f"The sum of {n} natural num is {sum}")
print(f"The sum of {n} even natural num is {sum_even}")
    