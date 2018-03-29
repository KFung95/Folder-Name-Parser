import os
from time import gmtime, strftime

time = strftime("%Y-%m-%d %H;%M;%S", gmtime())

root = input("Enter a file directory: ") + '\\'
logDirectory = input("Enter the Log directory: ") + '\\'
list = os.listdir(root)
newList = []
logFile = logDirectory + 'Log ' + time + '.txt'
file = open(logFile, 'w', encoding='utf-8')
print("Successfully created " + logFile)



for i in range(len(list)):
    run = False
    try:
        original = list[i]
    except UnicodeEncodeError:
        continue
    temp = "-Stored " + original + " in List." + '\n'
    try:
        file.write(temp)
    except UnicodeEncodeError:
        continue
    index = 0
    length = len(original)
    while index < length:
        if original[0] != '[':
            if original[0] != '(':
                break
        if original[index] == ']':
            original = original[index+2:length]
            run = True
            break
        index += 1

    index = 0
    length = len(original)

    if run is True:
        while index < length:
            if original[index] == '[':
                original = original[0:index]
                break
            index += 1
    newList.append(original)

for o in range(len(list)):
    old = root+list[o]
    new = root+newList[o]
    if old != new:
        os.rename(old, new)
        temp = "-Renamed " + list[o] + " to " + newList[o] + '\n'
        file.write(temp)
    elif old == new:
        temp = '-' + list[o] + " doesn't need to be changed." + '\n'
        file.write(temp)
file.close()
input("Hit Enter to close.")
