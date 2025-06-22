limit = 100

def even_generator(limit):
    for i in range(2,limit+1,2):
        # return i #return only 2 and get out from fx
        yield i
     

print("print even_generator ",even_generator(10))
r=iter(even_generator(10))
print(next(r))
print(next(r))
print(next(r))
print(next(r))
print(next(r))

for num in even_generator(20):
    print("Num : " ,num)
    
    