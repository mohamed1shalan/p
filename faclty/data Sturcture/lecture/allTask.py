from libarary import *
from TimeAlgorethem import *
from Sort import *
from processinlist import *
from SearchWay import *
from balance_prefix_postfix import *
from linkedList import *
from Tree import *
from queue import *


def hello():
    print("Hello Sharks\nform here you can chose a task to RUN")
    print("task for Task 1 (calc a time for any algorethem)")
    print("task for Task 2 (calc a time for search , add , delete for (list,tuble,set,dec))")
    print("task for Task 3 (write algorethems for sort wayes)")
    print("task for Task 4 (write algorethems for search wayes)")
    print("task for Task 5 (linked list)")
    print("task for Task 6 (postfix prefix)")
    print("task for Task 7 tree (add-print)")
    print("task for Task 8 queue(add-print)")
    choise = int(
        input("Enter Number of Task(1 or 2 or 3 or 4 or 5 or 6 or 7 or 8) "))
    print("#############")
    if choise < 9 and choise >= 1:
        match choise:
            case 1:
                timeAnyAlgorethem()
            case 2:
                timeInDeferentstorage()
            case 3:
                list_sort = [1, 5, 12, 10, 78, 26, 32, 4, 7, 8, 9, 11]
                sort(list_sort).Bubble_sort()
                sort(list_sort).selction_sort()
                sort(list_sort).insertion_sort()
                sort(list_sort).merge_sort()
            case 4:
                start = 0
                End = 1000
                step = 2
                print(
                    f"Ok Sharks this are wayes of search \na defult list is have a {(End + start)/step} elemet   (form {start} to {End} ,step is 2 )\ndefult number to search is 300")
                searchWay(start, End, step)
            case 5:
                print('OK')
                x = 10
                y = 10
                print('defoult\nadd items >> 10 \nremove 10')
                choise = input(
                    'are you want to enter number of items to (add, remove) y/n ')
                if choise == "y" or choise == "Y":
                    x = int(input(('enter number of items to add')))
                    y = int(input(('enter number for items to Remove')))
                linlkedList(x, y)
                timeLinkedistEnd = time.time()
            case 6:
                fix()
            case 7:
                x = int(input("what is number of item do you want to add"))
                listtree = []
                for i in range(x):
                    listtree.append(int(input("Enter number")))
                starttime = time.time()
                for i in range(len(listtree)):
                    if i == 0:
                        root = Tree(listtree[i])
                    else:
                        root.add(listtree[i])
                root.printtree()
                print("algorethm (add,print) time is : ", time.time()-starttime)
            case 8:
                quedata = queue.stackqueu()
                itemsadd = int(input('Enter number of items : '))
                for i in range(itemsadd):
                    quedata.add(int(input(f"Enter number {i+1} : ")))
                quedata.printq()
                for i in range(itemsadd):
                    print(f"pop number {itemsadd-i} : ")
                    quedata.pop()
                    quedata.printq()

    else:
        print("This Number is biager 4 or not number")
        return hello()


hello()
