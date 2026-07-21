# استيراد stdin و stdout للإدخال والإخراج السريع
from collections import deque, defaultdict
from numpy import array
from sys import stdin, stdout
# استبدال input() بالإصدار الأسرع
def input(): return stdin.buffer.readline().decode().rstrip()
# استيراد deque و defaultdict

# ==========================
# ============================================
# deque
# ============================================


# deque أسرع من list في الإضافة والحذف من البداية
q = deque()

# إضافة في آخر الـ deque
q.append(10)
q.append(20)

arr = array.array('i', [1, 2, 3, 4, 5])
# إضافة في أول الـ deque
q.appendleft(5)

print("\nAfter append:", q)
# deque([5, 10, 20])

# حذف من النهاية
q.pop()

print("After pop:", q)
# deque([5, 10])

# حذف من البداية
q.popleft()

print("After popleft:", q)
# deque([10])

# ============================================
# defaultdict
# ============================================

# defaultdict(int)
# أي مفتاح غير موجود قيمته الافتراضية 0
freq = defaultdict(int)

# زيادة عداد العناصر
freq["apple"] += 1
freq["banana"] += 1
freq["apple"] += 1

print("\nFrequency Dictionary:")
print(freq)

# لو المفتاح غير موجود لن يحدث Error
print(freq["orange"])     # 0

# ============================================
# stdout
# ============================================

# stdout.write لا يضيف سطر جديد تلقائياً
stdout.write("\nPrinting using stdout.write()\n")
