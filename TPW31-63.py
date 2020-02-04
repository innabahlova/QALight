import numpy as np


def generate(length, max_value):
    return np.random.randint(0, max_value, length)


a = generate(5, 20)
print(a)
