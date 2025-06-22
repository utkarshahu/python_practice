# day_input = input("Enter True/False for Wednesday: ").strip()
# day = day_input.lower() == "true"

# age = int(input("Enter the age: "))

# if age >= 18:
#     if day:
#         print("$2 discount so ticket price is $10.")
#     else:
#         print("Ticket price is $12.")
# else:  # no need for elif because the only other case is age < 18
#     if day:
#         print("$2 discount so ticket price is $6.")
#     else:
#         print("Ticket price is $8.")
day_input = input("Enter True/False for Wednesday: ").strip()
day = day_input.lower() == "true"

age = int(input("Enter the age: "))

price = 12 if age >= 18 else 8

if day:
    price -= 2

print(price)
print(f"Ticket price for you: ${price}")










