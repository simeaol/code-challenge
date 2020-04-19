import numpy
def map_evaluated(maps, n, m):
    infected = get_infected_cell(maps, n, m)
    #new_map = numpy.zeros((n,m))
    new_map = []
    new_map.extend(maps)
    visited = []
    queue = []
    for cell in infected:
        queue.append(cell)
        evaluate(maps, queue, visited, new_map, n, m)
    
    return new_map


def evaluate(maps, queue, visited, new_map, n, m):
    print(visited)
    while(len(queue) > 0):
        print(numpy.matrix(new_map))
        cell = queue[0]
        del queue[0] 
        visited.append(cell)
        if len(visited) > m*n:
            return True
        
        i = cell[0]
        j = cell[1]
        if j-1 >= 0: # look for left-side
            queue.append((i, j-1))
            if maps[i][j-1] == 'A' :
                new_map[i][j-1] = 'T'

        if j+1 < m:#rigth-side
            queue.append((i, j+1))
            if maps[i][j+1] == 'A':
                new_map[i][j+1] = 'T'

        if i-1 >= 0:#up-side
            queue.append((i-1, j))
            if maps[i-1][j] == 'A':
                new_map[i-1][j] = 'T'

        if i+1 < n:#bottom-site
            queue.append((i+1, j))
            if(maps[i+1][j] == 'A'):
                new_map[i+1][j] = 'T'

    print(new_map)
    return new_map


def get_infected_cell(maps, n, m):
    infected = []
    for i in range(0, n):
        for j in range(0, m):
            if(maps[i][j] == 'T'):
                infected.append((i, j))
    print("Infected={}".format(infected))
    return infected

if __name__ == "__main__":
    n = 3
    m = 3
    map1 = [['T', 'T', 'T'], ['X', 'X', 'A'], ['A', 'A', 'A']]
    #result = map_evaluated(map1, n, m)
    #print(numpy.matrix(result))

    map2 = [['A', 'T', 'A', 'A'], ['X', 'X', 'A', 'A'], ['A', 'A', 'A', 'X'], ['T', 'X', 'X', 'X']]
    #print(numpy.matrix(map_evaluated(map2, 4, 4)))
    map_evaluated(map2, 4, 4)

    n,m = map(int,input().split())
    maps = numpy.zeros((n,m))
    for i in range(n):
        mpas[i] = map(input().split())
        
    map_evaluated(maps, n, m)