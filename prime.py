def fast_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <=n:
        if n%i == 0 or n % (i+2) == 0:
            return False
        i+=6
    return True

def prime_classic(n):
    flag = False
    if n == 1:
        return False
    if n > 1:
        for i in range(2, n):
            if n%i == 0:
                flag = True
                break
        if flag:
            return False
        return True
import time
def timer(func):
    # Print the runtime of the decorated function
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value
    return wrapper_timer
