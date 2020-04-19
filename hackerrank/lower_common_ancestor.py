#LCA = Lower Common ancesstor
class Node:
    def __init__(self, value=None, left=None, rigth=None):
        self.left = left
        self.rigth = rigth
        self.value = value

    def printMe(self):
        print("{}'".format(self.value))

def isVisited(visited, node):
    return node in visited

def walk(visited, node):
    if node in visited:
        print(visited)
    else:
        visited.append(node)
        node.printMe()
        if node.left is not None:
            walk(visited, node.left)

        if node.rigth is not None:
            walk(visited, node.rigth)     

def lca(root, p, q):
    if root is None:
        return None

    if root.value == p or root.value == q:
        return root.value

    p_found = lca(root.left, p, q)
    q_found = lca(root.rigth, p, q)

    print("First found={}".format(p_found))
    print("Second found={}".format(q_found))

    if p_found is not None and q_found is not None:
        return root.value


    return p_found if p_found is not None else q_found

        

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(5)
    root.rigth = Node(1)

    root.left.left = Node(6)
    root.left.rigth = Node(2)

    root.left.rigth.left = Node(7)
    root.left.rigth.rigth = Node(4)

    root.rigth.left = Node(0)
    root.rigth.rigth = Node(8)

    visited = []
    walk(visited, root)

    p = 6
    q = 4
    print("LCA between {} and {} = {}".format(p,q,lca(root, p, q)))




