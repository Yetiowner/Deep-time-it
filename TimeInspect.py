import inspect as inspector
import time
import timeit

def inspect(func, args=[], kwargs={}):
    alltimesvar = "dicttimes"
    allcountsvar = "dictcounts"
    allintervaledvar = "dictintervalled"
    linetimevar = "linetime"
    triggerinterval = 600
    interval = 100
    lines = inspector.getsource(func).rstrip().split("\n")
    start = lines[0]
    #oldstart = start
    lines = lines[1:]
    timedChunksIndices = getChunksToTime(lines)
    newlines = []
    newlines.append(start)
    openbrace = "{"
    closebrace = "}"
    firstlineindentation = getIndentation(lines[1])
    for var in [alltimesvar, allcountsvar, allintervaledvar]:
        newlines.append(firstlineindentation+f"{var} = {openbrace}{closebrace}")
        newlines.append(firstlineindentation+f"for i in range({len(timedChunksIndices)}):")
        if var != allintervaledvar:
            newlines.append(firstlineindentation+f"  {var}[i] = 0")
        else:
            newlines.append(firstlineindentation+f"  {var}[i] = False")

    for lineindex, line in enumerate(lines):
        starttimerstoadd = []
        for timerindex, i in enumerate(timedChunksIndices):
            if lineindex == i[0]:
                starttimerstoadd.append(timerindex)
        for start in starttimerstoadd:
            newlines.append(getIndentation(line)+f"if not({allintervaledvar}[{start}]) or {allcountsvar}[{start}]%{interval} == 0: ")
            newlines.append(getIndentation(line)+f"    if {allcountsvar}[{start}] > {triggerinterval}:")
            newlines.append(getIndentation(line)+f"        {allintervaledvar}[{start}] = True")
            newlines.append(getIndentation(line)+f"    {linetimevar}{start} = time.time()")
        newlines.append(line)
        endtimerstoadd = []
        for timerindex, i in enumerate(timedChunksIndices):
            if lineindex == i[1]:
                endtimerstoadd.append([timerindex, getIndentation(lines[i[0]])])
        endtimerstoadd.sort(reverse=True, key=lambda x: x[0])
        for end, ind in endtimerstoadd:
            newlines.append(ind+f"if not({allintervaledvar}[{end}]) or {allcountsvar}[{end}]%{interval} == 0: ")
            newlines.append(ind+f"    if {allcountsvar}[{end}] > {triggerinterval}:")
            newlines.append(ind+f"        {allintervaledvar}[{end}] = True")
            newlines.append(ind+f"    {alltimesvar}[{end}] += time.time()-{linetimevar}{end}")
            newlines.append(ind+f"    {allcountsvar}[{end}] += 1")
    
    if newlines[-1].lstrip().startswith("return"):
        if newlines[-1].lstrip().startswith("return "):
            newlines[-1] += f", {alltimesvar}, {allcountsvar}"
        else:
            newlines[-1] += f" {alltimesvar}, {allcountsvar}"
    else:
        newlines.append(f"{getIndentation(lines[1])}return {alltimesvar}, {allcountsvar}")

    
    lines = "\n".join(newlines)
    strtoexec = "\n"+lines
    print(strtoexec)
    localcopy = locals()
    exec(strtoexec, globals(), localcopy)
    funcname = func.__name__
    exec(f"returnval = {funcname}(*args, **kwargs)", globals(), localcopy)
    print(localcopy["returnval"])

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
    import random
    t = 1
    for i in range(1, a*b):
        t *= i
        x = 0
        if extraadd:
            for i in range(100000):
                x += i
    print(t)
    return t

start = time.time()
factorial(5, 5)
print(time.time()-start, "asdf")

inspect(factorial, args=[5, 5])