import numpy

global n
global queen

def isSafe(col):
    numOfQueen = len(queen)
    for i in range(numOfQueen):
        if (queen[i]==col) or (abs(numOfQueen-i) == abs(queen[i]-col)):
            return False
    return True

def place(pos):
    if pos>=0 and pos<n:
        queen.append(pos)

def unplace():
    if len(queen) > 0:
        queen.pop(len(queen)-1)

def isGoal():
    return len(queen) == n


def BFS():
    pass


def DFS():
    if isGoal():
        return True
    else:
        for i in range(n):
            if isSafe(i):
                place(i)
                res = DFS()
                if res:
                    return res
                unplace()
    return False

def Heuristic():
    pass

def DisplayBoard():
    for pos in queen:
        for x in range(pos):
            print("0", end=" ")
        print("1",end=" ")
        for x in range(pos+1,n):
            print("0", end=" ")
        print()



if __name__ == "__main__":

    n = int(input("Input n: "))

    # Init queen array
    queen = []
    DFS()
    DisplayBoard()

    