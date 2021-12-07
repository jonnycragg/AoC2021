from collections import Counter


def readData(file):
    myData = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            cleanline = line.replace(" ", "").replace("\n", "")
            myData = cleanline.split(',')
            myData = [int(i) for i in myData]
            myData = sorted(myData)
    return myData


def calcfuel(steps):
    if steps == 0:
        return 0
    if steps == 1:
        return 1
    else:
        return steps + calcfuel(steps - 1)


def mySpawnCount(data):
    answer = 0
    for k, v in data.items():
        answer = answer + v
    return answer


if (__name__ == "__main__"):
    myInput = readData('testinputDay7.txt')
    print(myInput)
    start = myInput[0]
    end = myInput[-1]
    print(str(start) + ", " + str(end))
    crabCounts = Counter(myInput)
    possanswer = []
    while start <= end:
        answer = 0
        for k, v in crabCounts.items():
            answer = answer + sum(range(1, abs(start - k)+1)) * v
        start = start + 1
        possanswer.append(answer)
    print(sorted(possanswer))

    myInput = readData('realinputDay7.txt')
    print(myInput)
    start = myInput[0]
    end = myInput[-1]
    print(str(start) + ", " + str(end))
    crabCounts = Counter(myInput)
    possanswer = []
    while start <= end:
        answer = 0
        for k, v in crabCounts.items():
            answer = answer + sum(range(1, abs(start - k) + 1)) * v
        start = start + 1
        possanswer.append(answer)
    print(sorted(possanswer))