import inspect as inspector
import time
import copy
import tkinter
import colorsys
import matplotlib

CHUNK_ADJACENCIES = {"if ": ["elif ", "else:"], "try:": ["except ", "except:", "finally:"]}

class Time():
    def __init__(self, start, end, time, indentation, nextindentation=None):
        self.start = start
        if type(self.start) == list:
            for index, x in enumerate(self.start):
                self.start[index] = x+1
        else:
            self.start += 1
        self.end = end
        self.end += 1
        self.time = time
        self.indentation = len(indentation)
        self.nextindentation = len(nextindentation) if nextindentation else nextindentation
    
    def __repr__(self):
        return str([self.start, self.end, self.time, self.indentation, self.nextindentation])

class Info():
    def __init__(self, lines, times, removed, unabletobetimed):
        self.lines = lines
        self.times = times
        self.removed = removed
        self.unabletobetimed = unabletobetimed
    
    def show(self, mintimetotrigger=None):
        MAXX = 100
        MAXY = 30
        root = tkinter.Tk()
        root.title(" Function display ")

        scroll_v = tkinter.Scrollbar(root)
        scroll_v.pack(side = tkinter.RIGHT, fill = "y")
        scroll_h = tkinter.Scrollbar(root, orient = tkinter.HORIZONTAL)
        scroll_h.pack(side = tkinter.BOTTOM, fill = "x")

        Output = tkinter.Text(root, width = min(MAXX, max([len(i) for i in self.lines])), height = min(MAXY, len(self.lines)), yscrollcommand = scroll_v.set, xscrollcommand = scroll_h.set, wrap = tkinter.NONE)

        scroll_h.config(command = Output.xview)
        scroll_v.config(command = Output.yview)

        for index, line in enumerate(self.lines):
            Output.insert(tkinter.INSERT, line.ljust(max([len(i) for i in self.lines]))+("\n" if index != len(self.lines)-1 else ""))
        mintime = 0
        maxtime = max(self.times, key=lambda x: x.time).time
        for index, timeset in enumerate(self.times):
            rgb = colorsys.hsv_to_rgb(((1-timeset.time/maxtime) if maxtime > (mintimetotrigger if mintimetotrigger else 0) else 1) / 3., 1.0, 1.0)
            col = [round(255*x) for x in rgb]
            tagid = index
            Output.tag_config(tagid, background=rgb_to_hex(col))
            Output.tag_config(str(tagid)+"a", background=rgb_to_hex(scale_lightness(col, 0.7)))
            setCol(Output, timeset, tagid, self.lines)
            Output.tag_bind(tagid, "<Enter>", lambda event, id=tagid: self.enter(event, id, Output))
            Output.tag_bind(tagid, "<Leave>", lambda event, id=tagid: self.leave(event, id, Output))
        for index, timeset in enumerate(self.removed):
            col = (0, 255, 255)
            tagid = str(index)+"f"
            Output.tag_config(tagid, background=rgb_to_hex(col))
            Output.tag_config(tagid+"a", background=rgb_to_hex(scale_lightness(col, 0.7)))
            setCol(Output, timeset, tagid, self.lines)
            Output.tag_bind(tagid, "<Enter>", lambda event, id=tagid: self.enter(event, id, Output, tagtype="removed"))
            Output.tag_bind(tagid, "<Leave>", lambda event, id=tagid: self.leave(event, id, Output, tagtype="removed"))
        for index, timeset in enumerate(self.unabletobetimed):
            col = (255, 0, 255)
            tagid = str(index)+"g"
            Output.tag_config(tagid, background=rgb_to_hex(col))
            Output.tag_config(tagid+"a", background=rgb_to_hex(scale_lightness(col, 0.7)))
            setCol(Output, timeset, tagid, self.lines)
            Output.tag_bind(tagid, "<Enter>", lambda event, id=tagid: self.enter(event, id, Output, tagtype="unable"))
            Output.tag_bind(tagid, "<Leave>", lambda event, id=tagid: self.leave(event, id, Output, tagtype="unable"))
        Output.config(state=tkinter.DISABLED)
        Output.pack()
        tkinter.mainloop()
    
    def enter(self, event, id, Output, tagtype="timed"):
        setCol(Output, (self.times if tagtype == "timed" else (self.removed if tagtype == "removed" else self.unabletobetimed))[(int(id[:-1]) if type(id) == str else id)], str(id)+"a", self.lines)
    
    def leave(self, event, id, Output, tagtype="timed"):
        setCol(Output, (self.times if tagtype == "timed" else (self.removed if tagtype == "removed" else self.unabletobetimed))[(int(id[:-1]) if type(id) == str else id)], str(id)+"a", self.lines, remove=True)

