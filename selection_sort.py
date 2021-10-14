from time_check import time_check


@time_check
def selection_sort(array):
    counter = 0
    for i in range(len(array)):
        max_index = i

        for j in range(i, len(array)):
            counter += 1
            if array[j] < array[max_index]:
                max_index = j

        array[i], array[max_index] = array[max_index], array[i]

    return counter


if __name__ == '__main__':
    arr1 = [1, 2, 5, 7, 2, 1]
    print(selection_sort(arr1))
