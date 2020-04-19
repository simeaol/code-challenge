def quick_sort(arr, target):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return 0 if arr[0] == target else  None

    half = len(arr) // 2
    if arr[half] == target:
        return half
    elif arr[half] < target:
        return quick_sort(arr[half:], target)
    else:
        return quick_sort(arr[:half], target)



if __name__== "__main__":
    arr = [4, 7, 2, 6, 5, 1, 8, 3, 0, 12]
    target = int(input("enter the element: "))
    
    arr.sort() #UICK SORT IS ONLY APPLIYED FOR SORTING ARRAY
    print("{}".format(arr))
    found = quick_sort(arr, target)
    print("element found at position: {}".format(found))
    