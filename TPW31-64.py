import numpy as np


def compare(size1, max1, size2, max2):
    a = np.random.randint(0, max1, size1)
    b = np.random.randint(0, max2, size2)
    c = [value for value in a if value in b]

    print(a, b)

    if len(c) == 0:
        print(c, "совпадений нет")
    else:
        print(c)


compare(3, 5, 8, 10)
