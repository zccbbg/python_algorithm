# 例3.2 斐波那契数列
def fibonacci(n):
    f0, f1 = 1, 1
    print(f0, f1, end=" ")
    for i in range(3, n + 1):
        f2 = f0 + f1
        print(f2, end=" ")
        f0, f1 = f1, f2

n = 20
fibonacci(n)
