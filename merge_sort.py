from time_check import time_check


@time_check
def merge_sort(array):
    counter = 0
    if len(array) > 1:
        mid_element = len(array) // 2
        left_side = array[:mid_element]
        right_side = array[mid_element:]

        merge_sort(left_side)
        merge_sort(right_side)

        i = j = k = 0

        while i < len(left_side) and j < len(right_side):
            counter += 1
            if left_side[i] < right_side[j]:
                counter += 1
                array[k] = left_side[i]
                i += 1
            else:
                array[k] = right_side[j]
                j += 1
            k += 1

        while i < len(left_side):
            counter += 1
            array[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            counter += 1
            array[k] = right_side[j]
            j += 1
            k += 1

    return counter


if __name__ == '__main__':
    arr1 = [1, 2, 5, 7, 2, 1]
    print(merge_sort(arr1))
