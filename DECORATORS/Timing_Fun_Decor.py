import time

def timer(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f'Elapsed time: {end - start}')
        return result
    return wrapper
@timer
def example_function(n):
    time.sleep(n)

example_function(20)