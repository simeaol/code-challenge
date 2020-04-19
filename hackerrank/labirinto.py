global ladj
global visited

def dfs(u):
    visited[u] = True

    ret = 0
    for v in ladj[u]:
        if visited[v] == False:
            ret += dfs(v)+1
    
    return ret+1


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        start = int (input())
        V,A = map(int,input().split())
        ladj = [[] for i in range(V)]
        visited = [False] * V
        
        for i in range (A):
            u,v = map(int,input().split())
            ladj[u].append(v)
            ladj[v].append(u)

        result = dfs(start) - 1
        print(result)


