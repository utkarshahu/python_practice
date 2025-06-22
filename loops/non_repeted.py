string = "abcabcrabcbca"

for char in string:
    if string.count(char) ==1:
        print(f"Non-repeated string is : {char}")
        break
        
