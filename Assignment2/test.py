from functools import reduce

M = [1,2,3,7,8]

print(reduce(lambda x,y: x + y,M,0))