import inspect as inspector
import time

def inspect(func, args=[], kwargs={}):
    alltimesvar = "alltimesasdf"
    linestarttime = "linstarttime"
    lines = inspector.getsource(func).split("\n")[:-1]
    index = 0
    newlines = []
    newlines.append(lines[0])
    openbrace = "{"
    closebrace = "}"
    firstlineindentation = getIndentation(lines[1])
    newlines.append(firstlineindentation+f"{alltimesvar} = {openbrace}{closebrace}")
    newlines.append(firstlineindentation+f"for i in range({len(lines)}):")
    newlines.append(firstlineindentation+f"  {alltimesvar}[i] = 0")
    for lineindex, line in enumerate(lines[1:]):
        lineindex += 1
        index += 1
        indentation = getIndentation(line)
        if shouldAddTimer(lines, lineindex):
            newlines.append(indentation+f"{linestarttime} = time.time()")
        newlines.append(line)
        if shouldAddTimer(lines, lineindex):
            newlines.append(indentation+f"{alltimesvar}[{index}] += time.time()-{linestarttime}")
    print("\n".join(newlines))

def shouldAddTimer(lines, lineindex):
    if lineindex != len(lines)-1 and getIndentation(lines[lineindex]) != getIndentation(lines[lineindex+1]):
        return False
    if lines[lineindex].lstrip().startswith("return "):
        return False
    return True

def getIndentation(line):
    try:
        return " "*line.index(line.lstrip()[0])
    except:
        return ""

def factorial(a, b, extraadd = True):
    alltimesasdf = {}
    for i in range(11):
      alltimesasdf[i] = 0
    linstarttime = time.time()
    import random
    alltimesasdf[1] +=  time.time()-linstarttime
    linstarttime = time.time()
    t = 1
    alltimesasdf[2] +=  time.time()-linstarttime
    for i in range(1, a*b):
        linstarttime = time.time()
        t *= i
        alltimesasdf[4] +=  time.time()-linstarttime
        linstarttime = time.time()
        x = 0
        alltimesasdf[5] +=  time.time()-linstarttime
        if extraadd:
            for i in range(100000):
                linstarttime = time.time()
                p = random.randint(5, 100)
                alltimesasdf[8] +=  time.time()-linstarttime
                x += p
    return t, alltimesasdf

print(factorial(10, 15))

def factorial(a, b, extraadd = False):
    import random
    t = 1
    for i in range(1, a*b):
        t *= i
        x = 0
        if extraadd:
            for i in range(100000):
                p = random.randint(5, 100)
                x += p
    return t

inspect(factorial, args=[5, 10], kwargs={"extraadd": True})