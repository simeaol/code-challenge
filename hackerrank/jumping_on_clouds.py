
def jumps(arr):
    total = 0
    cont = 0

    while(cont < len(arr)-1):
        if(arr[cont] == 0 and arr[cont+1] == 0):
            if(cont+2 < len(arr) and arr[cont+2] == 0):
                cont += 2
                total += 1
            else:
                cont += 1
                total += 1
                
        else:
            cont += 2
            total += 1
                
    return total

#=========================================================#
def recursive(arr, result):
    if(len(arr) <= 3):
        print("Stop condition:{}".format(arr))
        return result + 1
    elif(arr[1] == 0 and arr[2] == 0):
        print("Next of the next equal 0: {}".format(arr))
        return recursive(arr[2:], result) + result + 1
    elif(arr[1] == 0):
        print("Next equal 0: {}".format(arr))
        return recursive(arr[1:], result) + result + 1
    elif(arr[2] == 0):
        print("Next equal 1 and next-of-next equal 0: {}".format(arr))
        return recursive(arr[2:], result) + result + 1
    else:
        raise ValueError("Next element is 1 and cannot jump")

if __name__ == "__main__":
    arr =   [0, 0, 1, 0, 0, 1, 0, 0, 0, 0]
    tulpe = (0, 0, 1, 0, 0, 1, 0)
    result = jumps(tulpe)
    #print("{}".format(result))
    print("{}".format(recursive(arr, 0)))


    

