def checkarray(arr):
    visited = {}#HashMap where the key is the character read
    for i in range(0, len(arr)):
        if(arr[i] in visited):
            return arr[i]
        else:
            visited[arr[i]] = 1

    return None

def sum_repeat(arr):
    visited = {}#HashMap where the key is the character read = {'A': 1}
    for i in arr:
        if(i in visited.keys()):
            visited[i] += 1
        else:
            visited[i] = 1
    return visited

if __name__ == "__main__":
    arr = ['A', 'B', 'A', 'D', 'E', 'A']
    result = checkarray(arr)
    print("{}".format(result))

    visited = sum_repeat(arr)
    print("{}".format(visited))


