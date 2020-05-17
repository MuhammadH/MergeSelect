import time
import math


# combines selection sort and merge sort which is faster
# than just merge sort for some value k 

# k is the list size at which merge sort will stop dividing
# and sorts the remaining list with selection sort 

# merge sort will then merge divided lists like normal


def SelectionSort (someList):
    length = len(someList)

    # start at the beginning of the unsorted list each outer loop

    for i in range(length):
        storage = i
        j = 1

        # check each element of the unsorted loop

        for j in range(length-i):
            if someList[storage] > someList[i + j]:
                storage = i + j

        # swap

        someList[i], someList[storage] = someList[storage], someList[i]
    
    return


def MergeSort (someList, kValue):
    if len(someList) > kValue:

        # make some new list

        newList1 = []
        newList2 = []

        # get mid point and split the list

        mid = len(someList)//2
        for i in range(len(someList)):
            if i < mid:
                newList1.append(someList[i])
            else:
                newList2.append(someList[i])

        # plug new lists into merge sort

        MergeSort(newList1, kValue)
        MergeSort(newList2, kValue)

        # have some large data points
        # to avoid out of range errors

        newList1.append(10000000)
        newList2.append(10000000)

        # plug newLists back into someList

        for i in range(len(someList)):
            if newList1[0] < newList2[0]:
                someList[i] = newList1[0]
                newList1.pop(0)
            else:
                someList[i] = newList2[0]
                newList2.pop(0)
    else:
        SelectionSort(someList);
    return

# make empty list

numList = []


# get and open file # CHANGE FILE NAME FOR DIFFERENT TESTS

fileName = input("please enter the name of the file, ex: randNums.txt")
numFile = open(fileName, 'r')

# read file

lines = numFile.read()

# split file and add each number to a list

linesSplit = lines.split()
for i in linesSplit:
    numList.append(int(i))

# remember to close file

numFile.close()

# because of the recursive nature of merge sort
# the timer has to be done without decoration
# to get an accurate time

print ("k value should be " + str(math.log(len(numList), 2)) + " or less")
kValue = input("please enter a k value")
kValue = int(kValue)
timeStart = time.time()
MergeSort(numList, kValue)
timeEnd = time.time()
print ("total merge select run time:", timeEnd - timeStart)



