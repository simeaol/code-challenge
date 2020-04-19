arr = [5,3,2,1,4]
index = 0

for i in range(0, len(arr)):
    min = arr[i]
    for j in range(i+1, len(arr)):        
        if(arr[j] < min):
            min = arr[j]
            index = j
    aux = arr[i]
    arr[i] = min
    arr[index] = aux

print("{}".format(arr))
    

