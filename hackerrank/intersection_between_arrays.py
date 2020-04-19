#Find the intersection between arrays
#A=[2,6,9,11,13,17] B=[3, 6, 7, 10, 13, 18] and C=[4, 5, 6, 9, 11, 13]
import numpy as np

def intersection(A, B, C):
    x, y, z = 0, 0, 0
    result = []
    while(x < len(A) and y < len(B) and z < len(C)):
        if(A[x] == B[y] == C[z]):
            result.append(A[x])
        if A[x] < B[y]:
            x += 1
        elif B[y] < C[z]:
            y += 1
        else:
            z += 1
    return result

def using_set(A, B, C):
    A1 = np.set(A)
    B1 = np.set(B)
    C1 = np.set(C)
    return A1 - B1 - C1

if __name__ == "__main__":
    A=[2,6,9,11,13,17]
    B=[3, 6, 7, 10, 13, 18] 
    C=[4, 5, 6, 9, 11, 13]
    print("Result={}".format(intersection(A, B, C)))
    print("Set Result={}".format(intersection(A, B, C)))