import math
# 例5.1 素数环
b = [0] * 11
total = 0
a = [0] * 11

def search(t):
    global total
    for i in range(1, 11):
        if pd(a[t - 1], i) and not b[i]:
            a[t] = i
            b[i] = 1
            if t == 10:
                if pd(a[10], a[1]):
                    print_solution()
            else:
                search(t + 1)
            b[i] = 0

def print_solution():
    global total
    total += 1
    print(f"<{total}>", end=" ")
    for j in range(1, 11):
        print(a[j], end=" ")
    print()

def pd(x, y):
    i = x + y
    k = 2
    while k <= math.sqrt(i) and i % k != 0:
        k += 1
    return k > math.sqrt(i)

if __name__ == "__main__":
    search(1)
    print(total)
