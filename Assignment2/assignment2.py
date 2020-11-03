# Them cac thu vien neu can
import math, numpy, random, time
from functools import reduce

global pos
global M, N
global orders
global employees

def cong(theTich,trongLuong):
    """ """
    return 5 + theTich + trongLuong*2

def chiPhi(tongKhoangCach,employee):
    """Calculate the total cost"""
    return (tongKhoangCach/40)*20 + 10

def distance(pos1,pos2):
    """Distance between two point"""
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def doanhThu(tongCong):
    """ """
    return reduce(lambda x,y: x + y,tongCong,0)

def loiNhuan(employee):
    pass

def readInput(file_input):
    """ """
    f = open(file_input,"r")
    readline = f.readline()
    pos = [int(x) for x in readline[:-1].split(" ")]
    readline = f.readline()
    tmp = readline[:-1].split(" ")
    M = int(tmp[0])
    N = int(tmp[1])
    orders = []
    for _ in range(N):
        readline = f.readline()
        orders += [[int(x) for x in readline[:-1].split(" ")]]
    
    # print(pos)
    # print(str(M))
    # print(str(N))
    # print(orders)

def algorithm():
    """ """
    pass

def writeOutput(file_output,out):
    """ """
    f = open(file_output,"w")
    for employ in out:
        for e in employ:
            f.write(str(e)+ " ")
        f.write("\n")



def assign(file_input, file_output):
    # read input
    readInput(file_input)
    # run algorithm
    employees = [[0,3],[4],[2,1]]
    # write output
    writeOutput(file_output,employees)
    return


assign('input.txt', 'output.txt')
