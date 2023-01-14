import inspect as inspector
import time
import copy
import tkinter
import colorsys
import matplotlib
from typing import Optional, Tuple, Union, List
import timeit


CHUNK_ADJACENCIES = {"if ": ["elif ", "else:"], "try:": ["except ", "except:", "finally:"]}

class Colour():
    """A simple class that allows you to create
    an RGB colour, and has a list of named colours
    as static variables."""

    ALICEBLUE = (240, 248, 255)
    ANTIQUEWHITE = (250, 235, 215)  
    AQUA = (0, 255, 255)
    AQUAMARINE = (127, 255, 212)    
    AZURE = (240, 255, 255)
    BEIGE = (245, 245, 220)
    BISQUE = (255, 228, 196)        
    BLACK = (0, 0, 0)
    BLANCHEDALMOND = (255, 235, 205)
    BLUE = (0, 0, 255)
    BLUEVIOLET = (138, 43, 226)     
    BROWN = (165, 42, 42)
    BURLYWOOD = (222, 184, 135)     
    CADETBLUE = (95, 158, 160)
    CHARTREUSE = (127, 255, 0)
    CHOCOLATE = (210, 105, 30)
    CORAL = (255, 127, 80)
    CORNFLOWERBLUE = (100, 149, 237)
    CORNSILK = (255, 248, 220)
    CRIMSON = (220, 20, 60)
    CYAN = (0, 255, 255)
    DARKBLUE = (0, 0, 139)
    DARKCYAN = (0, 139, 139)
    DARKGOLDENROD = (184, 134, 11)
    DARKGRAY = (169, 169, 169)
    DARKGREEN = (0, 100, 0)
    DARKGREY = (169, 169, 169)
    DARKKHAKI = (189, 183, 107)
    DARKMAGENTA = (139, 0, 139)
    DARKOLIVEGREEN = (85, 107, 47)
    DARKORANGE = (255, 140, 0)
    DARKORCHID = (153, 50, 204)
    DARKRED = (139, 0, 0)
    DARKSALMON = (233, 150, 122)
    DARKSEAGREEN = (143, 188, 143)
    DARKSLATEBLUE = (72, 61, 139)
    DARKSLATEGRAY = (47, 79, 79)
    DARKSLATEGREY = (47, 79, 79)
    DARKTURQUOISE = (0, 206, 209)
    DARKVIOLET = (148, 0, 211)
    DEEPPINK = (255, 20, 147)
    DEEPSKYBLUE = (0, 191, 255)
    DIMGRAY = (105, 105, 105)
    DIMGREY = (105, 105, 105)
    DODGERBLUE = (30, 144, 255)
    FIREBRICK = (178, 34, 34)
    FLORALWHITE = (255, 250, 240)
    FORESTGREEN = (34, 139, 34)
    FUCHSIA = (255, 0, 255)
    GAINSBORO = (220, 220, 220)
    GHOSTWHITE = (248, 248, 255)
    GOLD = (255, 215, 0)
    GOLDENROD = (218, 165, 32)
    GRAY = (128, 128, 128)
    GREEN = (0, 128, 0)
    GREENYELLOW = (173, 255, 47)
    GREY = (128, 128, 128)
    HONEYDEW = (240, 255, 240)
    HOTPINK = (255, 105, 180)
    INDIANRED = (205, 92, 92)
    INDIGO = (75, 0, 130)
    IVORY = (255, 255, 240)
    KHAKI = (240, 230, 140)
    LAVENDER = (230, 230, 250)
    LAVENDERBLUSH = (255, 240, 245)
    LAWNGREEN = (124, 252, 0)
    LEMONCHIFFON = (255, 250, 205)
    LIGHTBLUE = (173, 216, 230)
    LIGHTCORAL = (240, 128, 128)
    LIGHTCYAN = (224, 255, 255)
    LIGHTGOLDENRODYELLOW = (250, 250, 210)
    LIGHTGRAY = (211, 211, 211)
    LIGHTGREEN = (144, 238, 144)
    LIGHTGREY = (211, 211, 211)
    LIGHTPINK = (255, 182, 193)
    LIGHTSALMON = (255, 160, 122)
    LIGHTSEAGREEN = (32, 178, 170)
    LIGHTSKYBLUE = (135, 206, 250)
    LIGHTSLATEGRAY = (119, 136, 153)
    LIGHTSLATEGREY = (119, 136, 153)
    LIGHTSTEELBLUE = (176, 196, 222)
    LIGHTYELLOW = (255, 255, 224)
    LIME = (0, 255, 0)
    LIMEGREEN = (50, 205, 50)
    LINEN = (250, 240, 230)
    MAGENTA = (255, 0, 255)
    MAROON = (128, 0, 0)
    MEDIUMAQUAMARINE = (102, 205, 170)
    MEDIUMBLUE = (0, 0, 205)
    MEDIUMORCHID = (186, 85, 211)
    MEDIUMPURPLE = (147, 112, 219)
    MEDIUMSEAGREEN = (60, 179, 113)
    MEDIUMSLATEBLUE = (123, 104, 238)
    MEDIUMSPRINGGREEN = (0, 250, 154)
    MEDIUMTURQUOISE = (72, 209, 204)
    MEDIUMVIOLETRED = (199, 21, 133)
    MIDNIGHTBLUE = (25, 25, 112)
    MINTCREAM = (245, 255, 250)
    MISTYROSE = (255, 228, 225)
    MOCCASIN = (255, 228, 181)
    NAVAJOWHITE = (255, 222, 173)
    NAVY = (0, 0, 128)
    OLDLACE = (253, 245, 230)
    OLIVE = (128, 128, 0)
    OLIVEDRAB = (107, 142, 35)
    ORANGE = (255, 165, 0)
    ORANGERED = (255, 69, 0)
    ORCHID = (218, 112, 214)
    PALEGOLDENROD = (238, 232, 170)
    PALEGREEN = (152, 251, 152)
    PALETURQUOISE = (175, 238, 238)
    PALEVIOLETRED = (219, 112, 147)
    PAPAYAWHIP = (255, 239, 213)
    PEACHPUFF = (255, 218, 185)
    PERU = (205, 133, 63)
    PINK = (255, 192, 203)
    PLUM = (221, 160, 221)
    POWDERBLUE = (176, 224, 230)
    PURPLE = (128, 0, 128)
    REBECCAPURPLE = (102, 51, 153)
    RED = (255, 0, 0)
    ROSYBROWN = (188, 143, 143)
    ROYALBLUE = (65, 105, 225)
    SADDLEBROWN = (139, 69, 19)
    SALMON = (250, 128, 114)
    SANDYBROWN = (244, 164, 96)
    SEAGREEN = (46, 139, 87)
    SEASHELL = (255, 245, 238)
    SIENNA = (160, 82, 45)
    SILVER = (192, 192, 192)
    SKYBLUE = (135, 206, 235)
    SLATEBLUE = (106, 90, 205)
    SLATEGRAY = (112, 128, 144)
    SLATEGREY = (112, 128, 144)
    SNOW = (255, 250, 250)
    SPRINGGREEN = (0, 255, 127)
    STEELBLUE = (70, 130, 180)
    TAN = (210, 180, 140)
    TEAL = (0, 128, 128)
    THISTLE = (216, 191, 216)
    TOMATO = (255, 99, 71)
    TURQUOISE = (64, 224, 208)
    VIOLET = (238, 130, 238)
    WHEAT = (245, 222, 179)
    WHITE = (255, 255, 255)
    WHITESMOKE = (245, 245, 245)
    YELLOW = (255, 255, 0)
    YELLOWGREEN = (154, 205, 50)

    def __init__(self, r, g, b):
        self.rgb = (r, g, b)
    def __getitem__(self, key):
        return self.rgb[key]

