# Step 1: Write to the file
file = open("yttube.py", "w")
try:
    file.write("I am writing file\n")  # added newline
finally:
    file.close()

# Step 2: Read from the file
file = open("yttube.py", "r")
try:
    while True:
        line = file.readline()
        if not line:
            break
        print(line, end=" ")  # or just: print(line, end="")
finally:
    file.close()
