import numpy, datetime

# Check queen is safe
def isSafe(col):
    numOfQueen = len(queen)
    for i in range(numOfQueen):
        if (queen[i]==col) or (abs(numOfQueen-i) == abs(queen[i]-col)):
            return False
    return True

# Place queen in the board
def place(pos):
    if pos>=0 and pos<n:
        queen.append(pos)
# Unplace queen out the board
def unplace():
    if len(queen) > 0:
        queen.pop(len(queen)-1)
# Check is the goal of algorithm
def isGoal():
    return len(queen) == n

# Breadth First Search algorithm
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

# Depth First Search algorithm
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

# Heurisric algorithm
def Heuristic():
    return False

# Display chess board to screen
def DisplayBoard():
    for pos in queen:
        for x in range(pos):
            print("-", end=" ")
        print("1",end=" ")
        for x in range(pos+1,n):
            print("-", end=" ")
        print()

def solution():
    
    res = False
    global n
    global option
    print("Nhap lua chon giai thuat:")
    print("1. DFS")
    print("2. BFS")
    print("3. Heuristic")
    option = int(input("Nhap: "))
    n = int(input("Input n: "))
    if option == 1:
        start = datetime.datetime.now()
        res = DFS()
        end = datetime.datetime.now()
    elif option == 2:
        start = datetime.datetime.now()
        res = BFS()
        end = datetime.datetime.now()
    elif option == 3:
        start = datetime.datetime.now()
        res = Heuristic()
        end = datetime.datetime.now()
    else:
        print("Moi nhap lai.")
        print("---------------------------------------------------------")
        solution()
    if res:
        print("\nSolution:")
        DisplayBoard()
        print("Time: " + str(end-start))
    else:
        print("No solution")



if __name__ == "__main__":

    print("---------------------------------------------------------")
    print("-                   N-Queen Problem                     -")
    print("---------------------------------------------------------")
    
    global queen
    queen = []
    solution()
    
    