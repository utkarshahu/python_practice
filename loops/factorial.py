number = int(input("Enter the number : "))
factorial = 1

# while loop

while number>0:
    factorial = factorial*number
    number-=1
print(f"Factorial of a Number is : {factorial}")
