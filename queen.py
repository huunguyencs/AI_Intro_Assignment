import random
from math import exp
import time
from copy import deepcopy

TEMPERATURE = 4000

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
        for _ in range(pos):
            print("-", end=" ")
        print("1",end=" ")
        for _ in range(pos+1,n):
            print("-", end=" ")
        print()


def threat_calculate(n):
    '''Combination formular. It is choosing two queens in n queens'''
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2


def create_board(n):
    '''Create a chess board with a queen on a row '''
    chess_board = {}
    temp = list(range(n))
    random.shuffle(temp)  # shuffle to make sure it is random
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    del temp
    return chess_board


def cost(chess_board):
    '''Calculate how many pairs of threaten queen'''
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for column in chess_board:
        temp_m = column - chess_board[column]
        temp_a = column + chess_board[column]
        if temp_m not in m_chessboard:
            m_chessboard[temp_m] = 1
        else:
            m_chessboard[temp_m] += 1
        if temp_a not in a_chessboard:
            a_chessboard[temp_a] = 1
        else:
            a_chessboard[temp_a] += 1

    for i in m_chessboard:
        threat += threat_calculate(m_chessboard[i])
    del m_chessboard

    for i in a_chessboard:
        threat += threat_calculate(a_chessboard[i])
    del a_chessboard

    return threat


def simulated_annealing():
    '''Simulated Annealing'''



    solution_found = False
    answer = create_board(n)

    if n == 4:
        answer = {0:1,1:3,2:0,3:2}
        print_chess_board(answer)
        return True
    elif n == 3 or n == 2 or n <= 0:
        print("No solution")
        return False
    elif n == 1:
        answer = {0:0}
        print_chess_board(answer)
        return True

    # To avoid recounting when can not find a better state
    cost_answer = cost(answer)

    t = TEMPERATURE
    sch = 0.99

    while t > 0:
        t *= sch
        successor = deepcopy(answer)
        while True:
            index_1 = random.randrange(0, n - 1)
            index_2 = random.randrange(0, n - 1)
            if index_1 != index_2:
                break
        successor[index_1], successor[index_2] = successor[index_2], \
            successor[index_1]  # swap two chosen queens
        delta = cost(successor) - cost_answer
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = deepcopy(successor)
            cost_answer = cost(answer)
        if cost_answer == 0:
            solution_found = True
            print_chess_board(answer)
            break
    if solution_found is False:
        print("No solution")


def print_chess_board(board):
    '''Print the chess board'''
    for _, row in board.items():
        for _ in range(row):
            print("-", end=" ")
        print("1",end=" ")
        for _ in range(row+1,n):
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
        start = time.time()
        res = DFS()
    elif option == 2:
        start = time.time()
        res = BFS()
    elif option == 3:
        start = time.time()
        res = simulated_annealing()
        print("Runtime in second:", time.time() - start)
        return
    else:
        print("Moi nhap lai.")
        print("---------------------------------------------------------")
        solution()
    if res:
        print("\nSolution:")
        DisplayBoard()
        print("Runtime in second:", time.time() - start)
    else:
        print("No solution")



if __name__ == "__main__":

    print("---------------------------------------------------------")
    print("-                   N-Queen Problem                     -")
    print("---------------------------------------------------------")
    
    global queen
    queen = []
    solution()
    
    