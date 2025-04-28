import math
done = 0


def prim1(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n)+4), 1):
        if n % i == 0:
            return False
    return True


for i in range(int(input())):
    A, B = map(int, input().split())
    A_test = A
    B_test = B
    step = 0
    done = 0
    is_prime = 0
    if A == B:
        print(0)
    else:
        for j in range(2, B+1, 1):
            while (True):
                if A_test/j > B_test*j:
                    A_test /= j
                    B_test *= j
                    step += 1
                elif A_test/j == B_test*j:
                    step += 1
                    is_prime = prim1(j)
                    if is_prime == True:
                        done = 1
                        break
                    else:
                        break
                elif A_test/j < B_test*j:
                    done = 0
                    break
            if done == 1:
                print(step)
            else:
                print(-1)
            step = 0
            done = 0
            break
