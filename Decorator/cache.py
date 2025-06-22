
def cache_decoreator(func):
    cache = {}
    print(cache)
    def wrapper(*args):
        if args in cache:
            print(f"Returning Catch result for args {args}")
            print (cache[args])
            return cache[args]
        else:
            print(f"ccalculating new result for args {args}")
            
            result = func(*args)