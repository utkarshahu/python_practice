def print_user(**kwargs):
    print(kwargs)                 # Prints the entire dictionary
    # print(**kwargs)             # ❌ Remove or comment this line, it causes an error
    print(kwargs.items())         # Prints the dict_items object
    for key, value in kwargs.items():
        print(f"Key: {key}, value: {value}")

print_user(name="utkarsh")
print_user(name="utkarsh", course="BCA")
print_user(name="utkarsh", course="BCA", age=20)