def scale_lightness(rgb, scale_l):
    rgb = [i/255 for i in rgb]
    # convert rgb to hls
    h, l, s = colorsys.rgb_to_hls(*rgb)
    # manipulate h, l, s values and return as rgb
    return [round(i*255) for i in colorsys.hls_to_rgb(h, min(1, l * scale_l), s = s)]

def setCol(Output, timeset, tag, lines, remove=False):
    timesetstart = timeset.start
    if type(timesetstart) == int:
        timesetstart = [timesetstart]
    for start in timesetstart:
        if remove:
            Output.tag_remove(tag, f'{start+1}.0+{timeset.indentation}c', f'{start+1}.0+{len(lines[start])}c')
        else:
            Output.tag_add(tag, f'{start+1}.0+{timeset.indentation}c', f'{start+1}.0+{len(lines[start])}c')
    for endpos in range(timesetstart[0]+1, timeset.end+1):
        if remove:
            Output.tag_remove(tag, f'{endpos+1}.0+{timeset.indentation}c', f'{endpos+1}.0+{timeset.nextindentation}c')
        else:
            Output.tag_add(tag, f'{endpos+1}.0+{timeset.indentation}c', f'{endpos+1}.0+{timeset.nextindentation}c')

def rgb_to_hex(rgb):
    return matplotlib.colors.to_hex([i/255 for i in rgb])

def deepTimeit(func, args=[], kwargs={}, reattempt=True, show=True, mintime=None):
    alltimesvar = "dicttimes"
    allcountsvar = "dictcounts"
    allintervaledvar = "dictintervalled"
    linetimevar = "linetime"
    maxrepeats = 100000
    lines = inspector.getsource(func).rstrip().split("\n")
    newlines = []
    for line in lines:
        validline = True
        if line.lstrip() == "":
            validline = False
        if line.lstrip().startswith("#"):
            validline = False
        if validline:
            newlines.append(line)
    lines = newlines
    caller_frame = inspector.stack()[1]
    caller_module = inspector.getmodule(caller_frame[0])
    start = lines[0]
    oldstart = copy.deepcopy(start)
    lines = lines[1:]
    oldlines = copy.deepcopy(lines)
    needsToRedo = True
    ignores = []
    removedChunks = []

    while needsToRedo:
        lines = copy.deepcopy(oldlines)
        start = copy.deepcopy(oldstart)
        timedChunksIndices = getChunksToTime(lines)
        newchunks = []
        for index, chunk in enumerate(timedChunksIndices):
            if index not in ignores:
                newchunks.append(chunk)
            else:
                removedChunks.append(chunk)
        timedChunksIndices = newchunks
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
                i_0tocheck = copy.deepcopy(i[0])
                if type(i_0tocheck) == list:
                    i_0tocheck = i_0tocheck[0]
                if lineindex == i_0tocheck:
                    starttimerstoadd.append(timerindex)
            for start in starttimerstoadd:
                newlines.append(getIndentation(line)+f"if {allcountsvar}[{start}] < {maxrepeats}:")
                newlines.append(getIndentation(line)+f"    {linetimevar}{start} = time.time()")
            newlines.append(line)
            endtimerstoadd = []
            for timerindex, i in enumerate(timedChunksIndices):
                i_0tocheck = copy.deepcopy(i[0])
                if type(i_0tocheck) == list:
                    i_0tocheck = i_0tocheck[0]
                if lineindex == i[1]:
                    endtimerstoadd.append([timerindex, getIndentation(lines[i_0tocheck])])
            endtimerstoadd.sort(reverse=True, key=lambda x: x[0])
            for end, ind in endtimerstoadd:
                newlines.append(ind+f"if {allcountsvar}[{end}] < {maxrepeats}:")
                newlines.append(ind+f"    {alltimesvar}[{end}] += time.time()-{linetimevar}{end}")
                newlines.append(ind+f"    {allcountsvar}[{end}] += 1")
        
        for newlineindex, newline in enumerate(newlines):
            if newline.lstrip().startswith("return"):
                if newline.lstrip().startswith("return "):
                    newlines[newlineindex] += f", {alltimesvar}, {allcountsvar}"
                elif newline.lstrip() == "return":
                    newlines[newlineindex] += f" {alltimesvar}, {allcountsvar}"
            elif newlineindex == len(newlines)-1:
                newlines.append(f"{getIndentation(lines[1])}return {alltimesvar}, {allcountsvar}")

        
        lines = "\n".join(newlines)
        strtoexec = "\n"+lines
        #print(strtoexec)
        localcopy = locals()
        globalcopy = globals()
        try:
            globalcopy.update(caller_module.__dict__)
        except AttributeError:
            pass
        try:
            exec(strtoexec, globalcopy, localcopy)
        except SyntaxError:
            print(strtoexec)
            raise SyntaxError
        funcname = func.__name__
        exec(f"totaltime = time.time()\nreturnval = {funcname}(*args, **kwargs)\ntotaltime = time.time()-totaltime", globals(), localcopy)
        results = localcopy["returnval"]
        totaltime = localcopy["totaltime"]
        try:
            counts = results[-1]
            times = results[-2]
        except TypeError:
            print(strtoexec)
            raise TypeError
        maxx = max(counts.values())
        if maxx == maxrepeats and reattempt:
            needsToRedo = True
            ignores = []
            for i in counts:
                if counts[i] == maxrepeats:
                    ignores.append(i)
        else:
            needsToRedo = False
    
    unableLines = []
    for index, line in enumerate(oldlines):
        if unabletotime(line):
            unableLines.append([[index], index])

    alltimes = []
    alltimes.append(Time([-1], len(oldlines), totaltime, "", getIndentation(oldlines[0])))
    for timex in times:
        alltimes.append(Time(timedChunksIndices[timex][0], timedChunksIndices[timex][1], times[timex], getIndentation(oldlines[firstifint(timedChunksIndices[timex][0])]), None if timedChunksIndices[timex][0] == timedChunksIndices[timex][1] else getIndentation(oldlines[firstifint(timedChunksIndices[timex][0])+1])))
    
    removedTimes = []
    for chunk in removedChunks:
        removedTimes.append(Time(chunk[0], chunk[1], None, getIndentation(oldlines[firstifint(chunk[0])]), None if chunk[0] == chunk[1] else getIndentation(oldlines[firstifint(chunk[0])+1])))

    unableTimes = []
    for chunk in unableLines:
        unableTimes.append(Time(chunk[0], chunk[1], None, getIndentation(oldlines[firstifint(chunk[0])]), None))
    
    
    infoobj = Info([oldstart]+oldlines, alltimes, removedTimes, unableTimes)
    if show:
        infoobj.show(mintime)
    else:
        return infoobj

