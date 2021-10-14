import numpy as np
import pandas as pd
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from shell_sort import shell_sort
from array_generation import generate_array1, generate_array2, generate_array3, generate_array4


def count_statistics(sorting_fn, generating_fn, n_experiments, length):
    time_list, compare_operations_list = [], []

    for _ in range(n_experiments):
        arr = generating_fn(length)
        statistics = sorting_fn(arr)

        time_list.append(statistics["time"])
        compare_operations_list.append(statistics["compare_operations"])

    return sum(time_list) / n_experiments, sum(compare_operations_list) / n_experiments


if __name__ == '__main__':
    # make experiment deterministic
    np.random.seed(42)

    # define array sizes
    min_power, max_power = 7, 14
    lengths = [2 ** i for i in range(min_power, max_power + 1)]

    # stack array-generating functions along with number of experiments
    generating_fns = [(generate_array1, 5), (generate_array2, 1), (generate_array3, 1), (generate_array4, 3)]

    # create array of sorting functions
    sorting_fns = [(insertion_sort, "insertion_sort"), (selection_sort, "selection_sort"), (merge_sort, "merge_sort"),
                   (shell_sort, "shell_sort")]

    # measure time
    results = []

    for sorting_fn, algorithm_name in sorting_fns:
        for i, (generating_fn, n_experiments) in enumerate(generating_fns):
            for length in lengths:
                results.append((algorithm_name, f"experiment{i}", length,
                                *count_statistics(sorting_fn, generating_fn, n_experiments, length)))

    df = pd.DataFrame(results, columns=["algorithm_name", "experiment", "array_length", "time", "compare_operations"])

    # save results
    df.to_csv("statistics.csv", index=False)
