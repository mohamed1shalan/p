from sys import stdin


def input(): return stdin.readline().rstrip()


T = int(input())

tests = []
mx = 1

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    tests.append(arr)
    mx = max(mx, max(arr))

# dp[x] = أقل تكلفة لتحويل x إلى 1
dp = [0] * (mx + 1)
dp[1] = 0

for x in range(2, mx + 1):
    # العملية الأولى: إنقاص 1
    dp[x] = dp[x - 1] + 1

    d = 2
    while d * d <= x:
        if x % d == 0:
            # القسمة على d
            dp[x] = min(dp[x], d + dp[x // d])

            # القسمة على القاسم الآخر
            d2 = x // d
            if d2 != d and d2 != x:
                dp[x] = min(dp[x], d2 + dp[d])

        d += 1

    # استخدام الإنقاص فقط
    dp[x] = min(dp[x], x - 1)

for arr in tests:
    ans = 0
    for x in arr:
        ans += dp[x]
    print(ans)
