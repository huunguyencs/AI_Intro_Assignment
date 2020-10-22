import numpy, datetime


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
    global queen
    global queue
    queen = []
    queue = []
    for i in range(n):
        queue.append([i])
    while len(queue) != 0:
        queen = queue.pop(0)
        if isGoal():
            return True
        for i in range(n):
            if isSafe(i):
                temp = queen + [i]
                try:
                    queue.index(temp)
                except:
                    queue.append(temp)
        # print(queue)
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
    global n
    n = int(input("Nhap n: "))
    

    if BFS():
        DisplayBoard()
    else:
        print("No Solution")

    

