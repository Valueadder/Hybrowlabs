class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+1+size(node.right))


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.value == key:
            return root
        elif root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def search(root, key):
    if root is None or root.value == key:
        return root
    if root.value < key:
        return search(root.right, key)

    # key is smaller than root's key
    return search(root.left, key)


def getSucc(curr, key):
    while curr.left != None:
        curr = curr.left
    return curr.value


def deleteNode(root, key):
    if root == None:
        return
    elif root.value > key:
        root.left = deleteNode(root.left, key)
    elif root.value < key:
        root.ight = deleteNode(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSucc(root.right, key)
            root.value = succ
            root.right = deleteNode(root.right, succ)
    return root


if __name__ == "__main__":
    r = Node(50)
    insert(r, 30)
    insert(r, 20)
    insert(r, 40)
    insert(r, 70)
    insert(r, 60)
    insert(r, 80)
    print(search(r, 20))
    deleteNode(r, 20)
    print(search(r, 20))
