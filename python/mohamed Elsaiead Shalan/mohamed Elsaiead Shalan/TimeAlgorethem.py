from libarary import *


def timeAnyAlgorethem():
    print("#########################")
    print(
        "======== This is a algorethem to calc a time in \n ========(function , class ,normal algorthem)\n======== to creat a pascal teriangle")
    number = int(input("enter number of line row in Pascal's triangle = "))+1
    t_def0 = time.time()

    # c1 +c2 * (n+1) + 3(c3 * n)  + c4 (n *(n+1)) + c5 n**2 +c6 n**2 + 2 * n +(n**2 -2n) + n + n
    # this is a big(n**2)

    def deff():
        list1 = [1]
        # to print all row

        for x in range(1, number):
            y = number - x
            list2 = []
            w = 0
            for z in range(w, x + 1):
                q = z
                if z == 0 or z == x:
                    if z == 2:
                        list2.insert(z, list1[0])
                    else:
                        q = 0
                        list2.insert(z, list1[0])
                else:
                    list2.insert(z, list1[q] + list1[q - 1])
            print(" " * (y), *list1)
            list1 = list2

    deff()
    t_def1 = time.time()
    # #############

    t_class0 = time.time()

    class pascal():
        list1 = [1]
        # to print all row
        #
        for x in range(1, number):
            y = number - x
            list2 = []
            w = 0
            for z in range(w, x + 1):
                q = z
                if z == 0 or z == x:
                    if z == 2:
                        list2.insert(z, list1[0])
                    else:
                        q = 0
                        list2.insert(z, list1[0])
                else:
                    list2.insert(z, list1[q] + list1[q - 1])
            print(" " * (y), *list1)
            list1 = list2

    t_class1 = time.time()
    #####################
    t_normal0 = time.time()
    list1 = [1]
    for x in range(1, number):
        y = number - x
        list2 = []
        w = 0
        for z in range(w, x + 1):
            q = z
            if z == 0 or z == x:
                if z == 2:
                    list2.insert(z, list1[0])
                else:
                    q = 0
                    list2.insert(z, list1[0])
            else:
                list2.insert(z, list1[q] + list1[q - 1])
        print(" " * (y), *list1)
        list1 = list2
    t_normal1 = time.time()
    print("##################################################")
    print('time of normal : ', t_normal1 - t_normal0)
    print('time of definition : ', t_def1 - t_def0)
    print('time of class : ', t_class1 - t_class0)
    print("##################################################")
