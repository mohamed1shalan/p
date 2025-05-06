w1 = w2 = b = 0


def wighit_in_habb(old, x, y):
    return old + x * y


def bais_in_habb(old, y):
    return old + y


def learn_habb(w1, w2, b):
    w1 = wighit_in_habb(w1, x1, y)
    w2 = wighit_in_habb(w2, x2, y)
    b = bais_in_habb(b, y)
    print(f"w1: {w1}, w2: {w2}, b: {b}")
    return w1, w2, b


AND = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, -1)]
for x1, x2, y in AND:
    w1, w2, b = learn_habb(w1, w2, b)

print("Final weights and bias:")
