

x =99

def f1():
    x=88
    def f2():
        print(x)
    return f2

my_result = f1()
my_result()