class ColourRange():
    """A range of colours that can be defined,
    where the first colour listed in the constructor
    is for the slowest values being timed, and the
    last colour listed is for the fastest value, and
    the colour produced in the display is interpolated 
    through the list of colours. Static variables
    include pre-defined colour ranges, such as HEAT_MAP,
    TRAFFIC_LIGHT and RAINBOW."""

    HEAT_MAP = [Colour.RED, Colour.ORANGE, Colour.YELLOW, Colour.LIGHTBLUE, Colour.DARKBLUE]
    TRAFFIC_LIGHT = [Colour.RED, Colour.YELLOW, Colour.GREEN]
    RAINBOW = [Colour.PURPLE, Colour.INDIGO, Colour.BLUE, Colour.GREEN, Colour.YELLOW, Colour.ORANGE, Colour.RED]

    def __init__(self, colours: List[Union[Tuple[int, int, int], Colour]]):
        self.colours = colours

    def access(self, val: float):
        val = round(val, ndigits=5)
        interval = round(1/(len(self.colours)-1), ndigits=5)
        index = 0
        start = self.colours[index]
        end = self.colours[index+1]
        while val > interval:
            index += 1
            start = self.colours[index]
            end = self.colours[index+1]
            val -= interval
            val = round(val, ndigits=5)
        val *= (len(self.colours)-1)
        
        return (int(start[0]+(end[0]-start[0])*val), int(start[1]+(end[1]-start[1])*val), int(start[2]+(end[2]-start[2])*val))


