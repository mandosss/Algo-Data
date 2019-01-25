class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, node):
    if root is None:
        root = node
    else:
        if(root.val < node.val):
            if(root.right is None):
                root.right = node
            else:
                insert(root.right, node)
        elif(root.val > node.val):
            if(root.left is None):
                root.left = node
            else:
                insert(root.left, node)

def deleteNode(root, value):
    if(root is None):
        return root
    elif(root.val == value):
        if(root.left is None):
            tempNode = root.right
            #setting null to the root
            root = None
            return tempNode
        elif(root.right is None):
            tempNode = root.left
            #setting null to the root
            root = None
            return tempNode
        temp = minNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)
    elif(root.val < value):
        root.right = deleteNode(root.right, value)
    elif(root.val > value):
        root.left = deleteNode(root.left, value)
    return root

def searchNode(root, value):
    if(root is None):
        print("Not found")
    elif(root.val < value):
        searchNode(root.right, value)
    elif(root.val > value):
        searchNode(root.left, value)
    elif(root.val == value):
        print("Found node: %d"  % root.val)

def preorder(root):
    if(root):
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if(root):
        postorder(root.left)
        postorder(root.right)
        print(root.val)        

#helper functions
def minNode(root):
    topNode = root
    if(topNode.left is None):
        return topNode;
    else:
        topNode = minNode(root.left)       

