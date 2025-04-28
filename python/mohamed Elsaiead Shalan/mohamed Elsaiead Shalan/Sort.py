from libarary import *


class sort:
    def __init__(self, list):
        self.list = list

    def Bubble_sort(self):
        time_bubble_sort = time.time()
        for j in range(len(self.list)-1):
            for i in range(len(self.list)-1):
                if self.list[i] > self.list[i+1]:
                    self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
        print(self.list)
        print("Algorethm Bubble_sort time is ", time.time()-time_bubble_sort)
        print()

    def selction_sort(self):
        time_selction_sort = time.time()
        for j in range(len(self.list)):
            min = self.list[j]
            items = 0
            for i in range(j+1, len(self.list)):
                if self.list[j] > self.list[i]:
                    if min > self.list[i]:
                        min = self.list[i]
                        items = i
            if self.list[j] > self.list[items] and items != 0:
                self.list[j], self.list[items] = self.list[items], self.list[j]
        print(self.list)
        print("Algorethm selction_sort time is ",
              time.time()-time_selction_sort)
        print()

    def insertion_sort(self):
        time_insertion_sort = time.time()
        sort_list = []
        for i in range(len(self.list)):
            sort_list.append(self.list[i])
            if len(sort_list) < 2:
                continue
            else:
                for j in range(i, 0, -1):
                    if sort_list[j] < sort_list[j-1]:
                        sort_list[j], sort_list[j -
                                                1] = sort_list[j-1], sort_list[j]
        print(sort_list)
        print("Algorethm insertion_sort time is ",
              time.time()-time_insertion_sort)
        print()

    def merge_sort(self):
        time_merge_sort = time.time()
        orignal = self.list

        def split(orignal, sort1, sort2, sort3, sort4):

            med = len(orignal)//2
            if len(orignal) <= 3:
                for i in range(len(orignal)):
                    m1 = orignal.index(min(orignal))
                    sort3.append(orignal.pop(m1))
                return sort3
            elif len(orignal) > 3:
                sort1 = split(orignal[0:med], [], [], [], [])
                sort2 = split(orignal[med:], [], [], [], [])
                for i in range(len(sort1)+len(sort2)):
                    m3 = min(sort1+sort2)
                    sort4.append(m3)
                    if m3 in sort1:
                        m1 = sort1.index(min(sort1))
                        sort1.pop(m1)
                    else:
                        m2 = sort2.index(min(sort2))
                        sort2.pop(m2)
            return sort4
        print(split(orignal, [], [], [], []))
        print("Algorethm merge_sort time is ",
              time.time()-time_merge_sort)
        print()
