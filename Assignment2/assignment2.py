# Add necessary libraries
import math, numpy, random, time
from functools import reduce


def distance(pos1,pos2):
    """
    Khoang cach giua 2 diem
    """
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def readInput(file_input):
    """
    pos: int - Vi tri cua kho
    M: int - So luong nhan vien
    N: int - So luong don hang
    orders: List(Order) - Danh sach cac don hang
    """
    f = open(file_input,"r")
    readline = f.readline()
    pos = [int(x) for x in readline[:-1].split(" ")]
    readline = f.readline()
    tmp = readline[:-1].split(" ")
    M = int(tmp[0])
    N = int(tmp[1])
    orders = []
    for i in range(N):
        readline = f.readline()
        tmp = [int(x) for x in readline[:-1].split(" ")]
        order = Order(i,(tmp[0],tmp[1]),tmp[2],tmp[3])
        orders.append(order)
    return pos, M, N, orders
    

class Order:
    """
    Class dai dien cho cac don hang
    id: int - chi so cua don hang
    pos: tuple(int,int) - vi tri can giao cua don hang
    vol: int - the tich cua don hang
    weigth: int - trong luong cua don hang
    """
    def __init__(self,id,pos,vol,weigth):
        self.id = id
        self.pos = pos
        self.vol = vol
        self.weigth = weigth

    def __str__(self):
        return str(self.id)

    def cost(self):
        """
        Tinh chi phi cho mot don hang
        """
        return 5 + self.vol + self.weigth * 2


class Employee:
    """
    Class dai dien cho cac nhan vien
    id: int - chi so cua nhan vien
    pos: tuple(int,int) - vi tri ban dau cua nhan vien
    list: List(Order) - danh sach chi so cua cac don hang
    profit: int - loi nhuan cua nhan vien
    sumOfDis: int - tong khoang cach di chuyen cua nhan vien
    """
    
    def __init__(self,id,list,pos):
        self.id = id
        self.pos = pos
        self.list = list

    def __getDis(self):
        """
        Tinh tong khoang cach cho toan bo don hang cua mot nhan vien
        """
        dis = distance(self.pos,self.list[0].pos)
        for i in len(self.list - 1):
            dis += distance(self.list[i].pos,self.list[i+1].pos)
        return dis

    def __calCost(self):
        """
        Tinh toan chi phi cua nhan vien
        """
        return (float(self.__getDis())/40)*20 + 10

    
    def __calRev(self):
        """
        Tinh toan doanh thu cua nhan vien
        """
        return sum([e.cost() for e in self.list])

    def getProfit(self):
        """
        Tinh toan loi nhuan cua nhan vien
        """
        return self.__calRev() - self.__calCost()


def writeOutput(file_output,out):
    """
    Viet output:
    Lay ra chuoi id order cua tung nhan vien va in ra man hinh
    """
    f = open(file_output,"w")
    for employ in out:
        out = [str(order.id) for order in employ.list]
        output = " ".join(out)
        f.write(output + "\n")



def assign(file_input, file_output):
    """
    """
    # read input
    pos, M, N, Orders = readInput(file_input)

    listEmploy = []
    for i in range(M):
        tmp = Employee(i,[],pos)
        listEmploy.append(tmp)

    ## BEGIN TEST
    listEmploy[0].list.append(Orders[3])
    listEmploy[0].list.append(Orders[4])
    listEmploy[1].list.append(Orders[0])
    listEmploy[2].list.append(Orders[2])
    listEmploy[2].list.append(Orders[1])
    ## END TEST

    ## SOLUTION
    # TODO



    #write output
    writeOutput(file_output,listEmploy)


assign('input.txt', 'output.txt')
