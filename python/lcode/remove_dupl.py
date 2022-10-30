# a = [1,1,1,2,3,3]
# b = []

# for i in range(len(a)):
#     if a[i] != a[i-1]:
#         b.append(a[i])
# print(b)

# a = [1,1,1,2,3,3]
# b = [a[0]]

# a_prev = a[0]

# for i in range(1, len(a)):
#     if a[i] != a_prev:
#         b.append(a[i])
#     a_prev = a[i]
# print(b)


a = [1,1,1,2,2,2,2,2,3,3]
a_prev = a[0]
b = [a[0]]

for i in a[1:]:
    if a_prev != i:
        b.append(i)
    a_prev = i
print(b)