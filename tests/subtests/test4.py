from deep_timeit import deepTimeit, Colour
import time

def smallFunction(x):
    return x
  
deepTimeit(smallFunction, args=[5]).show()