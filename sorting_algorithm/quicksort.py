def quicksort(arr, left, right):
    if(left >= right):
        return
    p = partition(arr, left, right)
    quicksort(arr, left, p-1)
    quicksort(arr, p+1, right)
    
def partition(arr, left, right):
    pivot = ((left + right) // 2)
    aux = pivot
    while left < right:
        if arr[left] < arr[pivot]:
            left += 1
        elif arr[right] > arr[pivot]:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left
    



if __name__ == "__main__":
    arr = [4, 7, 2, 6, 4, 1, 8, 3]
    print('arr before: {}'.format(arr))
    quicksort(arr, 0, len(arr)-1)
    print('arr after: {}'.format(arr))
