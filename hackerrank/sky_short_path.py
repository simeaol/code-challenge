def solve(m):
    n = len(m)-1
    vis = [[0]*(n+1) for i in range((n+1))]
    queue = [(0, 0)]
    while(len(queue) > 0):
        node = queue[0]
        print('queue begin loop ')
        print(queue)
        del queue[0]
        if(node[0] == n and node[1] == n):
            return True
        if(node[0]+1 <= n and m[node[0]+1][node[1]] != 1 and vis[node[0]+1][node[1]] == 0):
            vis[node[0]+1][node[1]] = 1
            queue.append((node[0]+1, node[1]))
        if(node[1]+1 <= n and m[node[0]][node[1]+1] != 1 and vis[node[0]][node[1]+1] == 0):
            vis[node[0]][node[1]+1] = 1
            queue.append((node[0], node[1]+1))
        if(node[0]+1 <= n  and node[1]+1 <=n and m[node[0]+1][node[1]+1] != 1 and vis[node[0]+1][node[1]+1] == 0):
            vis[node[0]+1][node[1]+1] = 1
            queue.append((node[0]+1, node[1]+1))
        print('queue end loop')
        print(queue)

    return False



if __name__ == "__main__":
    m = [ [0, 0, 0], [0, 1, 1], [0, 1, 0]]
    #m = [ [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = solve(m)
    print("{}".format(result))