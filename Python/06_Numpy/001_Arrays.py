# Problem : https://www.hackerrank.com/challenges/np-arrays/problem
# Score : 10 points(MAX)

import numpy as np


def arrays(arr):
    return np.array(arr, float)[::-1]  # A função recebe uma lista, transforma os numeros em float e por fim trás seu inverso com slicing