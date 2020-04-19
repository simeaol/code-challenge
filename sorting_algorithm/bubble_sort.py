def bubble_sort(arr): #wrost and median case O(n¨2)
    for i in range(0, len(arr)):
        for j in range (0, i):
            if arr[j] > arr[i]:
                print("swap {} <-> {}".format(arr[j], arr[i]))
                arr[j], arr[i] = arr[i], arr[j]

def sort(arr, n): #best case O(n)
    if n < 0:
        return
    for i in range(0, n):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    sort(arr, n-1)
    
    

if __name__== "__main__":
    arr = [4, 7, 2, 6, 5, 1, 8, 3]
    print("before: {}".format(arr))
    bubble_sort(arr)
    print("after: {}".format(arr))

    arr1 = [4, 7, 2, 6, 5, 1, 8, 3]
    print('best case')
    sort(arr1, len(arr)-1)
    print('best {}'.format(arr1))