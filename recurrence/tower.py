# 例3.1 数塔问题

def main():
    n = 5
    a = [[0] * 101 for _ in range(101)]
    a[1][1] = 7
    a[2][1] = 3
    a[2][2] = 8
    a[3][1] = 8
    a[3][2] = 1
    a[3][3] = 0
    a[4][1] = 2
    a[4][2] = 7
    a[4][3] = 4
    a[4][4] = 4
    a[5][1] = 4
    a[5][2] = 5
    a[5][3] = 2
    a[5][4] = 6
    a[5][5] = 5

    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(f"i: {i} j: {j}")
            print(f"a[{i + 1}][{j}]: {a[i + 1][j]}")
            print(f"a[{i + 1}][{j + 1}]: {a[i + 1][j + 1]}")
            print(f"a[{i}][{j}] origin: {a[i][j]}")
            if a[i + 1][j] >= a[i + 1][j + 1]:
                a[i][j] += a[i + 1][j]
            else:
                a[i][j] += a[i + 1][j + 1]
            print(f"a[{i}][{j}] now: {a[i][j]}\n")

    print(a[1][1])

if __name__ == "__main__":
    main()
