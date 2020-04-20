import sys
import os.path
import random

argc = len(sys.argv)
parameters = sys.argv

command = sys.argv[0]

count = 0
LineCount = 0
random.seed()

if(argc < 2):
    print("Usage: ", command, "argments .....")
    exit(1)

else:
    SelectCount = (int)(sys.argv[1])

    if os.path.isfile("MusicList.dat") == False:
        print("{0}: No such file or directory.".format("MusicList.dat"))
        exit(1)

index_set = set()

while len(index_set) < SelectCount:
    index_set.add(random.randint(1 , 95))

NumberList = list(index_set)

NumberList.sort()
print(NumberList)

with open ("MusicList.dat", "r" , encoding="utf-8_sig") as r_file:

    for music in open("MusicList.dat" , encoding="utf-8_sig").readlines():
        LineCount += 1
        name = music.split(",")

        if LineCount == NumberList[count]:
            print(name[0])
            print("!p {0}".format(name[1]))
            count += 1

        if count == SelectCount:
            break