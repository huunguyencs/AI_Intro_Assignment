# import random

# lst = [1,2,3,4,5,6,7,8,9]
# l = []
# random.shuffle(lst)
# M = 4
# N = 9
# for i in range(M - 1):
#     x = random.randint(1,N-(M-i)+1)
#     print(x)
#     le = []
#     for i in lst[:x]:
#         le.append(i)
#         lst.remove(i)
#     l.append(le)
#     N -= x
# le = []
# print(N)
# for i in lst[:N]:
#     le.append(i)
#     lst.remove(i)
# l.append(le)


# print(l)

import operator, random

# lst = [1,4,5,7,9,9,1,4,6,7,7]
# indexMax, maxValue = max(enumerate(lst), key=operator.itemgetter(1))
# indexMin, minValue = min(enumerate(lst), key=operator.itemgetter(1))


# print(indexMax, indexMin , maxValue, minValue)

lst = [1,5,7,8,9,7,-3]

l = [e < 0 for e in lst]

print(l)

if any(l):
    print("True")
else:
    print("False")

