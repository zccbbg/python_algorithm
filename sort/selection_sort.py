def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


if __name__ == "__main__":
    a = [10, 6, 7, 1, 2, 16, 18, 9]
    sorted_a = selection_sort(a)
    print(sorted_a)
