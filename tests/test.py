import deep_timeit
import random
import time

p = 1

def factorial(a, b, extraadd = True):
    t = 1
    time.sleep(0.05)
    time.sleep(p/20)
    for i in range(1, a*b):
        t *= i
        x = 0
        y = 0
        if extraadd:
            for i in range(100000):
                y += i
                if i < 500:
                    x += i
                    x += random.randint(1, 100)
    return t

deep_timeit.deepTimeit(factorial, args=[5, 5], kwargs={"extraadd": True})