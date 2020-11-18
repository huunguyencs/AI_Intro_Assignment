from copy import deepcopy

def test(lst):
    lst[0] = 5
    lst[1] = 7

lst = [1,7,8,9,2,4,5,6,4,3]

a = deepcopy()


a = lst
print(a)