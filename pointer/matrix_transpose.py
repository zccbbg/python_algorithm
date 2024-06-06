# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def matrix_transpose():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]

    # 获取原矩阵的行数和列数
    rows = len(matrix)
    cols = len(matrix[0])

    # 创建一个新矩阵来存储转置结果
    transpose = [[0] * rows for _ in range(cols)]

    # 转置矩阵
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    # 打印转置矩阵
    for i in range(cols):
        for j in range(rows):
            print(transpose[i][j], end=" ")
        print()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix_transpose()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