class Time():
    def __init__(self, start, end, time, indentation, timesrun, nextindentation=None):
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
        self.timesrun = timesrun
        self.nextindentation = len(nextindentation) if nextindentation else nextindentation
    
    def __repr__(self):
        return str([self.start, self.end, self.time, self.indentation, self.nextindentation])

class Info():   
    def __init__(self, lines: list, times: Time, removed: Time, unabletobetimed: Time):
        self.lines = lines
        self.times = times
        self.removed = removed
        self.unabletobetimed = unabletobetimed
    
    def show(self, mintimetotrigger: Optional[float] = None, comparetopeer: bool = True, minsizeofdisplay: Tuple[int, int] = (30, 10), maxsizeofdisplay: Tuple[int, int] = (100, 30), xsizeofinfo: int = 30, colourrange: Union[ColourRange, Tuple[Tuple[int, int, int], Tuple[int, int, int], Tuple[int, int, int]]] = ColourRange([Colour(255, 0, 0), Colour(255, 255, 0), Colour(0, 255, 0)]), textcolour: Union[Colour, Tuple[int, int, int]] = Colour(0, 0, 0), backgroundcolour: Union[Colour, Tuple[int, int, int]] = Colour(255, 255, 255)):
        """Function that displays the info about the timed function. It produces a
        tkinter window that allows hovering over the line, that can be customized by
        the parameters.
        
        :param mintimetotrigger: Sets the minimum time the function has to take to 
        trigger the colour coding. Should be None or a float. Set to None by default.

        :param comparetopeer: If set to True, sets the time colour to the result of the
        comparison between the most time consuming function within the scope of all 
        lines of the same indentation, whereas if set to False it compares to the time
        taken of the entire function. Set to True by default.

        :param minsizeofdisplay: Sets the minimum size of the display, for example
        if the function timed is very small, then the smallest the screen will become
        is this parameter. Should be a tuple of integers.

        :param maxsizeofdisplay: Same as above, except the largest the screen will
        become is this parameter. Should also be a tuple of integers.

        :param xsizeofinfo: Integer that sets the width of the information box to the
        right of the display box.

        :param colourrange: Parameter of either type ColourRange or a tuple of 3 rgb
        colours in the form (r, g, b). Sets the range of colours that are displayed
        depending on the speed of each line of code. The order of colours goes slow,
        medium, and fast speed.

        :param textcolour: The colour of the text displayed, of type Colour or an rgb
        tuple.

        :param backgroundcolour: The colour of the background of the text displayed,
        of type Colour or an rgb tuple.
        """
        if type(colourrange) != ColourRange:
            colourrange = ColourRange(colourrange)

        MAXX, MAXY = maxsizeofdisplay
        MINX, MINY = minsizeofdisplay
        INFOXSIZE = xsizeofinfo
        root = tkinter.Tk()
        root.title("Function display")

        scroll_v = tkinter.Scrollbar(root)
        scroll_v.pack(side = tkinter.RIGHT, fill = "y")
        scroll_h = tkinter.Scrollbar(root, orient = tkinter.HORIZONTAL)
        scroll_h.pack(side = tkinter.BOTTOM, fill = "x")

        Output = tkinter.Text(root, width = max(min(MAXX, max([len(i) for i in self.lines])), MINX), height = max(min(MAXY, len(self.lines)), MINY), yscrollcommand = scroll_v.set, xscrollcommand = scroll_h.set, wrap = tkinter.NONE, bg=tohex(backgroundcolour.rgb if type(backgroundcolour) == Colour else backgroundcolour), fg=tohex(textcolour.rgb if type(textcolour) == Colour else textcolour))
        Info = tkinter.Text(root, width = INFOXSIZE, height = max(min(MAXY, len(self.lines)), MINY), bg=tohex(backgroundcolour.rgb if type(backgroundcolour) == Colour else backgroundcolour), fg=tohex(textcolour.rgb if type(textcolour) == Colour else textcolour))
        
        Output.pack(side=tkinter.LEFT)
        Info.pack(side=tkinter.RIGHT)

        scroll_h.config(command = Output.xview)
        scroll_v.config(command = Output.yview)

        for index, line in enumerate(self.lines):
            Output.insert(tkinter.INSERT, line.ljust(max([len(i) for i in self.lines]))+("\n" if index != len(self.lines)-1 else ""))
        mintime = 0
        maxtime = max(self.times, key=lambda x: x.time).time
        for index, timeset in enumerate(self.times):
            if comparetopeer:
                maxtime = max([i for i in self.times if self.getParent(i) == self.getParent(timeset)], key=lambda x: x.time).time
            col = self.getColour((1-timeset.time/maxtime) if maxtime > (mintimetotrigger if mintimetotrigger else 0) else 1, colourrange)
            tagid = index
            Output.tag_config(tagid, background=rgb_to_hex(col))
            Output.tag_config(str(tagid)+"a", background=rgb_to_hex(scale_lightness(col, 0.7)))
            setCol(Output, timeset, tagid, self.lines)
            Output.tag_bind(tagid, "<Enter>", lambda event, id=tagid: self.enter(event, id, Output, Info))
            Output.tag_bind(tagid, "<Leave>", lambda event, id=tagid: self.leave(event, id, Output, Info))
        for index, timeset in enumerate(self.removed):
            col = (0, 255, 255)
            tagid = str(index)+"f"
            Output.tag_config(tagid, background=rgb_to_hex(col))
            Output.tag_config(tagid+"a", background=rgb_to_hex(scale_lightness(col, 0.7)))
            setCol(Output, timeset, tagid, self.lines)
            Output.tag_bind(tagid, "<Enter>", lambda event, id=tagid: self.enter(event, id, Output, Info, tagtype="removed"))
            Output.tag_bind(tagid, "<Leave>", lambda event, id=tagid: self.leave(event, id, Output, Info, tagtype="removed"))
        for index, timeset in enumerate(self.unabletobetimed):
            col = (255, 0, 255)
            tagid = str(index)+"g"
            Output.tag_config(tagid, background=rgb_to_hex(col))
            Output.tag_config(tagid+"a", background=rgb_to_hex(scale_lightness(col, 0.7)))
            setCol(Output, timeset, tagid, self.lines)
            Output.tag_bind(tagid, "<Enter>", lambda event, id=tagid: self.enter(event, id, Output, Info, tagtype="unable"))
            Output.tag_bind(tagid, "<Leave>", lambda event, id=tagid: self.leave(event, id, Output, Info, tagtype="unable"))

        Output.config(state=tkinter.DISABLED)
        Info.config(state=tkinter.DISABLED)

        tkinter.mainloop()
    
    def getColour(self, val, range: ColourRange):
        return range.access(val)
    
    def enter(self, event, id, Output, Info, tagtype="timed"):
        setCol(Output, (self.times if tagtype == "timed" else (self.removed if tagtype == "removed" else self.unabletobetimed))[(int(id[:-1]) if type(id) == str else id)], str(id)+"a", self.lines)
        info = self.getInfo(id)
        Info.config(state=tkinter.NORMAL)
        Info.delete('1.0', tkinter.END)
        for line in info.split("\n"):
            Info.insert(tkinter.INSERT, line+"\n")
        Info.config(state=tkinter.DISABLED)
    
    def leave(self, event, id, Output, Info, tagtype="timed"):
        setCol(Output, (self.times if tagtype == "timed" else (self.removed if tagtype == "removed" else self.unabletobetimed))[(int(id[:-1]) if type(id) == str else id)], str(id)+"a", self.lines, remove=True)
        Info.config(state=tkinter.NORMAL)
        Info.delete('1.0', tkinter.END)
        Info.config(state=tkinter.DISABLED)
    
    def getInfo(self, id):
        if type(id) == int:
            idtype = "normal"
        elif id[-1] == "f":
            idtype = "removed"
        else:
            idtype = "untimable"
        timeobj = self.times[id] if idtype == "normal" else (self.removed[int(id[:-1])] if idtype == "removed" else self.unabletobetimed[int(id[:-1])])
        timetaken = timeobj.time
        timesrun = timeobj.timesrun
        parent = self.getParent(timeobj)
        info = f"""Info:

Total time taken: {'Unknown' if timetaken == None else self.formatTime(timetaken)}
Times run: {'Unknown' if timesrun == None else (timesrun if type(timesrun) == int else '>'+str(timesrun.maxval-1))}
Time taken per hit: {'Unknown' if timetaken == None or timesrun == 0 else self.formatTime(timetaken/timesrun)}
% of total time: {'Unknown' if timetaken == None or self.times[0].time == 0 else self.formatPercentage(timetaken/self.times[0].time*100)}
% of parent time: {'Unknown' if timetaken == None or parent == None or parent.time == 0 else self.formatPercentage(timetaken/parent.time*100)}"""
        return info
    
    def getParent(self, timeobj):
        maxlinevalid = -1
        maxvalid = None
        for time in self.times:
            if time.start[0] > maxlinevalid and time.end >= timeobj.end and time.start[0] < timeobj.start[0]:
                maxlinevalid = time.start[0]
                maxvalid = time
        return maxvalid
    
    def formatTime(self, timetaken):
        units = ["s", "ms", "μs", "ns", "ps"]
        unitindex = 0
        while timetaken < 0.1:
            if unitindex == len(units)-1:
                return "0s"
            unitindex += 1
            timetaken *= 1000
        return f"{timetaken:.4g}{units[unitindex]}"
    
    def formatPercentage(self, percentage):
        return f"{percentage:.4g}%"

