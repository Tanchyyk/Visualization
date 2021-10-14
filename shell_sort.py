from time_check import time_check


@time_check
def shell_sort(array):
    arr_len = len(array)
    mid_index = arr_len // 2

    counter = 0
    while mid_index > 0:
        for i in range(mid_index, arr_len):
            temp_el = array[i]
            j = i
            counter += 1
            while j >= mid_index and array[j - mid_index] > temp_el:
                counter += 1
                array[j] = array[j - mid_index]
                j -= mid_index

            array[j] = temp_el
        mid_index = mid_index // 2

    return counter


if __name__ == '__main__':
    arr1 = [1, 2, 5, 7, 2, 1]
    print(shell_sort(arr1))
