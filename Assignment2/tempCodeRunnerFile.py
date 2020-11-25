    rand = random.randint(0,listEmploy[randEmp].numOfOrder()-1)
            order = listEmploy[randEmp].list[rand]
            listEmploy[randEmp].remove(order)
            listEmploy[minIndex].append(order)