import TimeInspect
import random

def factorial(a, b, extraadd = False):
    t = 1
    for i in range(1, a*b):
        t *= i
        x = 0
        if extraadd:
            for i in range(100000):
                p = random.randint(5, 100)
                x += p
    return t

TimeInspect.inspect(factorial, args=[5, 10], kwargs={"extraadd": True})