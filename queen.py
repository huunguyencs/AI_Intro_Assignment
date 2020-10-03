import numpy

global n
global queen

def isSafe(col):
    numOfQueen = len(queen)
    for i in range(numOfQueen):
        if (queen[i]==col) or (abs(numOfQueen-i) == abs(queen[i]-col)):
            return False
    return True

def BFS():
    pass

def DFS():
    pass

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
    queen = [0,1,2,3]

    DisplayBoard()

    