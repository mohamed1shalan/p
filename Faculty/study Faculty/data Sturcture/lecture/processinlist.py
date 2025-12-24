from libarary import *


def timeInDeferentstorage():
    # list , tuple , set , dic
    print()
    list = []
    tuple = ()
    sett = set()

    dic = {}
    x = 10000
    x = int(input("enter number items to add "))
    print(
        f"======== those times\n======== (add, search , delete)\n======== in (list ,tuble ,dec,set)\n======== in this algorethon we add,delet,search a {x} nmuber\n ")
    # list
    listTimeStart = time.time()
    for i in range(x):
        list.append(i)
    print(f"Time in list to add {x} numbers is :", time.time()-listTimeStart)

    # tuple
    tupleTimeStart = time.time()
    for i in range(x):
        tuple += (i,)
    print(f"Time in tuple to add {x} numbers is :", time.time()-tupleTimeStart)

    # set
    setTimeStart = time.time()
    for i in range(x):
        sett.add(i)
    setTtimeEnd = time.time()
    print(f"Time in set to add {x} numbers is :", time.time()-setTimeStart)

    # dic
    dicTimeStart = time.time()
    for i in range(x):
        dic[i] = i
    dicTimeEnd = time.time()
    print(f"Time in dic to add {x} numbers is :", time.time() - dicTimeStart)
    print()
    # /////////////////// search
    # list
    y = 1000
    listTimeStart = time.time()
    if y in list:
        print("Search Time in list is :", time.time()-listTimeStart)

    # tuple
    # tupleTimeStart = time.time()
    # for i in range(len(tuple)):
    #     tuple[i].
    # print("Time in tuple is :", time.time()-tupleTimeStart)

    # set
    setTimeStart = time.time()
    if y in sett:
        print("Search Time in set is :", time.time()-setTimeStart)

    # dic
    dicTimeStart = time.time()
    if y in dic:
        print("Search Time in dic is :", time.time() - dicTimeStart)
    print()
    # /////////////////// delete
    # list
    listTimeStart = time.time()
    for i in range(len(list)):
        list.pop()
    print("Delete Time in list is :", time.time()-listTimeStart)

    # tuple
    # tupleTimeStart = time.time()
    # for i in range(len(tuple)):
    #     tuple[i].
    # print("Time in tuple is :", time.time()-tupleTimeStart)

    # set
    setTimeStart = time.time()
    for i in range(len(sett)):
        sett.remove(i)
    setTtimeEnd = time.time()
    print("Delete Time in set is :", time.time()-setTimeStart)

    # dic
    dicTimeStart = time.time()
    for i in range(len(dic)):
        dic.pop(i)
    dicTimeEnd = time.time()
    print("Delete Time in dic is :", time.time() - dicTimeStart)
