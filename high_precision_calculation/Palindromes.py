def init(a):
    s = "921"
    a.clear()
    a.extend(map(int, s[::-1]))

def check(a):
    return a == a[::-1]

def jia(a):
    b = a[::-1]
    carry = 0
    for i in range(len(a)):
        a[i] += b[i] + carry
        carry = a[i] // 10
        a[i] %= 10
    if carry:
        a.append(carry)

def print_array(a):
    size = len(a)
    print("size:", size)
    print(" ".join(map(str, a)))

if __name__ == "__main__":
    a = []
    init(a)
    print("init:")
    print_array(a)

    if check(a):
        print(0)
    else:
        ans = 0
        while ans <= 30:
            ans += 1
            jia(a)
            print(f"Test: {ans}  ", end="")
            print_array(a)
            if check(a):
                print(ans)
                break
        else:
            print("impossible")
