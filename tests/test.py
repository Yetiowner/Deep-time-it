import os
from os import listdir
from os.path import isfile, join

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

__location__ = join(__location__, "subtests")

onlyfiles = [f for f in listdir(__location__) if isfile(join(__location__, f))]

for index, test in enumerate(onlyfiles):
    print(f"Running test {index+1}:")
    outcome = os.system(f"python {__location__}\\{test}")
    if outcome == 2:
        print("Test failed!")
    else:
        print("Test success!")