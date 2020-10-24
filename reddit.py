import random

def configureRandomly():
    for i in range(n):
        x = int(random.randrange(0,n))
        queen.append(x)

def DisplayBoard():
    for pos in queen:
        for x in range(pos):
            print("-", end=" ")
        print("1",end=" ")
        for x in range(pos+1,n):
            print("-", end=" ")
        print()

def compareStates(state1,state2):
    for i in range(n):
        if state1[i] != state2[i]:
            return False
    return True

def fill(pos):
    for i in range(n):
        queen[i] = pos

def calculateObject():
    attacking  = 0
    row = col = 0
    for i in range(n):
        row = sta

if __name__ == "__main__":
    global n
    global queen

    n = int(input("Nhap n: "))
    queen = []