from operator import index
from random import randint


def findSmallest(array):
    smallestNumber = array[0]
    smallestIndex = 0

    for i in range(1, len(array)):
        if array[i] < smallestNumber:
            smallestNumber = array[i]
            smallestIndex = i
    return smallestIndex


def sortHighest(array):
    largestnumber = array[0]
    n_index = 0
    for i in range(1, len(array)):
        if array[i] > largestnumber:
            largestnumber = array[i]
            n_index = i
    return n_index


def selectionSort(array):
    sorted_array = []
    for num in range(0, len(array)):
        number = findSmallest(array)
        sorted_array.append(array.pop(number))
    return sorted_array


def selectionHighSort(array):
    sorted_array = []
    for num in range(0, len(array)):
        number = sortHighest(array)
        sorted_array.append(array.pop(number))
    return sorted_array


random_array = []

for i in range(0, 20):
    random_array.append(randint(0, 1000))

new_array = selectionSort(random_array)
print(new_array)
print(selectionHighSort(new_array))
