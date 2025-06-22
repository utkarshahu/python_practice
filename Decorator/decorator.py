# import time

# # ---------------- TIMER DECORATOR ----------------
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"⏱ Function '{func.__name__}' took {end - start:.2f} seconds to run")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(3)

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args) if args else "None"
        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else "None"
        print(f"📌 Calling '{func.__name__}' with args: {args_value} | kwargs: {kwargs_value}")
        return func(*args, **kwargs)
    return wrapper

@debug
def student2(gaming, paytm, name="Utkarsh", course="BCA"):
    print(f"Student Name: {name}, Course: {course}, Game: {gaming}, Paytm: {paytm}")

# ✅ Positional args only → kwargs will be None
student2("Car Racing", 2000)

# ✅ Now adding keyword args → kwargs will show
student2("Free Fire", 3000, name="Ankit", course="MCA")