class MaxSize():
    def __init__(self, maxval):
        self.maxval = maxval

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def tohex(t):
    return rgb2hex(*t)

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

def getAnnotatedFunction(lines):
    importantmarkings = ['''"""''', """'''""", '"', "'", "#"]
    markingdict = {i: False for i in importantmarkings}
    delaycount = 0
    markingindices = {i: [] for i in importantmarkings}
    for lineindex, line in enumerate(lines):
        for i in importantmarkings[2:]:
            markingdict[i] = False
        for charindex, char in enumerate(line):
            if delaycount > 0:
                delaycount -= 1
            if delaycount > 0:
                continue
            foundmarking = None
            activeindex = None
            for index, marking in enumerate(importantmarkings):
                if markingdict[marking] == True:
                    activeindex = index

            for marking in importantmarkings:
                if itemsFoundAtPosition(marking, line, charindex) and (activeindex == None or activeindex == importantmarkings.index(marking)):
                    foundmarking = marking
                    break
            if foundmarking != None:
                if foundmarking == "#":
                    valtosetto = True
                else:
                    valtosetto = not markingdict[foundmarking]
                if not markingdict[foundmarking]:
                    markingindices[foundmarking].append([(lineindex, charindex)])
                    if foundmarking == "#":
                        markingindices[foundmarking][-1].append((lineindex, len(line)-1))
                elif foundmarking != "#":
                    markingindices[foundmarking][-1].append((lineindex, charindex+len(foundmarking)-1))

                markingdict[foundmarking] = valtosetto
                delaycount = len(foundmarking)
    return markingindices

