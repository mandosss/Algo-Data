from BST import *

def main():
    binTree = Node(50)
    insert(binTree,Node(10)) 
    insert(binTree,Node(20)) 
    insert(binTree,Node(30)) 
    insert(binTree,Node(40)) 
    insert(binTree,Node(60)) 
    insert(binTree,Node(70)) 

    print("BEFORE-----------------")
    inorder(binTree)
    #preorder(binTree)
    #postorder(binTree)
    #searchNode(binTree, 60)
    print("AFTER-----------------")
    deleteNode(binTree, 50)
    inorder(binTree)
    print("Addd 60-----------------")
    insert(binTree,Node(50))
    inorder(binTree)

if __name__ == "__main__":
    main()

