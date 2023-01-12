import deep_timeit
import time

def add(a, b):
    accumilator = 0
    for i in range(a):
      accumilator += 1
    for i in range(b):
      accumilator += 1
    print(f"The result of the addition of a and b is: {accumilator}")

deep_timeit.deepTimeit(add, args=[100000, 200000]).show()
time1 = time.time()
add(100000, 200000)
time2 = time.time()-time1
print(time2)