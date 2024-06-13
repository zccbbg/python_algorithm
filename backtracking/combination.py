# 例5.2
num = 0
a = [0] * 10001
b = [False] * 10001
n = 5
r = 4

def search(k):
    global num
    for i in range(1, n + 1):
        if not b[i]:
            a[k] = i
            b[i] = True
            if k == r:
                print_combination()
            else:
                search(k + 1)
            b[i] = False

def print_combination():
    global num
    num += 1
    for i in range(1, r + 1):
        print(f"{a[i]:3}", end='')
    print()

if __name__ == "__main__":
    search(1)
    print(f"number={num}")
