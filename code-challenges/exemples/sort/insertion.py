import time

array = [11, 2, 40, 6, 800, 21, 3, -1, 400, 111, 222, 4032, 622, 8020, 211, 312, -111, 4010, 11, 2, 40, 6, 800, 21, 3, -1, 400, 111, 222, 4032, 622, 8020, 211, 312, -111, 4010]


def sort(array):
    for j in range(len(array)):
        key = array[j]
        i = j - 1

        while i >= 1 and array[i] > key:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key


sort(array)

print(array)