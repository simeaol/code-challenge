import numpy as np


def find(arr):
    m = np.array(arr)
    nm = np.shape(arr)
    max_row = nm[0]
    max_column = nm[1]
    print(m)

    total = 0

    pos = (0, max_column-1)
    for i in range(max_column, 0, -1):
        if(m[pos[0]][pos[1]] > 0):
            pos = 

    return 0


if __name__ == "__main__":
    m = [[-3, -2, -1, 1], [-2, 2, 3, 4], [4, 5, 7, 8]]
    result = find(m)
    # print("{}".format(result))
