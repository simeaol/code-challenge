def double_for(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            print("{},{}".format(i,j))

def double_recursive(arr, n):
    if n > len(arr):
        return
    for i in range(0, n+1):
        print("{},{}".format(i, n))
        double_recursive(arr, n+1)



def ways_to_rep_arr(arr):
    memo = {}
    for i in arr:
        for j in arr:
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)
        
def ways_to_rep_arr_recursive(arr, n):
    if n >= len(arr):
        return
    for i in arr:
        arr[n], arr[i] = arr[i], arr[n]
        print(arr)
        #print(f'{n},{i}')
        ways_to_rep_arr_recursive(arr, n+1) 



if __name__ == "__main__":
    arr = [0,1,2]
    double_for(arr)
    double_recursive(arr, 0)
    #ways = num_ways(arr, len(arr)-1)
    #ways_to_rep_arr(arr)
    #ways_to_rep_arr_recursive(arr, 0)