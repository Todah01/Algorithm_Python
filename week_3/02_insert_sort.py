input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    for i in range(len(array)):
        print(array)
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                print(array[i-j-1], array[i-j], ": change")
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            else:
                break

    return array

print(insertion_sort(input)) # [1, 2, 4, 6, 9] 가 되어야 합니다!