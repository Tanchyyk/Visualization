import numpy as np


def generate_array1(length):
    return list(np.random.randint(low=1, high=length + 1, size=length))


def generate_array2(length):
    return list(np.arange(1, length + 1, 1))


def generate_array3(length):
    return generate_array2(length)[::-1]


def generate_array4(length):
    return list(np.random.choice([1, 2, 3], size=length))
