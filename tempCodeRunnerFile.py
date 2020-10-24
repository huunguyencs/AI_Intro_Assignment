import random, numpy, numbers, math

K_BOLTZMANN = 1.38e-23
ALPHA = 0.1

def isSafe(col):
    numOfQueen = len(queen)
    for i in range(numOfQueen):
        if (queen[i]==col) or (abs(numOfQueen-i) == abs(queen[i]-col)):
            return False
    return True

def isGoal():
    return len(queen) == n

def estimate():
    fail = 0
    for i in queen:
        if isSafe(i)==False:
            fail += 1
    return fail

def initBoard():
    for i in range(n):
        a = int(n/2) if n%2==0 else int(n/2)+1
        x = i%a
        if i < a:
            queen.append(2*x)
        else:
            queen.append(2*x+1)

def Heuristic():
    initBoard()
    if estimate() == 0:
        return True
    else:
        return False


def DisplayBoard():
    for pos in queen:
        for x in range(pos):
            print("-", end=" ")
        print("1",end=" ")
        for x in range(pos+1,n):
            print("-", end=" ")
        print()



if __name__ == "__main__":
    n = int(input("Nhap n: "))
    global queen
    queen = []
    if Heuristic():
        DisplayBoard()
    