from libarary import *


def linlkedList(choiseStart, choiseEnd):
    linkedListTimeStart = time.time()

    def linearlinked(choiseStart, choiseEnd):
        class linear:
            def __init__(self, value):
                self.value = value
                self.next = None
                self.items = 1

        class stack:
            def __init__(self):
                self.head = linear("value")

            def push(self, value):
                node = linear(value)
                if self.head.items != 1:
                    node.next = self.head.next.next
                    self.head.next.next = node
                    self.head.next = node
                else:
                    self.head.next = node
                    node.next = node
                self.head.items += 1

            def print(self):
                print()
                print("add to inverse Linear LinkedList")
                pointer = self.head.next.next
                cout = ''
                for i in range(self.head.items-1):
                    cout += f" + {pointer.value}"
                    pointer = pointer.next
                return cout

            def IsEmpyt(self):
                if self.head.items == 1:
                    print("it is Empty")
                else:
                    print("it isnot Empty")

            def calcitems(self):
                print(f"number of items is {self.head.items-1}")
        Stack = stack()
        timeLinkedistStart = time.time()
        for i in range(choiseStart):
            Stack.push(i)
        print(Stack.print())
        Stack.calcitems()
        Stack.IsEmpyt()
        print('Time Algorthem linear linkedList is ',
              (time.time() - timeLinkedistStart))
    linearlinked(choiseStart, choiseEnd)

    def circule_linear(choiseStart, choiseEnd):
        class circule:
            def __init__(self, value):
                self.value = value
                self.next = None
                self.head = None

        class stack:
            def __init__(self):
                self.stander = circule("head")
                self.stander.head = self.stander
                self.items = 0

            def push(self, value):
                node = circule(value)
                node.next = self.stander
                node.head = self.stander.head
                self.stander.head.next = node
                self.stander.head = node
                self.items += 1

            def print(self):
                pointer = self.stander.next
                pointerinverse = self.stander.head
                cirlist = ''
                cirlistinverse = ''
                for i in range(self.items):
                    cirlist += f" + {pointer.value}"
                    pointer = pointer.next

                for i in range(self.items):
                    cirlistinverse += f" + {pointerinverse.value}"
                    pointerinverse = pointerinverse.head
                print(f"normal  {cirlist}")
                print(f"inverse {cirlistinverse}")

            def IsEmpty(self):
                if self.items == 0:
                    print("it is Empty")
                else:
                    print("it is not Empty")

            def calcitlem(self):
                print(f'items is {self.items-1}')

            def poplast(self, choiseEnd):
                print()
                print(f"-------remove {choiseEnd} from last")
                for i in range(choiseEnd):
                    self.stander.head = self.stander.head.head
                    self.stander.head.next.next = None
                    self.stander.head.next.head = None
                    self.stander.head.next = self.stander
                    self.items -= 1

        Stack = stack()
        timeLinkedistStartc = time.time()
        print()
        print("add last in circule LinkedList")
        for i in range(choiseStart):
            Stack.push(i)
        Stack.print()
        Stack.poplast(choiseEnd)
        Stack.IsEmpty()
        Stack.print()
        Stack.calcitlem()
        print('Time Algorthem linear linkedList is :',
              (time.time() - timeLinkedistStartc))

    circule_linear(choiseStart, choiseEnd)
