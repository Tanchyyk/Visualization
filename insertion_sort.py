from time_check import time_check


@time_check
def insertion_sort(array):
    counter = 0
    for i in range(1, len(array)):
        current_el = array[i]
        j = i - 1

        counter += 1
        while j >= 0 and current_el < array[j]:
            counter += 1
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_el

    return counter


if __name__ == '__main__':
    arr1 = [1, 2, 5, 7, 2, 1]
    print(insertion_sort(arr1))
