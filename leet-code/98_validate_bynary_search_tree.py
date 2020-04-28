def binary_search_tree(root, lower=float('-inf'), upper=float('inf')):
    if not root:
        return True
    
    val = root.value

    if val <= lower or val >= upper:
        return False
    
    if not binary_search_tree(root.left, lower, val):
        return False

    if not binary_search_tree(root.right, val, upper):
        return False

    return True

class Node:
    def __init__(self, value, left=None, right=None):
        super().__init__()
        self.value = value
        self.left = left
        self.right = right

if __name__== '__main__':
    n1 = Node(1)
    n3 = Node(3)
    n6 = Node(6)
    n4 = Node(4, n3, n6)
    n5 = Node(5, n1, n4)

    result = binary_search_tree(n5)
    print('result = {}'.format(result))


    #this implementation is based on DFS (Depth First Search) algorithm with Time complexity of O(n)