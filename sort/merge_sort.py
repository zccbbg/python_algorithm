# Created by zccbbg on 2024-06-06

a = [0, 10, 6, 7, 10, 2, 16, 18, 9]  # 输入数组，a[0] 不使用
r = [0] * 101  # 辅助数组，初始化为0


def msort(start, end):
    if start == end:
        return

    mid = (start + end) // 2

    msort(start, mid)  # 分解左序列
    msort(mid + 1, end)  # 分解右序列
    print(f"start: {start} mid: {mid} end: {end}")

    inner_start = start
    inner_mid = mid + 1
    k = start  # 接下来合并
    print(f"inner start: {inner_start} inner mid: {inner_mid} k: {k}")

    while inner_start <= mid and inner_mid <= end:
        if a[inner_start] <= a[inner_mid]:
            r[k] = a[inner_start]
            k += 1
            inner_start += 1
        else:
            r[k] = a[inner_mid]
            k += 1
            inner_mid += 1

    while inner_start <= mid:
        r[k] = a[inner_start]
        k += 1
        inner_start += 1

    while inner_mid <= end:
        r[k] = a[inner_mid]
        k += 1
        inner_mid += 1

    print("after inner sort:", end=" ")
    for i in range(start, end + 1):
        a[i] = r[i]
        print(a[i], end=" ")
    print()
    print()


def main():
    n = 8
    msort(1, n)
    print("after sort:")
    for z in range(1, n + 1):
        print(a[z], end=" ")
    print()


if __name__ == "__main__":
    main()
