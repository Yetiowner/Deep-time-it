from deep_timeit import deepTimeit, Colour
import time


def incrementalTime():
    """This is a function that takes incrementally long to run
    and is a good test of the range of colours."""
    time.sleep(1) # This takes a while to run
    time.sleep(2)
    time.sleep(3)
    time.sleep(4)
    time.sleep(5)
    time.sleep(6)
    time.sleep(7)
    time.sleep(8)
    time.sleep(9)
    time.sleep(10)
    for i in range(1):
        time.sleep(0.1)
        time.sleep(0.2)
        time.sleep(0.3)
        time.sleep(0.4)
        time.sleep(0.5)
        time.sleep(0.6)
        time.sleep(0.7)
        time.sleep(0.8)
        time.sleep(0.9)
        time.sleep(1)
        for j in range(1):
            time.sleep(0.01)
            time.sleep(0.02)
            time.sleep(0.03)
            time.sleep(0.04)
            time.sleep(0.05)
            time.sleep(0.06)
            time.sleep(0.07)
            time.sleep(0.08)
            time.sleep(0.09)
            time.sleep(0.1)

deepTimeit(incrementalTime).show()