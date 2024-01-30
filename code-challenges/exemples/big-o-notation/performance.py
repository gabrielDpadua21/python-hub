import time

size = int(input("Determinate the array size: "))

a = []

for index in range(size):
    a.append(index)


start_time = time.time()

def function1(array):
    print(1 + array[0]);



def function2(array):
    sumArray = 0
    for number in array:
        sumArray += number;
        print(sumArray)


def function3(array):
    for number in array:
        for index in array:
            print(str(number) + ', ' + str(index))
            print("/")
        print("//")


function1(a)

print("------- %s TIME EXECUTION --------- " % (time.time() - start_time))




