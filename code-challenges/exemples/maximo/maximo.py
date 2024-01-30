import time

array = [11, 2, 40, 6, 800, 21, 3, -1, 400, 111, 222, 4032, 622, 8020, 211, 312, -111, 4010, 11, 2, 40, 6, 800, 21, 3, -1, 400, 111, 222, 4032, 622, 8020, 211, 312, -111, 4010]

start_time = time.time()

def maximoRec(array, n):
    if n == 1:
        return array[0]
    else:
        max = maximoRec(array, n - 1)

        if max > array[n - 1]:
            return max
        else:
            return array[n - 1]


max = maximoRec(array, len(array))

print(max)
print("------- %s TIME EXECUTION --------- " % (time.time() - start_time))
