# array_a = [1, 2, 3, 5]
# array_b = [4, 6, 7, 8]
#
#
# def merge(array1, array2):
#     result = []
#     array1_index = 0
#     array2_index = 0
#
#     while array1_index < len(array1) and array2_index < len(array2):
#         if array1[array1_index] > array2[array2_index]:
#             result.append(array2[array2_index])
#             array2_index += 1
#         else:
#             result.append(array1[array1_index])
#             array1_index += 1
#
#     if array1_index == len(array1):
#         while array2_index < len(array2):
#             result.append(array2[array2_index])
#             array2_index += 1
#     else:
#         while array1_index < len(array1):
#             result.append(array2[array1_index])
#             array1_index += 1
#
#     return result
#
#
# print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!


array = [5, 3, 2, 1, 6, 8, 7, 4]


def merge_sort(array):
    if len(array) <= 1:
        return array

    center = (0 + len(array)) // 2
    left_array = merge_sort(array[:center])
    right_array = merge_sort(array[center:])
    print(array)
    print("left :", left_array)
    print("right :", right_array)

    return merge(left_array, right_array)


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

# K단계 시간복잡도 : 배열을 나누는 과정에서 배열의 길이 N을 배열의 길이가 1이 될때까지 2로 K번 나누기때문에, K단계까지 총 N/2^K번만큼 시행된다. 즉, K = log2N 이다.
# K단계 만큼 반복하는데, 각각의 단계는 O(N)만큼 걸린다. 즉, O(N * log2N) = O(N * logN) 만큼의 시간복잡도를 가진다.