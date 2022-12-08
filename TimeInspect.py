import inspect as inspector
import time
import timeit

def inspect(func, args=[], kwargs={}):
    alltimesvar = "dicttimes"
    linetimevar = "linetime"
    lines = inspector.getsource(func).rstrip().split("\n")
    start = lines[0]
    lines = lines[1:]
    timedChunksIndices = getChunksToTime(lines)
    newlines = []
    newlines.append(start)
    openbrace = "{"
    closebrace = "}"
    firstlineindentation = getIndentation(lines[1])
    newlines.append(firstlineindentation+f"{alltimesvar} = {openbrace}{closebrace}")
    newlines.append(firstlineindentation+f"for i in range({len(timedChunksIndices)}):")
    newlines.append(firstlineindentation+f"  {alltimesvar}[i] = 0")

    for lineindex, line in enumerate(lines):
        starttimerstoadd = []
        for timerindex, i in enumerate(timedChunksIndices):
            if lineindex == i[0]:
                starttimerstoadd.append(timerindex)
        for start in starttimerstoadd:
            newlines.append(getIndentation(line)+f"{linetimevar}{start} = time.time()")
        newlines.append(line)
        endtimerstoadd = []
        for timerindex, i in enumerate(timedChunksIndices):
            if lineindex == i[1]:
                endtimerstoadd.append(timerindex)
        for end in endtimerstoadd:
            newlines.append(getIndentation(line)+f"{alltimesvar}[{end}] += time.time()-{linetimevar}{start}")
    
    print("\n".join(newlines))

def getChunksToTime(lines):
    print(lines)
    indices = []
    for index, line in enumerate(lines):
        if line.lstrip().startswith("return "):
            continue
        lineindentation = getIndentation(line)
        nextlineindentation = getIndentation(lines[min(index+1, len(lines)-1)])
        if nextlineindentation <= lineindentation:
            indices.append([index, index])
        else:
            nextIndexWhereLEQ = len(lines)-1
            for newindex in range(index+1, len(lines)):
                if getIndentation(lines[newindex]) <= lineindentation:
                    nextIndexWhereLEQ = newindex-1
                    break
            indices.append([index, nextIndexWhereLEQ])
    
    return indices

def shouldAddTimer(lines, lineindex):
    if lineindex != len(lines)-1 and getIndentation(lines[lineindex]) < getIndentation(lines[lineindex+1]):
        return False
    if lines[lineindex].lstrip().startswith("return "):
        lines[lineindex] = ""
        return False
    return True


def getIndentation(line):
    try:
        return " "*line.index(line.lstrip()[0])
    except:
        return ""

def factorial(a, b, extraadd = True):      
    alltimes = {}
    for i in range(10):
      alltimes[i] = 0
    linstarttime = time.time()
    import random
    alltimes[1] += time.time()-linstarttime
    linstarttime = time.time()
    t = 1
    alltimes[2] += time.time()-linstarttime
    for i in range(1, a*b):
        linstarttime = time.time()
        t *= i
        alltimes[4] += time.time()-linstarttime
        linstarttime = time.time()
        x = 0
        alltimes[5] += time.time()-linstarttime
        if extraadd:
            for i in range(100000):
                x += i
    return t
    alltimes[9] += time.time()-linstarttime

print(factorial(5, 5))

def factorial(a, b, extraadd = True):
    import random
    t = 1
    for i in range(1, a*b):
        t *= i
        x = 0
        if extraadd:
            for i in range(100000):
                x += i
    return t

start = time.time()
factorial(5, 5)
print(time.time()-start)

inspect(factorial, args=[5, 10], kwargs={"extraadd": True})