def unabletotime(line):
    if line.lstrip() == "return" or line.lstrip().startswith("return "):
        return True
    return False

def firstifint(a):
    if type(a) == list:
        return a[0]
    return a

def getChunksToTime(lines):
    indices = []
    for index, line in enumerate(lines):
        if line.lstrip().startswith("return "):
            continue
        lineindentation = getIndentation(line)
        nextlineindentation = getIndentation(lines[min(index+1, len(lines)-1)])
        if nextlineindentation <= lineindentation:
            indices.append([[index], index])
        else:
            adjacentchunktitles = []
            for i in CHUNK_ADJACENCIES:
                for j in CHUNK_ADJACENCIES[i]:
                    adjacentchunktitles.append(j)
            shouldcont = False
            for i in adjacentchunktitles:
                if lines[index].lstrip().startswith(i):
                    shouldcont = True
            if shouldcont:
                continue
            nextIndexWhereLEQ = len(lines)-1
            startindex = [index]
            for newindex in range(index+1, len(lines)):
                if getIndentation(lines[newindex]) <= lineindentation:
                    partofadjacent = False
                    for key in CHUNK_ADJACENCIES:
                        if lines[index].lstrip().startswith(key):
                            partofadjacent = CHUNK_ADJACENCIES[key]
                    if partofadjacent != False:
                        oneofadjacent = False
                        for potadj in partofadjacent:
                            if lines[newindex][len(getIndentation(lines[index])):].startswith(potadj):
                                oneofadjacent = True
                        if not(oneofadjacent):
                            nextIndexWhereLEQ = newindex-1
                            break
                        else:
                            startindex.append(newindex)
                    else:
                        nextIndexWhereLEQ = newindex-1
                        break
            indices.append([startindex, nextIndexWhereLEQ])
    
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
    time.sleep(0.05)
    time.sleep(1/20)
    try:
        x = 1
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

deepTimeit(deepTimeit, args=[deepTimeit], kwargs={"args":[factorial], "kwargs":{"args":[5, 5]}})
#deepTimeit(deepTimeit, args=[factorial], kwargs={"args":[5, 5]})
#deepTimeit(factorial, args=[5, 5])