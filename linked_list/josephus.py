def josephus(n, k):
    people = list(range(1, n + 1))
    index = 0

    print("约瑟夫环问题解决方案:")
    while len(people) > 0:
        index = (index + k - 1) % len(people)
        print("出局的人:", people.pop(index))



if __name__ == '__main__':
    n = 8  # 8个人
    k = 5  # 报数为5
    josephus(n, k)
