score = int( input("Enter score : "))

if score >= 101:
    print("Please verify your grade ")
    exit()
    
if score>=90:
    grade = "A"
elif score>=80:
    grade = "B"        
elif score>=70:
    grade = "C"
elif score>=60:
    grade = "D"
else :
    grade = "E"


print(f"Grade of a student is {grade}");

