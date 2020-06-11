from functools import wraps
from time import sleep

def delay(timer):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"Waiting {timer}s before running {fn.__name__}")
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def say_hi():
    return "hi"

print(say_hi()) #RETURNS:
# Waiting 3s before running say_hi
# hi