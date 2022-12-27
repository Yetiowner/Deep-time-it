from deep_timeit import deepTimeit, Colour
import time

def factorial(a, b, extraadd = True):
    import random
    t = 1
    time.sleep(0.05)
    time.sleep(1/20)
    p = '"Hello world!"'
    q = "'Hello world!'"
    """asdf
    asdf
    asdf ""# 12
'''
'''
    fdsa"""
    try:
        x = 1 # asdf1 # funny
    except:
        y = 1
    #asdf
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

deepTimeit(deepTimeit, args=[deepTimeit], kwargs={"args":[factorial], "kwargs":{"args":[3, 3]}}).show(backgroundcolour=Colour(255, 0, 255), textcolour=Colour(0, 0, 255), colourrange=((128, 128, 0), (128, 128, 128), (128, 128, 255)))