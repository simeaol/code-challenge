
def merge_sort(arr, left, right):
    if(left >= right):
        return
    middle = (left + right) // 2
    merge_sort(arr, left, middle)
    merge_sort(arr, middle+1, right)
    merge(arr, middle, left, right)

def merge(arr, middle, left, right):
    leftStart = left
    leftEnd = middle

    rightStart = middle+1

    temp = []

    #while(leftStart <= leftEnd and rightStart <=right):
    for index in range(left, right):
        if(arr[leftStart] < arr[rightStart]):
            temp.append(arr[leftStart])
            leftStart += 1
        elif(arr[left]):
            temp.append(arr[rightStart])
            rightStart += 1
    

    #copy temp array into arr from index left to right
    for i in range(0, len(temp)-1):
        arr[left] = temp[i]
        left += 1

        


if __name__ == '__main__':
    arr = [4, 7, 2, 6, 5, 1, 8, 3]
    print("before: {}".format(arr))
    merge_sort(arr, 0, len(arr)-1)
    print("after: {}".format(arr))