# SORT ANALYZER STARTER CODE

import time

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp


# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
# startTime = time.time()
# bubbleSort(randomData)
# endTime = time.time()
# print(f"Bubble Sort Random Data: {endTime - startTime} seconds")
def bubbleSort(anArray):
    for i in range(len(anArray)):
        for i in range(len(anArray) - 1):
            if(anArray[i] > anArray[i+1]):
                anArray[i], anArray[i+1] = anArray[i+1], anArray[i]

def selectionSort(anArray):
    for i in range(len(anArray)):
        minPos = i
        for j in range(i + 1, len(anArray)):
            if(anArray[j] < anArray[minPos]):
                minPos = j
        anArray[i], anArray[minPos] = anArray[minPos], anArray[i]


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertVal = anArray[i]
        insertPos = i
        while insertPos > 0 and anArray[insertPos-1] > insertVal:
            anArray[insertPos], anArray[insertPos-1] = anArray[insertPos-1], anArray[insertPos]
            insertPos -= 1
        anArray[insertPos] = insertVal

times = []
for i in range(5):
    time1 = time.time()
    bubbleSort(randomData)
    time2 = time.time()
    print(time2-time1)
    times.append(time2 - time1)
averageTime = 0
for el in times:
    averageTime += el
averageTime /= len(times)
print(averageTime)