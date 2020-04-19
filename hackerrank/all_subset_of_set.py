import math
def get_subset(arr):
    subset = [None for i in range(len(arr))]
    print(subset)
    helper(arr, subset, 0)

def helper(arr, subset, i):
    if i == len(arr):
        print_subset(subset)
    else:
        subset[i]=None
        i += 1
        if(i > len(arr)):
            helper(arr, subset, i)
            subset[i] = arr[i]
            helper(arr, subset, i)

def print_subset(sub):
    for s in sub:
        print(s)

def naive_solution(S):
    size = len(S) -1
    a = b = c = ''    
    for i in range(size):
        for j in range(size):
            for k in range(size):
                if i == 1:
                    a = S[0]
                if j == 1:
                    b = S[1]
                if k == 1:
                    c = S[2]                
                print("[{}{}{}]".format(a, b, c))
                #print(f"'{'{a}{b}{c}'}''")
                a = b = c = ''
def solution_naive(S):
    total = (int) (math.pow(2, len(S)))
    j = 0
    counter = 0
    for counter in range(total):
        print(f'Counter={counter}')
        for j in range(0, len(S)):
            print(f'j={j}', end="\n")
            value = (counter & (1 << j))
            print(f'value={value}')
            if(counter & (1 << j) > 0):
                print(S[j], end="")
                print()
        print("")


if __name__ == "__main__":
    arr = [1,2]
    get_subset(arr)

    S = ['a', 'b', 'c']
    naive_solution(S) #n^3
    solution_naive(S) #n^2
