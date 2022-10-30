def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        middle = (low + high) // 2
        if (input_array[middle] == value):
            return middle
        elif (input_array[middle] < value):
            low = middle + 1
        else:
            high = middle - 1
    return -1

print(binary_search([1,2,3,5,6,7,8,9,11,12,17,67,75,89,99], 11))