def itemsFoundAtPosition(marking, line, index):
    same = True
    for i in range(len(marking)):
        try:
            if line[index+i] != marking[i]:
                same = False
        except:
            return False
    return same

def simplify(lines):
    markingIndices = getAnnotatedFunction(lines)
    for quotetype in ["'''", '"""']:
        newlines = []
        endlineindexofmultilinestring = None
        shouldtruncateNext = False
        for index, line in enumerate(lines):
            if index in [i[0][0] for i in markingIndices[quotetype]]:
                quotemarkingindex = [i[0][0] for i in markingIndices[quotetype]].index(index)
                endlineindexofmultilinestring = markingIndices[quotetype][quotemarkingindex][1][0]
            if shouldtruncateNext:
                newlines[-1] += "\\n"+line
            else:
                newlines.append(line)
            shouldtruncateNext = False
            if endlineindexofmultilinestring != None:
                if index == endlineindexofmultilinestring:
                    shouldtruncateNext = False
                    endlineindexofmultilinestring = None
                else:
                    shouldtruncateNext = True

        lines = newlines
    
    markingIndices = getAnnotatedFunction(lines)

    newlines = []
    for index, line in enumerate(lines):
        validline = True
        if line.lstrip() == "":
            validline = False
        if line.lstrip().startswith("#"):
            validline = False
        if validline:
            if index in [i[0][0] for i in markingIndices["#"]]:
                commentmarkingindex = [i[0][0] for i in markingIndices["#"]].index(index)
                commentmarkingstart = markingIndices["#"][commentmarkingindex][0][1]
                line = line[:commentmarkingstart]
            if line.lstrip() != "":
                newlines.append(line)
    return newlines


