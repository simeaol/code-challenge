import numpy as np


def find(arr):
    M = np.array(arr)
    nm = np.shape(arr)
    n = nm[0]
    m = nm[1]
    print(m)

    total = 0
    
    i = 0
    j = m-1

    while(j >= 0 and i < n):
        if(M[i][j] < 0):
            total += (j+1)
            i += 1
        else:
            j -= 1

    return total



if __name__ == "__main__":
    m = [[-3, -2, -1, 1], [-2, 2, 3, 4], [4, 5, 7, 8]]
    result = find(m)
    print("{}".format(result))
