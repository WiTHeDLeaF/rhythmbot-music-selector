import sys
import os.path
import random

argc = len(sys.argv)
parameters = sys.argv

command = sys.argv[0]
opFile = sys.argv[1]

count = 0
LineCount = 0
fileLine = 0
random.seed()

if(argc < 3):
    print("Usage: ", command, "argments .....")
    exit(1)

else:
    SelectCount = (int)(sys.argv[2])

    if os.path.isfile(opFile) == False:
        print("{0}: No such file or directory.".format(opFile))
        exit(1)

    with open (opFile, "r" , encoding="utf-8_sig") as r_file:

        for music in open(opFile , encoding="utf-8_sig").readlines():
            fileLine += 1
    
    if SelectCount > fileLine:
        print("Input num is over range.")
        exit(1)

index_set = set()

while len(index_set) < SelectCount:
    index_set.add(random.randint(1 , fileLine))

NumberList = list(index_set)

NumberList.sort()

with open (opFile, "r" , encoding="utf-8_sig") as r_file:

    for music in open(opFile , encoding="utf-8_sig").readlines():
        LineCount += 1
        name = music.split(",")

        if LineCount == NumberList[count]:
            print(name[0])
            print("!p {0}".format(name[1]))
            count += 1

        if count == SelectCount:
            break