def deepTimeit(func, args=[], kwargs={}, maxrepeats: Optional[int]=None) -> Info:
    """Function that times another function, that can be passed in
    through the func argument. Returns an Info object that has the
    method .show(), in order to display the information.
    
    :param args: A list of the arguments to be passed in to the
    function to be timed. Empty be default.
    
    :param kwargs: A dictionary of the keyword arguments to be
    passed in to the function to be timed. Empty be default.
    
    :param maxrepeats: The maximum number of times a chunk of
    code can be repeated before it stops being timed. Can be
    set to None for no limit. Note: if the limit is surpassed, the
    function will be timed again, this time without timing that
    chunk of code. This is risky if the code has side effects. If
    set to None, which it is by default, the code never re-attempts 
    timing."""

    alltimesvar = "dicttimes"
    allcountsvar = "dictcounts"
    allintervaledvar = "dictintervalled"
    linetimevar = "linetime"
    lines = inspector.getsource(func).rstrip().split("\n")
    newlines = []
    lines = simplify(lines)
    caller_module = inspector.getmodule(func)
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
        firstlineindentation = getIndentation(lines[0])
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
                newlines.append(getIndentation(line)+f"{linetimevar}{start} = time.perf_counter()")
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
                newlines.append(ind+f"{alltimesvar}[{end}] += time.perf_counter()-{linetimevar}{end}")
                newlines.append(ind+f"{allcountsvar}[{end}] += 1")
        
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
        exec(f"totaltime = time.perf_counter()\nreturnval = {funcname}(*args, **kwargs)\ntotaltime = time.perf_counter()-totaltime", globals(), localcopy)
        results = localcopy["returnval"]
        totaltime = localcopy["totaltime"]
        try:
            counts = results[-1]
            times = results[-2]
        except TypeError:
            print(strtoexec)
            raise TypeError
        try:
            maxx = max(counts.values())
        except ValueError:
            break
        if maxx == maxrepeats and maxrepeats != None:
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
    alltimes.append(Time([-1], len(oldlines), totaltime, "", 1, getIndentation(oldlines[0])))
    for index, timex in enumerate(times):
        alltimes.append(Time(timedChunksIndices[timex][0], timedChunksIndices[timex][1], times[timex], getIndentation(oldlines[firstifint(timedChunksIndices[timex][0])]), counts[index], None if firstifint(timedChunksIndices[timex][0]) == timedChunksIndices[timex][1] else getIndentation(oldlines[firstifint(timedChunksIndices[timex][0])+1])))

    alltimes = subtractChildrenTimingTimes(alltimes, counts)

    removedTimes = []
    for chunk in removedChunks:
        removedTimes.append(Time(chunk[0], chunk[1], None, getIndentation(oldlines[firstifint(chunk[0])]), MaxSize(maxrepeats), None if firstifint(chunk[0]) == chunk[1] else getIndentation(oldlines[firstifint(chunk[0])+1])))

    unableTimes = []
    for chunk in unableLines:
        unableTimes.append(Time(chunk[0], chunk[1], None, getIndentation(oldlines[firstifint(chunk[0])]), None, None))
    
    
    infoobj = Info([oldstart]+oldlines, alltimes, removedTimes, unableTimes)
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

