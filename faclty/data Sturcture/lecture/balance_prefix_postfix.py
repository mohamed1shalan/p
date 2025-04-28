from libarary import *


def fix():
    print("to prefix and postfix")
    infix = input("Enter :")

    def balance(eq):
        balance_time = time.time()
        print('balance ckeck : ')
        balancechick = list(eq)
        listoperator = []
        for i in balancechick:
            if i == '(':
                listoperator.append(i)
            elif i == ')':
                for j in range(len(listoperator)-1, -1, -1):
                    if listoperator[j] == ')':
                        continue
                    else:
                        listoperator.pop(j)
                        break
        if len(listoperator) == 0:
            print('it is balance')
        else:
            print('it isnot balance')
        print("balance time AnyAlgorethem", time.time() - balance_time)

    def postfix(eq):
        postfix_time = time.time()
        print('postfix : ')
        orignal = list(eq)
        listoperation = []
        listresult = []
        for i in orignal:
            if (len(listoperation)-1) == "/" or (len(listoperation)-1) == "*":
                for i in range(len(listoperation)):
                    listresult.append(listoperation.pop())
                listoperation.append(i)
            elif i == "(":
                listoperation.append(i)
            elif i == ")":

                for j in range(len(listoperation)-1, -1, -1):
                    if listoperation[j] == '(':
                        listoperation.pop()
                        break
                    else:
                        listresult.append(listoperation.pop())
            elif i == "+" or i == "-":
                listoperation.append(i)
            elif i == "*" or i == "/":
                if (len(listoperation)-1) == "/" or (len(listoperation)-1) == "*":
                    for i in range(len(listoperation)):
                        listresult.append(listoperation.pop())
                listoperation.append(i)
            else:
                listresult.append(i)

        if len(listoperation) > 0:
            for j in range(len(listoperation)):
                listresult.append(listoperation.pop())
        print(*listresult, sep="")
        print("postfix time AnyAlgorethem", time.time() - postfix_time)

    def prefix(eq):
        prefix_time = time.time()
        print('prefix : ')
        orcreat = list(eq)
        test = []
        final_result = []
        listoperationcraert = ['*', '/', '+', '-']
        for i in range(len(orcreat)-1):
            if orcreat[i] == '(' or orcreat[i] == ')':
                final_result.append(orcreat[i])
                test = []
                continue
            if orcreat[i] in listoperationcraert:
                test.insert(0, orcreat[i])
                if orcreat[i] not in listoperationcraert:
                    test.append(orcreat[i])
                elif ((orcreat[i] in listoperationcraert) or i == (len(orcreat)-1)):
                    if (i <= len(orcreat)+1):
                        if (orcreat[i+1] not in listoperationcraert) and (orcreat[i+1] != ')' and orcreat[i+1] != '('):
                            test.append(orcreat[i+1])
                            orcreat.pop(i+1)
                    cur = ''
                    for j in test:
                        cur += j
                    final_result.append(cur)
                    test.clear()
                    cur = ''
                    test = []
                    i += 1
            else:
                test.append(orcreat[i])
        if len(test) != 0:
            cur = ''
            for i in test:
                cur += i
            final_result.append(cur)
            test = []
        print(*final_result, sep='')
        print("prefix time AnyAlgorethem", time.time() - prefix_time)
    balance(infix)
    print()
    prefix(infix)
    print()
    postfix(infix)
