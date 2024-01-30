array = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 23, 45, 123, 321]


def binary_search(element, array):
    min = 0
    max = len(array) - 1
    print(min)
    print(max)
    middle = 0

    while min <= max:
        middle = (min + max) // 2

        if element > array[middle]:
            min = middle + 1
        elif element < array[middle]:
            max = middle - 1
        else:
            print("I founded: ", array[middle])
            return
        middle = int((min + max) / 2)
        print("min: ", min)
        print("max: ", max)
        print("middle: ", middle)

    
binary_search(23, array)
        
            
