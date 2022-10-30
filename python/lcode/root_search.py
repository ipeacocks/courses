# def root_search(x):
#     list = range(x)
#     low = 0 
#     high = len(list) - 1

#     while low <= high:
#         middle = (low + high) // 2
#         second_power = list[middle] * list[middle]
#         if second_power == x:
#             return list[high]
#         elif second_power < x:
#             low = middle + 1
#         elif second_power > x:
#             high = middle - 1
#     return list[high]

"""
y is the number you want to find the square root of
then the question becomes solving f(x) = x**2 - y = 0 for x.
newton's method: iterate new_x = x - f(x)/f'(x). 
f'(x) = 2x
therefore, new_x = x - (x**2 - y)/(2x).
"""

def root_search(y):
    prevx = -1
    newx = 1
    while abs(newx - prevx) > 1e-10:
        prevx = newx
        newx = prevx - (prevx**2 - y)/ (2*prevx)

    return int(newx)

print(root_search(63))

