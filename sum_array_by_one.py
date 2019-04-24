def sum(arr):
    copy_arr = [0 for i in range(len(arr))] # copy the array with the same len of provided array
    carry = 1 #controller to handle the arrays positions change and to change array length
    for i in range(len(arr), 0, -1):
        s = arr[i-1] + carry
        if(s == 10):
            carry = 1
        else:
            carry = 0
        arr[i-1] = s % 10

    if(carry == 1):
        arr = [0 for i in range(len(arr)+1)]
        arr[0] = 1
    return arr

if __name__ == "__main__":
    arr = [0, 9, 9]
    arr1 = [8, 9, 9]
    arr2 = [9, 9, 9]
    print("{}".format(sum(arr)))
    print("{}".format(sum(arr1)))
    print("{}".format(sum(arr2)))