def getTimeOfTimeFunc(count, mode="self"):
    if mode == "self":
        time1 = time.perf_counter()
        for i in range(count):
            x = time.perf_counter()
        t2 = time.perf_counter()-time1
        return t2
    elif mode == "child":
        dicttimes = [0]
        dictcounts = [0]
        time1 = time.perf_counter()

        for i in range(count):
            linetime6 = time.perf_counter()
            dicttimes[0] += time.perf_counter()-linetime6
            dictcounts[0] += 1

        t2 = time.perf_counter()-time1
        return t2

def subtractChildrenTimingTimes(times: List[Time], counts):
    newtimes = []
    #print(counts)
    #print(times)
    largconst = 1000000
    timeofselfrun = getTimeOfTimeFunc(largconst, mode="self")
    timeofchildrun = getTimeOfTimeFunc(largconst, mode="child")
    for index, time in enumerate(times):
        #print(time)
        children = getChildren(time, times)
        totalruntime = 0
        totalruntime += timeofselfrun*(counts[index-1] if index > 0 else 1)/largconst
        totalcount = 0
        for child, childindex in children:
            totalcount += counts[childindex-1] if childindex > 0 else 1

        totalruntime += timeofchildrun*(totalcount)/largconst
        #print(timeofchildrun, totalcount, largconst)
        time.time = max(time.time-totalruntime, 0)
        newtimes.append(time)
    return newtimes

def getChildren(time, times):
    tstart = time.start[0]
    tend = time.end
    children = []
    for index1, time1 in enumerate(times):
        t1start = time1.start[0]
        t1end = time1.end
        if t1start > tstart and t1end <= tend:
            children.append((time1, index1))
    return children
