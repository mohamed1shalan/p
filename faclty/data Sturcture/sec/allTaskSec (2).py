# task 1
print("hello Eng : Samer\nMy name is Mohamed Shalan")


def task1(n):
    result = 0
    for i in range(0, n+1):
        result += i
    return result


listTask = [11, 10, 9, 8, 7, 6]


def task2sort(listTask):
    for i in range(0, len(listTask)):
        for j in range(0, len(listTask)):
            if listTask[i] < listTask[j]:
                listTask[i], listTask[j] = listTask[j], listTask[i]
    print(listTask)
    return listTask
    # ok now to search by binary


def task2search(listTask, l, r, numberSearch):
    med = int((l+r)//2)
    if l == r+1 or r == l+1:
        print("numer is not hear")
    elif numberSearch == listTask[med]:
        print(f'index of {numberSearch} is {med}')
    elif listTask[med] > numberSearch:
        return task2search(listTask, l, med-1, numberSearch)
    elif listTask[med] < numberSearch:
        return task2search(listTask, med+1, r, numberSearch)


print('we have a 2 task')
start = input('Enter Y to start Y')
if start == 'y' or start == 'Y':
    print('Task 1')
    number = int(input("Enter Number to test  "))
    print(f'result is ==> {task1(number)}')
    print()
    print('Task 2')
    print(f'this is a result of task2 (sort) :')
    sortedData = task2sort(listTask)
    print('\nTask 2')
    print(f'Ok task2 >> Search by binary search :')
    task2search(sortedData, 0, len(listTask)-1, 8)
