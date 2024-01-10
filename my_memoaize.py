from time import perf_counter

def calc_runtime(func):
    def wrapper_decorator(*args,**kwargs):
        start_time=perf_counter()
        temp_func=func(*args,**kwargs)
        end_time=perf_counter()
        runtime=end_time-start_time
        print("Runtime of",func.__name__,"is",runtime)
        return runtime
    return wrapper_decorator

def memoize(func):
    memo = {}
    def wrapper_decorator(n):

        if n not in memo:
            memo[n]=func(n)
        return memo[n]
    return wrapper_decorator

@calc_runtime
@memoize
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(40))
