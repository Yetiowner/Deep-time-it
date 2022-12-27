import deep_timeit

def add(a, b):
    accumilator = 0
    for i in range(a):
      accumilator += 1
    for i in range(b):
      accumilator += 1
    print(f"The result of the addition of a and b is: {accumilator}")

deep_timeit.deepTimeit(add, args=[10000, 20000]).show()