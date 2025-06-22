age = int(input("Enter the age of user: \n"))

if age < 13:
    print("I am a Child.")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
