from collections import Counter

def readData(file):
    myData = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            cleanline = line.replace(" ", "").replace("\n", "")
            myData = cleanline.split(',')
            myData = [int(i) for i in myData]
            print(sorted(myData))
    return Counter(myData)

def calcSpawnNumbers(data):
    length = len(data)
    #print("Calc spawn numbers: " + str(data) + ", length=" + str(length))
    spawning = {}
    for k, v in data.items():
        #print("key=" + str(k) + ", count=" + str(v))
        if k == 0:  # k becomes a 6 and it spawns an 8
            try:
                spawning[6] += v
            except KeyError:
                spawning[6] = v
            try:
                spawning[8] += v
            except KeyError:
                spawning[8] = v
        if (k > 0) and (k < 9):  # k decreases by 1 only
            try:
                spawning[k-1] += v
            except KeyError:
                spawning[k-1] = v
    #print(spawning)
    #print(Counter(spawning))
    return Counter(spawning)

def mySpawnCount(data):
    answer = 0
    for k, v in data.items():
        answer = answer + v
    return answer

if (__name__ == "__main__"):
    myInput = readData('testinputDay7.txt')
    print(sorted(myInput))
    #print("OK, so i think: " + str(myInput))
#    i = 0
    #print("Day " + str(i) + ": " + str(myInput))
#    while i < 256:
#        i = i + 1
#        myInput = calcSpawnNumbers(myInput)
        #print("Day " + str(i) + ": " + str(myInput))
#    print("OK, so i think number of creatures = " + str(mySpawnCount(myInput)))
#   print("Test data with days: 80, total = " + str(calcSpawnNumbers(myInput)))

    myInput = readData('realinputDay7.txt')
    print(myInput)
#    i = 0
    # print("Day " + str(i) + ": " + str(myInput))
#    while i < 256:
#        i = i + 1
#        myInput = calcSpawnNumbers(myInput)
        # print("Day " + str(i) + ": " + str(myInput))
#    print("OK, so i think number of creatures = " + str(mySpawnCount(myInput)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/