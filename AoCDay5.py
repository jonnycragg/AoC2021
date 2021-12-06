def readData(file):
    myCoords = []  # Declare an empty list
    with open(file, 'rt') as myfile:  # Open lorem.txt for reading text.
        for line in myfile:  # For each line of text,
            cleanline = line.replace(" ", "").replace("\n", "")
            chunks = cleanline.split('->')
            coords1 = chunks[0].split(',')
            coords2 = chunks[1].split(',')
            x1 = int(coords1[0])
            y1 = int(coords1[1])
            x2 = int(coords2[0])
            y2 = int(coords2[1])
            startC = (x1,y1)
            endC = (x2,y2)
            # only add these coords if a horizontal or vertical line (ignore diagonals)
            if horv(startC, endC):
                allPoints = getHVCoordsBetween([startC, endC])
            else:
                allPoints = getDIACoordsBetween([startC, endC])
            for coord in allPoints:
                myCoords.append(coord)
    return myCoords

def getHVCoordsBetween(coords):
    # sorting them so always incrementing
    coords.sort()
    x1 = coords[0][0]
    y1 = coords[0][1]
    x2 = coords[1][0]
    y2 = coords[1][1]
    # now work out is incrementing x or y
    if x1 == x2:
        while y1+1 < y2:
            coords.append((x1, y1+1))
            y1 = y1 + 1
    if y1 == y2:
        while x1+1 < x2:
            coords.append((x1+1, y1))
            x1 = x1 + 1

#    print("getCoordsBetween: " + str(coords) + "numbs are: " + str(x1) + str(y1) + str(x2) + str(y2) )
    return coords

def getDIACoordsBetween(coords):
    # sorting them so always going upwards
    coords.sort()
    x1 = coords[0][0]
    y1 = coords[0][1]
    x2 = coords[1][0]
    y2 = coords[1][1]
    # now work out if incrementing both x and y
    if (x2 > x1) and (y2 > y1):
        while (y1+1 < y2) and (x1+1 < x2):
            coords.append((x1+1, y1+1))
            y1 = y1 + 1
            x1 = x1 + 1

    if (x2 > x1) and (y2 < y1):
        while (y1-1 > y2) and (x1+1 < x2):
            coords.append((x1+1, y1-1))
            y1 = y1 - 1
            x1 = x1 + 1

#    print("getCoordsBetween: " + str(coords) + "numbs are: " + str(x1) + str(y1) + str(x2) + str(y2) )
    return coords

def horv(start,end):
    # x1 = x2 OR y1 = y2
    #print(start[0])
    if start[0] == end[0]:
        return True
    if start[1] == end[1]:
        return True
    return False

def myCoordsCount(data):
    from collections import Counter
    counter = Counter(data)
    #print(counter)
    answer = 0
    for k, v in counter.items():
        if v > 1:
            answer = answer + 1
    print(answer)

if (__name__ == "__main__"):
    myInput = readData('testinputDay5.txt')
    print(myInput)
    myCoordsCount(myInput)

    myInput = readData('realinputDay5.txt')
    #print(myInput)
    myCoordsCount(myInput)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
