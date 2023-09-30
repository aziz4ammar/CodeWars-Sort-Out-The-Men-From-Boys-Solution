import numpy as np
def men_from_boys(arr):
    arr = np.array(arr)
    men = set(arr[arr % 2 == 0])
    boys = set(arr[arr % 2 ==1])
    return sorted(list(men)) + sorted(list(boys), reverse=True)