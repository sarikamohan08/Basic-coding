class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def PreOrderTraversal(root):
        if(root is None):
            return
        print(root.data,end=' ')
        PreOrderTraversal(root.left)
        PreOrderTraversal(root.right)
        
    
def InOrderTraversal(root):
        if(root is None):
            return
        
        InOrderTraversal(root.left)
        print(root.data,end=' ')
        InOrderTraversal(root.right)

    
def PostOrderTraversal(root):
        if(root is None):
            return
        
        PostOrderTraversal(root.left)
        PostOrderTraversal(root.right)
        print(root.data,end=' ')
        
def main():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.left.left.left=Node(7)
    root.left.left.right=Node(8)


    PreOrderTraversal(root)
    print()
    InOrderTraversal(root)
    print()
    PostOrderTraversal(root)
    print()
    
main()
