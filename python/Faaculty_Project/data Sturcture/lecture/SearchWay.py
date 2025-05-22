from libarary import *


def searchWay(Start=0, End=1000, Step=1):
    listTest = []
    listdet = input(
        'do you want to add anather list    for(start , end , step) y/n')
    if listdet == 'y' or listdet == 'Y':
        print("Enter >> ")
        Start = int(input('Start : '))
        End = int(input("End : "))
        Step = int(input('Step >> step start form 1 : '))
    vote = input('do you want to enter number to search y/n')

    for i in range(Start, End+1, Step):
        listTest.append(i)

    if vote == 'y' or vote == 'Y':
        searchNumber = int(input("enter number"))
    else:
        searchNumber = 300
    print("#############")

    def linear():
        timesearchLinerStart = time.time()
        makeindex = 0
        for i in range(len(listTest)):
            if listTest[i] == searchNumber:
                print(
                    f"# linear Search to >> {searchNumber} is:\n====index of {searchNumber} is ==> {i}")
                makeindex = 1
                break
        if (makeindex == 0):
            print("number is not list >> linear search  ")
        print("========Algorethem time is : ",
              time.time()-timesearchLinerStart)
        print()

    def binary(listTest, l, r, searchNumber):
        timesearchbinaryStart = time.time()
        med = int((l+r)//2)
        if l == r+1 or r == l+1:
            print("number is not list >> binary search ")
        elif (l == searchNumber):
            print(
                f"# binary Search to >> {searchNumber} is:\n====index of {searchNumber} is ==> {l}")
        elif (r == searchNumber):
            print(
                f"# binary Search to >> {searchNumber} is:\n====index of {searchNumber} is ==> {r}")
        elif searchNumber == listTest[med]:
            print(
                f"# binary Search to >> {searchNumber} is:\n====index of {searchNumber} is ==> {med}")
        elif searchNumber > listTest[med]:
            return binary(listTest, med+1, r, searchNumber)
        elif searchNumber < listTest[med]:
            return binary(listTest, l, med-1, searchNumber)
        print("========Algorethem time is : ",
              time.time()-timesearchbinaryStart)
        print()

    def jump(listTest, startj, stepj, searchNumber):
        timesearchjumpStart = time.time()
        point = 0
        for i in range(startj, len(listTest), stepj):
            if searchNumber == listTest[i]:
                print(
                    f"# jomp Search to >> {searchNumber} is: \n====index of {searchNumber} is ==> {i}")
                point = 1
                break
        if (point == 0):
            for i in range(startj+1, len(listTest), stepj):
                if searchNumber == listTest[i]:
                    print(
                        f"# jomp Search to >> {searchNumber} is:)\n====index of {searchNumber} is ==> {i}")
                    point = 1
                    break
        if (point == 0):
            print("number is not list >> jump search")
        print("========Algorethem time is : ",
              time.time()-timesearchjumpStart)
        print()

    linear()
    binary(listTest, 0, len(listTest)-1, searchNumber)
    jump(listTest, 0, 2, searchNumber)
