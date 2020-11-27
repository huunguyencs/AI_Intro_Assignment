# Add necessary libraries
import numpy, random, time, math, operator
from functools import reduce
from copy import deepcopy

TEMPERATURE = 4000



def readInput(file_input):
    """
    Doc file input - return pos, M, N, orders \n
    pos: int - Vi tri cua kho \n
    M: int - So luong nhan vien \n
    N: int - So luong don hang \n
    orders: List(Order) - Danh sach cac don hang
    """
    f = open(file_input,"r")
    readline = f.readline()
    pos = [int(x) for x in readline[:-1].split(" ")]
    readline = f.readline()
    # tmp = readline[:-1].split(" ")
    # N = int(tmp[0])
    # M = int(tmp[1])
    N, M = map(int,readline.split(' '))
    orders = []
    for i in range(N):
        readline = f.readline()
        if i == N - 1:
            tmp = [int(x) for x in readline.split(' ')]
        else:
            tmp = [int(x) for x in readline[:-1].split(' ')]
        order = Order(i,(tmp[0],tmp[1]),tmp[2],tmp[3])
        orders.append(order)
    return pos, M, N, orders
    

class Order:
    """
    Class dai dien cho cac don hang - Order(id, pos, vol, weigth)\n
    id: int - chi so cua don hang \n
    pos: tuple(int,int) - vi tri can giao cua don hang \n
    vol: int - the tich cua don hang \n
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
    Class dai dien cho cac nhan vien - Employee(id, list, pos)\n
    id: int - chi so cua nhan vien \n
    list: List(Order) - danh sach chi so cua cac don hang \n
    pos: tuple(int,int) - vi tri ban dau cua nhan vien \n
    """
    
    def __init__(self,id,list,pos):
        self.id = id
        self.pos = pos
        self.list = list

    @staticmethod
    def distance(pos1,pos2):
        return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

    def __getDis(self):
        """
        Tinh tong khoang cach cho toan bo don hang cua mot nhan vien
        """
        if self.list:
            dis = Employee.distance(self.pos,self.list[0].pos)
            for i in range(len(self.list) - 1):
                dis += Employee.distance(self.list[i].pos,self.list[i+1].pos)
            return dis
        return 0

    def __calCost(self):
        """
        Tinh toan chi phi cua nhan vien
        """
        return float(self.__getDis())/2 + 10

    
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
    
    def append(self,order:Order):
        """
        Them mot order vao danh sach cua nhan vien
        """
        self.list.append(order)

    def remove(self,order:Order):
        """
        Loai bo don hang ra danh sach cua nhan vien
        """
        if order in self.list:
            self.list.remove(order)
            return True
        return False
    
    def numOfOrder(self):
        """
        So luong don hang cua nhan vien
        """
        return len(self.list)


def writeOutput(file_output,out,start,cost):
    """
    Viet output \n
    Lay ra chuoi id order cua tung nhan vien va viet vao file output
    """
    # output ra man hinh
    t = time.time() - start
    print('-'*40 +'\nTime run: ' + str(t))
    print('-'*40 +'\nOptomal: ' + str(cost))

    

    f = open(file_output,"w")
    for employ in out:
        out = [str(order.id) for order in employ.list]
        output = " ".join(out)
        f.write(output + "\n")

def randomOrder(M,N,Orders,listEmploy):
    """
    Sap xep ngau nhien order vao danh sach cua nhan vien
    """
    # TODO
    # ...
    numOrder = N
    agv = N//M
    add = N%M

    order = Orders
    random.shuffle(order)

    for i in range(M - 1):
        if add > 0:
            rand = random.random()
            if rand > 0.5:
                numOr = agv + 1
                numOrder -= (agv + 1)
                add -= 1
            else:
                numOr = agv
                numOrder -= agv
            
        else:
            numOrder = agv
        for o in order[:numOr]:
            listEmploy[i].append(o)
            order.remove(o)
        numOrder -= numOr
    for o in order:
        listEmploy[M-1].append(o)
    
        


def optimal(listEmploy):
    """
    Tinh toan luong gia cho giai thuat \n
    return: cost, chi so max, chi so min
    """
    # TODO
    # ...
    lst = [ele.getProfit() for ele in listEmploy]
    indexMax, maxValue = max(enumerate(lst), key=operator.itemgetter(1))
    indexMin, minValue = min(enumerate(lst), key=operator.itemgetter(1))
    cost  = maxValue - minValue
    return cost, indexMax, indexMin

def changeState(listEmploy,maxIndex,minIndex):
    """
    Ham chuyen doi trang thai
    """
    # TODO
    ...
    if listEmploy[maxIndex].numOfOrder() > 1:
        rand = random.randint(0,listEmploy[maxIndex].numOfOrder()-1)
        order = listEmploy[maxIndex].list[rand]
        listEmploy[maxIndex].remove(order)
        listEmploy[minIndex].append(order)
        return True
    else:
        randEmp = -1
        i = 0
        while randEmp < 0 or listEmploy[randEmp].numOfOrder() > 1:
            randEmp = random.randint(0,len(listEmploy) - 1)
            i += 1
            if i > 1000:
                break
        if listEmploy[randEmp].numOfOrder() > 1:
            rand = random.randint(0,listEmploy[randEmp].numOfOrder()-1)
            order = listEmploy[randEmp].list[rand]
            listEmploy[randEmp].remove(order)
            listEmploy[minIndex].append(order)
        return True

    return False


def checkExit(listEmploy,M,N):
    """
    Kiem tra dieu kien dung
    """
    lst = [ele.getProfit()<=1.e-2 for ele in listEmploy]
    if any(lst):
        return False
    return True



def simulated_annealing(pos,M,N,Orders,listEmploy):
    """
    Phuong phap toi luyen mo phong \n
    pos: int - Vi tri cua kho \n
    M: int - So luong nhan vien \n
    N: int - So luong don hang \n
    Orders: List(Order) - Danh sach cac don hang \n
    listEmploy: List(Employee) - Danh sach cac nhan vien
    """

    # TODO
    # ...
    randomOrder(M,N,Orders,listEmploy)
    opt, iMax, iMin = optimal(listEmploy)
    t = TEMPERATURE
    sch = 0.99
    if N == M:
        return opt
    while t > 1.e-200 or (not checkExit(listEmploy,M,N)):
        t *= sch
        newState = listEmploy.copy()

        # change state for new state
        if not changeState(newState,iMax,iMin):
            break

        newOpt = optimal(newState)
        delta = newOpt[0] - opt

        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / t):
            listEmploy = newState.copy()
            opt, iMax, iMin = newOpt
        if opt < 5:
            break
    return opt





def assign(file_input, file_output):
    """
    Thuc hien chuc nang chinh trong chuong trinh
    """
    start = time.time()
    # read input
    pos, M, N, Orders = readInput(file_input)

    listEmploy = []
    for i in range(M):
        tmp = Employee(i,[],pos)
        listEmploy.append(tmp)

    ## BEGIN TEST
    # listEmploy[0].append(Orders[1])
    # listEmploy[1].append(Orders[0])
    # listEmploy[2].append(Orders[2])
    # listEmploy[2].append(Orders[3])
    ## END TEST

    ## SOLUTION
    # TODO
    cost = simulated_annealing(pos,M,N,Orders,listEmploy)
    # ...

    lst = [ele.getProfit() for ele in listEmploy]
    print(lst)
    

    #write output
    writeOutput(file_output,listEmploy,start,cost)

if __name__ == "__main__":
    assign('input.txt', 'output.txt')


